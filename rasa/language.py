
class Language(object): pass

class File(object) :
   ext = '.txt'
   def open(self, name) :
      return open(name + '.' + self.ext, 'w')
   def close(self, fo) :
      fo.close()
