from gluon.contenttype import contenttype
import StringIO

def index():
    return dict()

def upload():
    f = request.vars.myfile.file
    response.headers['Content-Type'] = contenttype('*.xls')
    response.headers['Content-disposition'] = 'attachment;filename=%s_converted.xls' % (request.now)
    
    return response.stream(f, chunk_size = 64 * 1024)
