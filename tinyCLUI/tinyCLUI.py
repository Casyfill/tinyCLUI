#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os


from settings import settings
from conditions import *   # redesign
# TODO: would be great to have an option to print any condition for the question

class TerminateError(Exception):
	'''
	Process terminate error - helps exit the process 
	if exit notation was entered
	'''
	

	def __init__(self, 
				 qletter=settings['terminate'], 
				 eString=settings['eString']):

		self.qletter=qletter
		self.eString = eString

	def __str__(self):
		return self.qletter + self.eString

def terminator(f, qletter=settings['terminate']):
	'''wrapper around the question, 
	that allows to terminate it'''

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


#### QUESTION STRATEGY

def infQuestion(question, condition, exitOnError):
	'''asking strategy'''
	#  TODO implement tryCounter, and rewrite
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


##### QUESTIONS

@terminator
def askForAnswer(options, 
	             question='Please, chouse your answer, Q to exit:', 
	             condition=None, 
	             exitOnError=False, 
	             default=None,
	             qletter=settings['terminate'], 
	             dletter = settings['default']):
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
	
	question = '\n' + question

	if default:
		question = question + ' or pass %s for default.\nDefault option: %s' % (dletter, str(default))

	if type(options) == list or type(options) == tuple:
		condition = lcond(options, qletter)
		
		# now print the options
		print
		# print quiestion
		for i, q in enumerate(options):
			print '%d. %s' % (i, q)

				
	elif type(options) == dict:
		condition = kcond(options,qletter)
		print
		for k,v in options.iteritems():
			print '%s. %s' % (str(k), v)

	r = infQuestion(question, condition, exitOnError)

	if r == dletter:
		return default
	else:
		return r
	


@terminator
def askForFile(question='Please, provide a path to file, Q to exit, enter to skip(use default):', 
			   exist=True,   					# if file should exist
			   
			   frmt=None,    					# specific format (.txt for example)
			   default=None,                    # default option 
			   exitOnError=False, 				# exit if error
			   qletter=settings['terminate'], 
			   dletter=settings['default']):

	'''ask user to input the path to folder or file'''
	question = '\n' + question	
	# TODO: allow custom conditions to be made, for example if files inside folder are requred
	# TODO: split to askForFolder, askForFile
	# TODO: multiple frmt
	
	if default:
		question = question + ' or pass %s for default.\nDefault option: %s' % (dletter, str(default))
	
	if frmt:
		question = question + '\nFile should be of %s format' % (frmt)
	

	condition = fileCondition(exist, frmt, default, qletter, dletter) 

	r = infQuestion(question, condition, exitOnError)

	# NOTE: should be a more clean way to do that (inside infQuestion?)
	if r == dletter:
		return default
	else:
		return r

@terminator
def askForDir(question='Please, provide a directory path, Q to exit', 
			   exist=True,   					# if file should exist
		
			   default=None,                    # default option 
			   exitOnError=False, 				# exit if error
			   qletter=settings['terminate'], 
			   dletter=settings['default']):

	'''ask user to input the path to folder or file'''
	question = '\n' + question
	# TODO: allow custom conditions to be made, for example if files inside folder are requred
	# TODO: split to askForFolder, askForFile
	
	if default:
		question = question + ' or pass %s for default.\nDefault option: %s' % (dletter, str(default))
	
	condition = dirCondition(exist, default, qletter, dletter) 

	r = infQuestion(question, condition, exitOnError)

	# NOTE: should be a more clean way to do that (inside infQuestion?)
	if r == dletter:
		return default
	else:
		return r

@terminator
def askBoolean(question='Did you stop drinking cognac in the mornings?', 
			   default=None, 
			   yletter=settings['yes'], 
			   nletter=settings['no'], 
			   qletter = settings['terminate'], 
			   dletter=settings['default'],
			   exitOnError=False):
	'''returns True or False'''
	
	question = '\n' + question
	question = question + '\nyes (*) or no(#), Q to exit, enter to skip(use default):'
	question = question.replace('*', yletter).replace('#',nletter)

	condition = bcond(yletter,nletter,qletter, dletter, default)
	r = infQuestion(question, condition, exitOnError)

	result =  {'':default,
	        yletter: True,
	        nletter: False,
	        qletter: qletter}[r]
	print 'Chosen: ', result
	return result


@terminator
def askInt(question='How old are you?', 
		   default=None, custom_condition=None, 
		   qletter = settings['terminate'], 
		   dletter = settings['default'],
		   exitOnError=False):
	
	'''returns Integer'''
	
	question = '\n' + question
	condition = intCondition(custom_condition, qletter, dletter, default)
	r = infQuestion(question, condition, exitOnError)
	
	if default and r=='':
		print 'Chosen:', default
		return default
	elif r==qletter:
		return r
	else:
		return int(r)

@terminator
def askFloat(question='How do you like it so far?', 
		     default=None, custom_condition=None,
		     rMin = 0, rMax = 1, 
		     qletter = settings['terminate'], 
		     dletter = settings['default'],
		     exitOnError=False):
	
	'''returns Float'''
	
	question = '\n' + question
	

	condition = rangeCondition(custom_condition, qletter, dletter, default)
	r = infQuestion(question, condition, exitOnError)
	
	if default and r=='':
		print 'Chosen:', default
		return default
	elif r==qletter:
		return r
	else:
		return float(r)


