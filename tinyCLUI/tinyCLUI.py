#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os

class TerminateError(Exception):
	'''
	Process terminate error - helps exit the process 
	if exit notation was entered
	'''

	def __init__(self, qletter='Q', eString=' was entered, Process Terminated'):
		self.qletter=qletter
		self.eString = eString

	def __str__(self):
		return self.qletter + self.eString


def terminator(f, qletter='Q'):
	def inner(*args, **kwargs):
		
		try:
			r = f(*args, **kwargs)
			if qletter in r:
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
def askForPath(question='Please, provide a path', exist=True, filepath=True, frmt=None, default=None, exitOnError=False, create=False, qletter='Q', dletter='D'):
	'''ask user to input the path to folder or file'''

	if default:
		question = question + ' or pass %s for default.\nDefault option: %s' % (dletter, str(default))
	
	condition = pathCondition(exist, filepath, frmt, default, create, qletter, dletter) 

	r = infQuestion(question, condition, exitOnError)

	# NOTE: should be a more clean way to do that (inside infQuestion?)
	if r == dletter:
		return default
	else:
		return r




def test():
	'''testing the functional'''
	print 'Test'

	print askForAnswer(['I like TinyCLUI','I dont like TinyCLUI'])

	print askForAnswer({'NY': 'New York', 'Al':'Alabama'},'Which State are you living in?')

	print askForPath(exist=True, 
					 filepath=True,
					 frmt='.png',
					 default='/Users/casy/Dropbox/Screenshots/Screenshot 2015-10-03 12.41.28.png',
					 )
	#  ask for directory
	print askForPath(question = 'Please, provide existing or new directory to use',
					 exist=False, 
					 filepath=False,
					 create=True
					 )


if __name__ == '__main__':
	test()



	
