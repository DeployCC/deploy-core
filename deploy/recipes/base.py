#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Deploy for Humans
	_________________
	
	This recipe will prepare nginx from source.
	
	:copyright: (c) 2012 by Jair Gaxiola 
	:license: GPLv3
"""
import requests
import os

from deploy.cook.build import Source, Configure, Make, MakeInstall

class Recipe():
	
	def source(self, url, info):
		self.r = Source()
		self.r.get(url, info)

	def configure(self, options = {}, with_value = {},  without_value = {}, enable = {}, disable = {}):
		self.r = Configure()
		self.r.to_compile(options, with_value, without_value, enable, disable)
	
	def make(self):
		self.r = Make()
	
	def makeInstall(self):
		self.r = MakeInstall()

if __name__ == "__main__":
	r = BaseRecipe()
	r.prepare()