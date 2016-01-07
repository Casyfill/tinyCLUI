#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
# TODO: would be great to have an option to print any condition for the question

class TerminateError(Exception):
	'''
	Process terminate error - helps exit the process 
	if exit notation was entered
	'''
	# TODO: replace D with enter as a default passkey

	def __init__(self, qletter='Q', eString=' was entered, Process Terminated'):
		self.qletter=qletter
		self.eString = eString

	def __str__(self):
		return self.qletter + self.eString


def terminator(f, qletter='Q'):
	def inner(*args, **kwargs):
		
		try:
			r = f(*args, **kwargs)
			if qletter==r:
				raise TerminateError(qletter=qletter)
			return r
		except TerminateError, e:
			print
			print str(e)
			exit()

	return inner

def lcond(options, qletter):
	'''return checker if result in the option index'''
	l = range(len(options))
	def checker(r):
		try:
			return (r==qletter) or (int(r) in l)
		except ValueError,e:
			print str(e)

	return checker

def kcond(options, qletter):
	'''return checker if result in the option keys'''
	l = [str(x) for x in options.keys()]
	
	def checker(r):
		return (r==qletter) or (r in l)
	return checker

def pathCondition(exist, filepath, frmt, default, create, qletter, dletter):
	'''return checker if result path is valid'''

	def checker(r):
		'''TODO: should rise error with explanation'''
		r = r.strip()

		if r == qletter:
			return True

		
		# check/use default option
		if default and r==dletter:
			print 'Default option chosen: ', default
			r = default

		if not filepath: #directory
			result = os.path.isdir(r)
			
			if result==False and create==True:
				# TODO :should print a create option
				os.makedirs(r)
				result = True
					
		else:
			result = os.path.exists(r)

			if frmt!=None:
				result = result and r.endswith(frmt)

		
		if exist:
			# NOTE: a flaw - user can pass total nonsence and get True on checker
			result = True
		return result

	return checker



def bcond(yletter,nletter,qletter,default):
	'''boolean conditioning'''

	def checker(r):
		if default!=None:
			opts = ('', yletter, nletter,qletter)
		else:
			opts = ( yletter, nletter,qletter)

		return r in opts

	return checker



def	intCondition(custom_condition, qletter, default):
	'''integer conditioner'''
	# TODO: add few custom int condition helpers
	
	def checker(r):
		if r==qletter:
			return True

		elif default!=None and  r == '':
			result = True
			

		else:
			try:
				x = int(r)
				result = True
			except:
				result = False

		if custom_condition:
			return result and custom_condition(r)
		else:
			return result

	return checker

# TODO: add few custom float condition helpers

def infQuestion(question, condition, exitOnError):
	'''asking strategy'''

	if exitOnError==True:
		r = raw_input(question + '\n')
		if condition(r):
			return r
		else:
			print 'answer is invalid. passing'
			return None

	elif exitOnError==False:
		while True:
			r = raw_input(question + '\n')
			if condition(r):
				return r
			else:
				print 'answer is invalid. try again!'
	elif type(exitOnError)== int and exitOnError>0:
		# TODO: Implement
		# TODO: create Not-Implemented error
		print 'Not Implemented yet'

@terminator
def askForAnswer(options, question='Please, chouse your answer, Q to exit:', condition=None, exitOnError=False, qletter='Q'):
	'''
	asks user to input the answer, then passes it as type

	options - list of possible options, supporting
	 1. list/tuple  -automatically enumerates and waits for numeric. Sorting is not supported yet
	 2. dictionaries key-name for abbreviation (support only str keys)
	 3. ranges NOT SUPPORTED YET

	 question - question to ask

	 condition - function, inputing raw answer which returning true/false, defines whatever the answer is valid.
	 by default, checks whatever answer is in the list of options (index for lists/tuples, key fo dicts)

	 exitOnError - boolean/ positive integer, defines if question  should be questioned again on invalid input
	 on True, stays in infinite loop, until the answer is valid
	 on False, rises terminate error after first invalid answer. on integer, asks that many time before exiting.
	 '''


	if type(options) == list or type(options) == tuple:
		condition = lcond(options, qletter)
		print
		# print quiestion
		for i, q in enumerate(options):
			print '%d. %s' % (i, q)

		
		
		
	elif type(options) == dict:
		condition = kcond(options,qletter)
		print
		for k,v in options.iteritems():
			print '%s. %s' % (str(k), v)

	return infQuestion(question, condition, exitOnError)
	

	

@terminator
def askForPath(question='Please, provide a path, Q to exit, enter to skip(use default):', exist=True, filepath=True, frmt=None, default=None, exitOnError=False, create=False, qletter='Q'):
	'''ask user to input the path to folder or file'''
	# TODO: allow custom conditions to be made, for example if files inside folder are requred
	# TODO: split to askForFolder, askForFile
	dletter = ''
	
	if default:
		question = question + ' or pass %s for default.\nDefault option: %s' % (dletter, str(default))
	
	condition = pathCondition(exist, filepath, frmt, default, create, qletter, dletter) 

	r = infQuestion(question, condition, exitOnError)

	# NOTE: should be a more clean way to do that (inside infQuestion?)
	if r == dletter:
		return default
	else:
		return r

@terminator
def askBoolean(question='Did you stop drinking cognac in the mornings?', default=None, yletter='y', nletter='n', qletter = 'Q', exitOnError=False):
	'''returns True or False'''
	question = '\n' + question + '\nyes (*) or no(#), Q to exit, enter to skip(use default):'
	question = question.replace('*', yletter).replace('#',nletter)

	condition = bcond(yletter,nletter,qletter,default)
	r = infQuestion(question, condition, exitOnError)

	result =  {'':default,
	        yletter: True,
	        nletter: False,
	        qletter: qletter}[r]
	print 'Chosen: ', result
	return result


@terminator
def askInt(question='How old are you?', default=None, custom_condition=None, qletter = 'Q', exitOnError=False):
	'''returns True or False'''
	
	condition = intCondition(custom_condition, qletter, default)
	r = infQuestion(question, condition, exitOnError)
	
	if default and r=='':
		print 'Chosen:', default
		return default
	elif r==qletter:
		return r
	else:
		return int(r)

# TODO: add askFloat


def test():
	'''testing the functional'''
	print 'Test'

	# print askForAnswer(['I like TinyCLUI','I dont like TinyCLUI'])

	# print askForAnswer({'NY': 'New York', 'Al':'Alabama'},'Which State are you living in?')

	# print askForPath(exist=True, 
	# 				 filepath=True,
	# 				 frmt='.png',
	# 				 default='/Users/casy/Dropbox/Screenshots/Screenshot 2015-10-03 12.41.28.png',
	# 				 )
	# #  ask for directory
	# print askForPath(question = 'Please, provide existing or new directory to use',
	# 				 exist=False, 
	# 				 filepath=False,
	# 				 create=True
	# 				 )

	# print askBoolean('Did you stop drinking cognac in the mornings?', default=False)

	print askInt('How old are you?')



if __name__ == '__main__':
	test()



	
