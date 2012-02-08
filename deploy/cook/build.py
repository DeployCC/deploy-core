#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Deploy for Humans
	_________________
	
	Build the source.
	
	:copyright: (c) 2012 by Jair Gaxiola 
	:license: GPL 2
"""

import requests
import os

from deploy.env import globals
			
class Source():	

	
	def get(self, url, info):	

		filename = "%(name)s-%(version)s" % info
		filepath = "%(path)s" % globals
		tar = filename + '.tar.gz'
		source = requests.get(url % info)
		filesource = open(filepath + tar, 'w')
		filesource.write(source.content)
		filesource.close()
		os.system("cd " + filepath + "; tar -zxvf " + tar)
		
		globals['source'] = "cd " + filepath + filename + ";"

class Configure():
	
	def to_compile(self, options = {}, with_value = {}, without_value = {}, enable = {}, disable = {}):
		compile = './configure'
		print options
		for k, v in options.items():
			compile += ' --' + k + '=' + v
		
		for k, v in with_value.items():
			compile += ' --with-' + k + '=' + v

		for k, v in without_value.items():
			compile += ' --with-' + k

		for k, v in enable.items():
			compile += ' --enable-' + k

		for k, v in disable.items():
			compile += ' --disable-' + k
		
		os.system(globals['source'] + compile)

class Make(object):
	
	def __init__(self):
		os.system(globals['source'] + "make")
		
class MakeInstall(object):

	def __init__(self):
		os.system(globals['source'] + "make install")