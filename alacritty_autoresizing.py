#!/usr/bin/python3

import os
import re
import runpy
import subprocess
import sys
import tempfile

import xdg.BaseDirectory
import ruamel.yaml


def main():
    find_config = xdg.BaseDirectory.load_first_config
    base_config = find_config('alacritty', 'alacritty.yml')
    resizing_config = find_config('alacritty', 'autoresizing.cfg.py')
    assert base_config is not None
    assert resizing_config is not None

    with open(base_config) as f:
        yaml = ruamel.yaml.YAML(typ='safe')
        cfg = yaml.load(f)

    with tempfile.NamedTemporaryFile(delete=False) as output_config:
        output_config.write(b'live_config_reload: true')
        output_config_path = output_config.name

    p = subprocess.Popen(['alacritty',
                          '-o', 'live_config_reload=true',
                          '--config-file', output_config_path,
                          '--print-events',
                          *sys.argv[1:]],
                         stdout=subprocess.PIPE)

    prev_params = None
    width, height, scale_factor = None, None, 1
    while True:
        l = p.stdout.readline()
        if not l:
            break
        ms = re.search(rb'ScaleFactorChanged { scale_factor: ([\d\.+])', l)
        md = re.search(rb'PhysicalSize { width: (\d+), height: (\d+) }', l)
        if md:
            width, height = int(md.group(1)), int(md.group(2))
        if ms:
            scale_factor = int(ms.group(1))
        if (ms or md) and width and height:
            param_func = runpy.run_path(resizing_config)['font']
            params = param_func(width, height, scale_factor)
            if params != prev_params:
                with open(output_config_path, 'w') as output_config_file:
                    cfg['font'].update(params)
                    yaml.dump(cfg, output_config_file)
            prev_params = params
    os.unlink(output_config_path)


if __name__ == '__main__':
    main()
