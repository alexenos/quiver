
from language import *

class python(Language):
   def __init__(self) :
      self.impl = python_impl()
   def define(self, args) :
      self.impl.define(args)
   def write(self, name, type) :
       self.impl.write(name, type)
   class Factory:
      def create(self): return python()

class python_syntax() :
   comment = '#'

class python_impl(File) :
   def __init__(self) :
      self.name = 'name'
      self.syntax = python_syntax()
      self.ext = 'py'
      self.writing = {'class' : self.write_class,
                      'main'  : self.write_main  }
   def define(self, args) :
      pass
   def write(self, name, type) :
      self.name = name
      fo = self.open(name)
      self.writing[type](fo)
      self.close(fo)
   def write_main(self, fo) :
      fo.write("#!/usr/bin/python\n")
      fo.write("\n")
      fo.write("import sys\n")
      fo.write("\n")
      fo.write("def main() :\n")
      fo.write("   return 0\n")
      fo.write("\n")
      fo.write("if __name__ == '__main__' :\n")
      fo.write("   sys.exit(main())\n")
   def write_class(self, fo) :
      fo.write("#!/usr/bin/python")
      fo.write("")
      fo.write("class " + self.name + " :")
      fo.write("   pass")

