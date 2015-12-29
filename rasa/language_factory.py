
from python_lang import python
from cpp_lang import cpp

class LanguageFactory:
    factories = {}
    def getLanguage(id):
        if not LanguageFactory.factories.has_key(id):
            LanguageFactory.factories[id] = \
              eval(id + '.Factory()')
        return LanguageFactory.factories[id].create()
    getLanguage = staticmethod(getLanguage)


def get(id) :
   return LanguageFactory.getLanguage(id)
