from gluon.dal import DAL,Field
db = DAL('sqlite://s_com.s_com')
db.define_table('orig_to_short',
                Field('id','id'),
                Field('originalurl','string'),
                Field('shorturl','string'))