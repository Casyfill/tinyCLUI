#!/usr/bin/env python
#-*- coding: utf-8 -*-


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
		print args, kwargs
		
		try:
			r = f(*args, **kwargs)
			if qletter in r:
				raise TerminateError(qletter=qletter)
			return r
		except TerminateError, e:
			print
			print str(e)

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
	'''return checker if result in the option index'''
	l = [str(x) for x in options.keys()]
	
	def checker(r):
		return (r==qletter) or (r in l)
	return checker


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

	if exitOnError==True:
		r = raw_input(question)
		if condition(r):
			return r
		else:
			print 'answer is invalid. passing'
			pass
	elif exitOnError==False:
		while True:
			r = raw_input(question)
			if condition(r):
				return r
			else:
				print 'answer is invalid. try again!'

	


if __name__ == '__main__':
	print 'test'
	opt = {'f':'foo','b':'bar','0':'banana'}
	result = askForAnswer(opt)
	print opt[result]
