#!/usr/bin/python

import language_factory

class Tabula :
   def __init__(self) :
      self.name = 'test'
      self.language = language_factory.get("python")
   def __init__(self, args) :
      self.name = args.name
      self.language = language_factory.get(args.language)
   def write(self) :
      self.language.write(self.name)

# module api
def create(args=None) :
   return Tabula(args)
