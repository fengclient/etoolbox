from gluon.dal import DAL,Field
db = DAL('mysql://test:123456@localhost:3306/s_com')
db.define_table('orig_to_short',
                Field('id','id'),
                Field('originalurl','string'),
                Field('shorturl','string'),
                migrate=False)