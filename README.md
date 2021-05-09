# gendiff

## Badges
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
[![Github Actions Status](https://github.com/sound-round/python-project-lvl2/workflows/linter/badge.svg)](https://github.com/sound-round/python-project-lvl2/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/aca4a90a1b44065aa4cb/test_coverage)](https://codeclimate.com/github/sound-round/python-project-lvl2/test_coverage)

### Hexlet tests and linter status:
[![Actions Status](https://github.com/sound-round/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/sound-round/python-project-lvl2/actions)

## Description
gendiff — a program that determines the difference between two data structures.
Utility features:

- Support for different input formats: yaml, json,
- Generating a report in plain text, stylish, and json format.

## Visuals

Demo gendiff on asciinema with JSON-files: 

[![asciicast](https://asciinema.org/a/9I8ZsgT8LnxECxJzBEfwrWTr4.svg)](https://asciinema.org/a/9I8ZsgT8LnxECxJzBEfwrWTr4)

Demo gendiff on asciinema with YAML-files: 

[![asciicast](https://asciinema.org/a/rsDtBpFh0TFutligAmkCXZYFJ.svg)](https://asciinema.org/a/rsDtBpFh0TFutligAmkCXZYFJ)

Demo gendiff on asciinema with nested files: 

[![asciicast](https://asciinema.org/a/OsQSqcoERvqMoo49nPH0iRX8M.svg)](https://asciinema.org/a/OsQSqcoERvqMoo49nPH0iRX8M)

Demo gendiff on asciinema with plain-format:

[![asciicast](https://asciinema.org/a/b8a9A5jvxQRiX0jNMAQJF0Xjq.svg)](https://asciinema.org/a/b8a9A5jvxQRiX0jNMAQJF0Xjq)

Final demo gendiff on asciinema: 

[![asciicast](https://asciinema.org/a/H7B6zgyNqVCS78oPnfzfe6nX3.svg)](https://asciinema.org/a/H7B6zgyNqVCS78oPnfzfe6nX3)


## Install
Use the following commands to install gendiff:
```
make build
make package-install
make install
```

## Local testing
Use the following command to test the package:
```
make lint
```

## Commands and options
```
$ gendiff -h   
usage: gendiff [-h] [-f {stylish,plain,json}] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f {stylish,plain,json}, --format {stylish,plain,json}
                        set format of output (default: "stylish") 
```

## Support
If you have questions you can email me to yudaev1@gmail.com

## Links
This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [flake8](https://flake8.pycqa.org/en/latest/)                               | "The tool for style guide enforcement"                  |
| [code climate](https://codeclimate.com/)                                    | "Actionable metrics for engineering"                    |
| [github actions](https://github.com/features/actions)                       | "Automatization software workflows with  CI/CD"          |

