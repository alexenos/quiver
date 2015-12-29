
from language import *

class python(Language):
   def __init__(self) :
      self.impl = python_impl()
   def write(self, name) :
       self.impl.write(name)
   class Factory:
      def create(self): return python()

class python_syntax() :
   comment = '#'

class python_impl(File) :
   def __init__(self) :
      self.syntax = python_syntax()
      self.ext = 'py'
      self.type = 'class'
      self.writing = {'class' : self.write_class,
                      'main'  : self.write_main  }
   def write(self, name) :
      fo = self.open(name)
      self.writing[self.type](fo)
      self.close(fo)
   def write_main(self, fo) :
      fo.write('testing')
   def write_class(self, fo) :
      fo.write('testing')

