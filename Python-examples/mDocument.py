#!/usr/bin/env python
# -*- coding: utf-8 -*-

def create ( ) :
    """Create new Document"""
    return Document( status = Document.New )
    
def load ( id ) :
    """Load document from database"""
    Doc = Document( id = id )
    Doc.restore()
    return Doc

class Document ( object ) :

    New = 1
    Status_Allowed = [ New ]

    def __init__( self, **kwargs ) :
        if "id" in kwargs :
            self.__Id = int( kwargs["id"] )
        if "status" in kwargs :
            if kwargs["status"] not in Document.Status_Allowed :
                raise ValueError
            self.__Status = kwargs["status"]
    
    id = property( lambda self : self.__Id )
    
    @property
    def status ( self ) :
        return self.__Status
        
    def save( self ) :
        pass
        
    def restore( self ) :
        pass

if __name__ == "__main__" :
    D = create()
    print u"Status = ", D.status
    try :
        print u"ID     = ", D.id
    except AttributeError :
        print u"<NONE>"
        
    D = load( id=1 )
    try :
        print u"Status = ", D.status
    except AttributeError :
        print u"<NONE>"
    try :
        print u"ID     = ", D.id
    except AttributeError :
        print u"<NONE>"

    D = load( id = u"123" )
    try :
        print u"Status = ", D.status
    except AttributeError :
        print u"<NONE>"
    try :
        print u"ID     = ", D.id
    except AttributeError :
        print u"<NONE>"
        