TinyCLUI
========


TinyCLUI is a small script helper, that simplifies the tedeous process of creating the carefull command line interface for your script.

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

- handle answer types
- Q must stop entire process (?)
- add newline to each question
- support numerical attempts
- support range

- REPORT function
- LOG function
- IterativeAnswer function
