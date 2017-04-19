#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mDocument

def create () :
    return Nakladnaya( status = mDocument.Document.New )

class Nakladnaya ( mDocument.Document ) :

    def __init__ ( self, **kwargs ) :
        mDocument.Document.__init__( self, **kwargs )
        
    itogo = property( lambda self : self.__Itogo )
        
if __name__ == "__main__" :
    Nakl = create()
    
    try :
        print u"Status = ", Nakl.status
    except AttributeError :
        print u"<NONE>"
    try :
        print u"ID     = ", Nakl.id
    except AttributeError :
        print u"<NONE>"
