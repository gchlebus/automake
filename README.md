# automake
[![Build Status](https://travis-ci.com/gchlebus/automake.svg?branch=master)](https://travis-ci.com/gchlebus/automake)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Run make automatically on sources change.

## Installation instructions
```
git clone https://github.com/gchlebus/automake.git
cd automake
pip install -r requirements.txt
install automake /usr/local/bin
```

## Usage
```
usage: automake [-h] [-f FILENAME] [-t TARGET] [-d]

Run make automatically on source files change.

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME, --makefilename FILENAME
                        name of the makefile (default "Makefile")
  -t TARGET, --target TARGET
                        make target (default "all")
  -d, --debug           toggle debug mode
```
