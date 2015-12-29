
from language import Language

class cpp(Language):
    comment = '//'
    ext = ['h', 'cpp']
    def __init__(self) :
       pass
    def write(self, name) :
       print self.comment
    def write_class(self) :
       pass
    def write_main(self) :
       pass

    class Factory:
       def create(self): return cpp()


