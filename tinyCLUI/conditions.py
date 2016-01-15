#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os

## CONDITIONS

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



def fileCondition(exist, frmt, default, qletter, dletter):
	'''return checker defining if result filePath is valid'''

	def checker(r):
		'''TODO: should rise error with explanation
		   NOTE: for now cant build new folders'''

		r = r.strip()

		if r == qletter:
			return True

		# check/use default option
		if default and r==dletter:
			print 'Default option chosen:\n', default
			r = default

		if exist:

			if frmt!=None:
				print os.path.exists(r)
				result = os.path.exists(r) and r.endswith(frmt)
			else:
				result = os.path.exists(r)
		
		else:

			if frmt!=None:
				result = os.path.isdir(os.path.dirname(r)) and r.endswith(frmt)
			else:
				result = os.path.isdir(os.path.dirname(r))

		return result

	return checker

def dirCondition(exist, default, qletter, dletter):
	'''return checker defining if result DirPath is valid'''

	def checker(r):
		'''TODO: should rise error with explanation'''
		r = r.strip()

		if r == qletter:
			return True

		# check/use default option
		if default and r==dletter:
			print 'Default option chosen:\n', default
			r = default

		if exist:
			result = os.path.exists(r)
		else:
			result = os.path.isdir(os.path.dirname(r))
				
		return result

	return checker



def bcond(yletter,nletter,qletter, dletter, default):
	'''boolean conditioning'''

	def checker(r):
		if default!=None:
			opts = ( yletter, nletter, qletter, dletter)
		else:
			opts = ( yletter, nletter,qletter)

		return r in opts

	return checker



def	intCondition(custom_condition, qletter, dletter, default):
	'''integer conditioner'''
	# TODO: add few custom int condition helpers
	
	def checker(r):
		if r==qletter:
			return True

		elif default!=None and  r == dletter:
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


def floatCondition(custom_condition, qletter, dletter, default):
	'''range conditioner'''
	
	def checker(r):
		if r==qletter:
			return True

		elif default!=None and  r == dletter:
			result = True
			

		else:
			try:
				x = float(r)
				result = True
			except:
				result = False

		if custom_condition:
			return result and custom_condition(r)
		else:
			return result

	return checker

# TODO: add few custom float condition helpers

