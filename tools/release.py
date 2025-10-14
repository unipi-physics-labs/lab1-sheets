#!/usr/bin/env python
#
# Copyright (C) 2016--2025, Luca Baldini (luca.baldini@pi.infn.it).
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

""" Rudimentary release manager.
"""


import argparse
import pathlib
import subprocess
import shutil
import sys

from loguru import logger

# Configure the logger.
logger.remove()
logger.add(sink=sys.stderr, colorize=True, format='>>> <level>{message}</level>')


LAB1SHEETS_ROOT = pathlib.Path(__file__).resolve().parent.parent

VERSION_FILE_PATH = LAB1SHEETS_ROOT / 'version.tex'
#README_FILE_PATH = LAB1SHEETS_ROOT / 'README.md'
GITHUB_RELEASE_URL = 'https://github.com/unipi-physics-labs/lab1-sheets/releases'

INCREMENT_MODES = ('major', 'minor', 'patch')

_ENCODING = 'utf-8'


def execute_shell_command(arguments):
    """Execute a shell command.
    """
    logger.info(f'About to execute "{" ".join(arguments)}"...')
    return subprocess.run(arguments, check=True)


def copy_file(src, dest):
    """ Copy a file in another location.
    """
    logger.info('Copying {src} to {dest}...')
    shutil.copy(src, dest)


def _read_version():
    """ Read the version straight from the appropriate file.
    """
    logger.info(f'Reading version from {VERSION_FILE_PATH}...')
    with open(VERSION_FILE_PATH, encoding=_ENCODING) as version_file:
        version = version_file.readline().strip('\n')
    logger.debug(f'Current version is {version}')
    return version


def _write_version(version: str):
    """ Write the version to the appropriate file.
    """
    logger.info(f'Writing version {version} to {VERSION_FILE_PATH}...')
    with open(VERSION_FILE_PATH, 'w', encoding=_ENCODING) as version_file:
        version_file.write(f'{version}\n')


def increment_version_file(mode: str) -> str:
    """Update the version.tex file.
    """
    logger.info(f'Bumping version file (mode = {mode})...')
    if mode not in INCREMENT_MODES:
        raise RuntimeError(f'Invalid increment mode "{mode}"---valid modes are {INCREMENT_MODES}')
    old_version = _read_version()
    major, minor, patch = (int(item) for item in old_version.split('.'))
    if mode == 'major':
        major += 1
        minor = 0
        patch = 0
    elif mode == 'minor':
        minor += 1
        patch = 0
    elif mode == 'patch':
        patch += 1
    new_version = f'{major}.{minor}.{patch}'
    logger.info(f'Target version is {new_version}')
    _write_version(new_version)
    return new_version


# def compile_latex():
#     """ Recompile the damned thing.
#     """
#     execute_shell_command(['make'])


# def _asset_url(name: str, version: str) -> str:
#     """ Return the URL for an asset.
#     """
#     return f'{GITHUB_RELEASE_URL}/download/{version}/{name}-{version}.pdf'

# def write_readme(version: str) -> None:
#     """ Write the README file.
#     """
#     pass

def release(mode: str) -> None:
    """ Tag the package and create a release.
    """
    execute_shell_command(['git', 'pull'])
    version = increment_version_file(mode)

    msg = f'Prepare for tag {version}.'
    execute_shell_command(['git', 'commit', '-a', '-m', msg])
    execute_shell_command(['git', 'push'])
    msg = f'Tagging version {version}...'
    execute_shell_command(['git', 'tag', '-a', version, '-m', msg])
    execute_shell_command(['git', 'push', '--tags'])
    execute_shell_command(['git', 'status'])
    logger.info(f'Release {version} completed successfully.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, choices=INCREMENT_MODES, help='Version increment mode')
    args = parser.parse_args()
    release(args.mode)
