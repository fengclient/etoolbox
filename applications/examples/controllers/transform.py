
def index():
    return dict()

def upload():
    data = request.vars.myfile.value
    return 'yes' if data else None
