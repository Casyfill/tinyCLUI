TinyCLUI
========


TinyCLUI is a small script helper, that simplifies the tedeous process of creating the carefull command line interface for your script.

## CREDITS

There are numerous options for that on the market: 
- [Click](http://click.pocoo.org/5/)
- optparse and argparse
- [docopt](http://docopt.org/)

Yes, this is one another implementation of what is presented in dozens of modules on the internet.
this one is mine and designed to: 

1. Practice slightly more comlpex development
2. write a tiny alternative that can be easy to inherit into the script, avoiding creation of one more exotic dependency

## Installation

Intentionally script is designed to be stored as a script, not a module. to aviod dependencies.
To use it's functionality, place script folder inside your main script folder and import it to the script:

```
from tinyCLUI import askForAnswer

r = askForAnswer(['I like TinyCLUI','I dont like TinyCLUI'])

```

## Dependencies
script is designed for python 2.7 and requies nothing but `os` module

## Example

```
from tinyCLUI import askForAnswer

print askForAnswer(['I like TinyCLUI','I dont like TinyCLUI'])

print askForAnswer({'NY': 'New York', 'Al':'Alabama'},'Which State are you living in?')

print askForPath(exist=True, 
				 filepath=True,
				 frmt='.png',
				 default='/Users/casy/Dropbox/Screenshots/Screenshot 2015-10-03 12.41.28.png',
				 )

#  ask for directory
print askForPath(question = 'Please, provide existing or new directory to use',exist=False, filepath=False, create=True )


```

## LOG

- [X] Q must stop entire process (?)
- [X] settings file
- [X] add newline to each question
- [X] separate path asks
- [X] support floatAsk
- [X] conditions
- [ ] support custom_conditions
- [ ] helper custom_conditions (range, positive, etc)

- [ ] default ask function or/and condition wrapper

- [ ] file/dir path: create if need (???) optional condition
- [ ] handle answer types

- [ ] rewrite AskStrategy, support numerical attempts

- [ ] TEST (bulk questionary)
- [ ] TEST support json/object input


- REPORT function
- LOG function
- IterativeAnswer function
