# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
# 短网址
#########################################################################

def get():
    '''
    get original url by id
    '''
    if hasattr(request,'vars') and 'id' in request.vars:
        row=db(db.orig_to_short.id==request.vars.id).select(db.orig_to_short.originalurl).first()
        if row:
            redirect(row.originalurl)

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    return dict(message=T("Hello World, I'm in."))

def convert():
    '''
    convert an external url to a short one with s.com
    '''
#    return dict(message=db().select(db.orig_to_short.ALL),
#                orig=request.vars['orig'] if hasattr(request,'vars') and 'orig' in request.vars else None)
    # create a short url
    from gluon.dal import Row
    if hasattr(request,'vars') and 'orig' in request.vars:
        row=Row()
        row.originalurl=request.vars.orig
        id=db.orig_to_short.insert(**row)
        return 'http://s.com/'+str(id) 
    else:
        return dict(message='"orig" is missing? try this: "http://s.com/welcome/default/convert?orig=www.baidu.com"')
    