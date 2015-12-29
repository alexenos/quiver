
class Language(object):
   def __init__(self) :
      pass
   def define(self, args) :
      pass
   def write(self, name, type) :
      pass

class File(object) :
   ext = '.txt'
   def open(self, name) :
      return open(name + '.' + self.ext, 'w')
   def close(self, fo) :
      fo.close()
