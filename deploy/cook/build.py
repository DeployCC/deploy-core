#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Deploy for Humans
	_________________
	
	Build the source.
	
	:copyright: (c) 2012 by Jair Gaxiola 
	:license: GPLv3
"""

import os

from deploy.env import globals
from deploy.commands import Tar, Wget
			
class Source():	

	def get(self, url, info):
	    fullname = "%(name)s-%(version)s" % info
	    resource = url % info
	    
	    wget = Wget()
	    wget.download(resource, fullname)
	    tar = Tar()
	    tar.untar(info)
	    
	    globals['source'] = "cd " + globals['store'] + "%(name)s/%(version)s;" % info

class PreCompile(object):
    
    def __init__(self, precompile):
        if precompile:
	        os.system(globals['source'] + precompile)

class Configure():
	
	def to_compile(self, flags = {}, options = {}, with_value = {}, without_value = {}, enable = {}, disable = {}):
	    
		compile = './configure'

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

class PostCompile(object):
    
    def __init__(self, postcompile):
        if postcompile:
	        os.system(globals['source'] + postcompile)