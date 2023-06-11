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
    output_config_path = tempfile.NamedTemporaryFile(prefix='alacritty.',
                                                     delete=False).name

    with open(base_config) as f:
        yaml = ruamel.yaml.YAML(typ='safe')
        cfg = yaml.load(f)

    def update_config(font_params):
        with open(output_config_path, 'w') as output_config_file:
            cfg['font'].update(font_params)
            yaml.dump(cfg, output_config_file)

    update_config({})

    p = subprocess.Popen(['alacritty',
                          '-o', 'live_config_reload=true',
                          '--config-file', output_config_path,
                          '--print-events',
                          *sys.argv[1:]],
                         stdout=subprocess.PIPE)

    prev_params = None
    width, height, scale_factor = None, None, 1
    logfile_killed = False
    while True:
        l = p.stdout.readline()
        if not l:
            break
        if not logfile_killed:
            os.symlink('/dev/null', f'/tmp/{p.pid}.tmp')
            os.replace(f'/tmp/{p.pid}.tmp', f'/tmp/Alacritty-{p.pid}.log')
            logfile_killed = True
        ms1 = re.search(rb'Window scale factor: ([\d\.+])', l)
        ms2 = re.search(rb'ScaleFactorChanged { scale_factor: ([\d\.+])', l)
        md = re.search(rb'PhysicalSize { width: (\d+), height: (\d+) }', l)
        if md:
            width, height = int(md.group(1)), int(md.group(2))
        if ms1:
            scale_factor = int(ms1.group(1))
        if ms2:
            scale_factor = int(ms2.group(1))
        if (ms1 or ms2 or md) and width and height:
            param_func = runpy.run_path(resizing_config)['font']
            params = param_func(width, height, scale_factor)
            if params != prev_params:
                update_config(params)
            prev_params = params
    os.unlink(output_config_path)


if __name__ == '__main__':
    main()
