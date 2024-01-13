from setuptools import setup

setup(
    name='alacritty_autoresizing',
    version='0.0.1',
    url='https://github.com/t184256/alacritty_autoresizing',
    author='Alexander Sosedkin',
    author_email='monk@unboiled.info',
    description='Wrapper that makes alacritty terminal scale fonts on resize',
    py_modules=['alacritty_autoresizing'],
    install_requires=['pyxdg', 'toml'],
    entry_points='''
        [console_scripts]
        alacritty-autoresizing=alacritty_autoresizing:main
    ''',
)
