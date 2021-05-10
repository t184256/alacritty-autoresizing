#!/usr/bin/python3

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
    while True:
        l = p.stdout.readline()
        if not l:
            break
        m = re.search(rb'PhysicalSize { width: (\d+), height: (\d+) }', l)
        if m:
            width, height = int(m.group(1)), int(m.group(2))
            params = runpy.run_path(resizing_config)['font'](width, height)
            if params != prev_params:
                with open(output_config_path, 'w') as output_config_file:
                    cfg['font'].update(params)
                    yaml.dump(cfg, output_config_file)
            prev_params = params
