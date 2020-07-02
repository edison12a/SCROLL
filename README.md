SCROLL: Automatically generates documentation and unit-tests for python programs
=======
**Built with Data processing programs in mind**


[![PyPI version](https://badge.fury.io/py/scroll.svg)](https://badge.fury.io/py/scroll)
[![Downloads](https://pepy.tech/badge/scroll)](https://pepy.tech/project/scroll)
[![Python 3.6](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)


## How it works
This tool monitors your function calls and returns while you "exercise" you program (i.e run functional tests).
It will collect this information (traces), record the order in which your functions run and generate documentations / tests using that information.


# Design concept
The final goal is to enable a developer/user browser through documentation that flows
in the order in which functions in the program run, hence the name SCROLL.


## Installation

```bash
pip install scroll
```

To install using wheel files, Check in [Distribution files](./dist)


## Example Usage
Lets say your file which contains the main entry function is called main.py

### An example main file with an entry function
```
# main.py

def run():
    '''this is your singlr entry function'''
    # your code here


if __name__ == '__main__':
    run()
```

### Run the file using scroll on bash 
```bash
scroll main.py
```


## How about some guidelines?
- There should be only one main entry function into you code
- 

## To-Do
- add creating of url with class name / func name ancored on it
- add creating of SCROLL.md that has scroll of all functions

## Contributing

To get started contributing, Visit the [CONTRIBUTING GUIDE](./CONTRIBUTING.MD)


## Contributors and acknowledgment
1. Edison Abahurire [simicode](https://github.com/SimiCode)


## Similar Libraries that do Runtime-Introspection:
1. [pythoscope](https://github.com/mkwiatkowski/pythoscope) for Auto unit-test generation
2. [auger](https://github.com/laffra/auger) for Auto Unit-test generation
3. [MonkeyType](https://github.com/Instagram/MonkeyType) for auto Auto Type hinting /  Annotation
4. [hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html) for Auto test-case generation


## License
[MIT](https://choosealicense.com/licenses/mit/)


## Credits
3. [MonkeyType](https://github.com/Instagram/MonkeyType): Whan I got this idea, My first option was to just plagiarise their code ;)


Packaged with: [Flit](https://buildmedia.readthedocs.org/media/pdf/flit/latest/flit.pdf)
