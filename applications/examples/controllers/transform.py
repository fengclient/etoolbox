from gluon.contenttype import contenttype
from StringIO import StringIO
#from freemind import FreeMindMap

def index():
    return dict()

def upload():
    f = request.vars.myfile.file
    response.headers['Content-Type'] = contenttype('*.xls')
    response.headers['Content-disposition'] = 'attachment;filename=%s_converted.xls' % (request.now)
    w=StringIO()
    a = FreeMindMap(f)
    a.save_excel(w)
    w.seek(0)
    return response.stream(w, chunk_size = 64 * 1024)
