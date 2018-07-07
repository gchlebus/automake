# automake
Run make automatically on sources change.

## Installation instructions
```
cd clone_directory
pip install -r requirements.txt
install automake /usr/local/bin
```

## Usage
```
usage: automake [-h] [--makefilename MAKEFILENAME] [--cmd CMD] [--debug]

Runs make automatically on source files change.

optional arguments:
  -h, --help            show this help message and exit
  --makefilename MAKEFILENAME
                        Name of the makefile (default "Makefile")
  --cmd CMD             make command (default "all")
  --debug               Run in debug mode.
```
