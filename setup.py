from setuptools import setup

APP = ['game/maze_runner.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
