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
script is designed for python 2.7 and requies nothing but `sys` module

## Example

```
from tinyCLUI import askForAnswer

print askForAnswer(['I like TinyCLUI','I dont like TinyCLUI'])

print askForAnswer({'NY': 'New York', 'Al':'Alabama'},'Which State are you living in?')

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
