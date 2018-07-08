# automake
[![Build Status](https://travis-ci.com/gchlebus/automake.svg?branch=master)](https://travis-ci.com/gchlebus/automake)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Run make automatically on sources change.

## Installation instructions
```
cd clone_directory
pip install -r requirements.txt
install automake /usr/local/bin
```

## Usage
```
usage: automake [-h] [--makefilename MAKEFILENAME] [--target TARGET] [--debug]

Runs make automatically on source files change.

optional arguments:
  -h, --help            show this help message and exit
  --makefilename MAKEFILENAME
                        Name of the makefile (default "Makefile")
  --target TARGET       Make target (default "all")
  --debug               Run in debug mode.
```
