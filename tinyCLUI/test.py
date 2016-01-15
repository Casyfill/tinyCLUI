#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import tinyCLUI

def test():
	'''testing the functional'''
	print 'Test'

	print tinyCLUI.askForAnswer(['I like TinyCLUI','I dont like TinyCLUI'])

	print tinyCLUI.askForAnswer({'NY': 'New York', 'Al':'Alabama'},'Which State are you living in?')

	# ask for file
	print tinyCLUI.askForFile(exist=True, 
					 frmt='.png',
					 default=False
					 )
	
	#  ask for directory
	print tinyCLUI.askForDir(question = 'Please, provide existing or new directory to use',
					 exist=False
					 )

	print tinyCLUI.askBoolean('Did you stop drinking cognac in the mornings?', default=False)

	print tinyCLUI.askInt('How old are you?')



if __name__ == '__main__':
	test()