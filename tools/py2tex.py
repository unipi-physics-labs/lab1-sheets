#! /usr/bin/env python
#
# Copyright (C) 2012--2025, Luca Baldini (luca.baldini@pi.infn.it).
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

"""Small script to pygmentize Python scripts and generate the corresponding
LaTeX output.
"""

import argparse
import pathlib
import subprocess
import sys

from loguru import logger

# Configure the logger.
logger.remove()
logger.add(sink=sys.stderr, colorize=True, format='>>> <level>{message}</level>')

LAB1SHEETS_GITHUB_URL = 'https://github.com/unipi-physics-labs/lab1-sheets/tree/main'

LAB1SHEETS_ROOT = pathlib.Path(__file__).resolve().parent.parent
LAB1SHEETS_PY = LAB1SHEETS_ROOT / 'snippy'
LAB1SHEETS_TEX = LAB1SHEETS_ROOT / 'sniptex'

_NO_OUTPUT_SCRIPTS = []
_ENCODING = 'utf-8'
_OUTPUT_LATEX_SUBSTITUTIONS = {}


def pygmentize(snippet_path: str = LAB1SHEETS_PY):
    """Run pygments on a python script and generate the corresponding LaTeX output.
    """
    # pylint: disable=use-dict-literal, too-many-locals
    # First thing first, if the path to the snippet(s) is not a pathlib.Path
    # instance, we turn it into one.
    if not isinstance(snippet_path, pathlib.Path):
        snippet_path = pathlib.Path(snippet_path)
    # If the target path does not exist, we raise an exception.
    if not snippet_path.exists():
        raise RuntimeError(f'Target path {snippet_path} does not exist')
    # If the target path is a folder, then we pygmentize all the Python files within
    # the folder calling the function recursively.
    if snippet_path.is_dir():
        logger.info(f'Pygmentizing folder {snippet_path}...')
        for _path in snippet_path.iterdir():
            if _path.is_file() and _path.suffix == '.py':
                pygmentize(_path)
        return
    if snippet_path.is_file() and snippet_path.suffix != '.py':
        raise RuntimeError(f'{snippet_path} is not a python file')

    # Now we are good to go with a single, good Python file!
    file_path = snippet_path.resolve()
    logger.info(f'Pygmentizing {file_path}...')
    # Pygmentize the script.
    cmd = f'pygmentize -f latex -O full -l python {file_path}'
    kwargs = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    with subprocess.Popen(cmd, **kwargs) as process:
        snippet_tex = process.stdout.read().decode()
    # Note at this point the LaTeX source is complete document with a long preamble,
    # and all we really care is whatever lies in the Verbatim block.
    snippet_tex = snippet_tex.split(r'\begin{Verbatim}[commandchars=\\\{\}]')[1]
    snippet_tex = snippet_tex.split(r'\end{Verbatim}')[0]

    # Complete the information with the url to the snippet on github.
    url = f'{LAB1SHEETS_GITHUB_URL}{str(file_path).replace(str(LAB1SHEETS_ROOT), "")}'
    file_name = file_path.name.replace('_', r'\_')
    title = f'https://github.com/.../{file_name}'
    label = r'\makebox{\href{%s}{%s}}' % (url, title)

    # We are ready to write the output file.
    full_text = r'\begin{Verbatim}[label=%s,commandchars=\\\{\}]' % label
    full_text = f'{full_text}{snippet_tex}'
    full_text = '%s\\end{Verbatim}\n' % full_text
    output_file_path = LAB1SHEETS_TEX / f'{file_path.stem}.tex'
    with open(output_file_path, 'w', encoding=_ENCODING) as output_file:
        output_file.write(full_text)
    logger.info('Done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target')
    args = parser.parse_args()
    pygmentize(args.target)
