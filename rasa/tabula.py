#!/usr/bin/python

import language_factory

class Tabula :
   def __init__(self) :
      self.name = 'test'
      self.name = 'class'
      self.language = language_factory.get("python")
   def __init__(self, args) :
      self.name = args.name
      self.define(args)
      self.language = language_factory.get(args.language)
      self.language.define(args)
   def define(self, args) :
      if args.main :
         self.type = 'main'
      else :
         self.type = 'class'
   def write(self) :
      self.language.write(self.name, self.type)

# module api
def create(args=None) :
   return Tabula(args)
