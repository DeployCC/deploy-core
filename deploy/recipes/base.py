#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Deploy for Humans
	_________________
	
	Is the base recipe for cook you code.
	
	:copyright: (c) 2012 by Jair Gaxiola 
	:license: GPLv3
"""
import requests
import os

from deploy.cook.build import PreCompile, Source, Configure, Make, MakeInstall, PostCompile

class Recipe():
	
	def preCompile(self, precompile):
	    self.r = PreCompile(precompile)
	    
	def source(self, url, info):
		self.r = Source()
		self.r.get(url, info)

	def configure(self, flags = {}, options = {}, with_value = {},  without_value = {}, enable = {}, disable = {}):
		self.r = Configure()
		self.r.to_compile(flags, options, with_value, without_value, enable, disable)
	
	def make(self):
		self.r = Make()
	
	def makeInstall(self):
		self.r = MakeInstall()
	
	def postCompile(self, postcompile):
	    self.r = PostCompile(postcompile)

if __name__ == "__main__":
	r = BaseRecipe()
	r.prepare()