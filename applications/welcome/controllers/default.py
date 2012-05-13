# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
# 短网址
#########################################################################

def get():
    '''
    get original url by id
    '''
    if request.vars.id:
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
    # create a short url
    from gluon.dal import Row
    if request.vars.orig:
        row = db(db.orig_to_short.originalurl == request.vars.orig).select(db.orig_to_short.id).first()
        if not row:
            row=Row(originalurl=request.vars.orig)
            id=db.orig_to_short.insert(**row)
        else:
            id=row.id
        return 'http://s.com/'+str(id)
    else:
        return dict(message='"orig" is missing? try this: "http://s.com/welcome/default/convert?orig=www.baidu.com"')

def reset():
    '''
    clean up records in database
    '''
    count=db(db.orig_to_short.id>=0).delete()
    return count
