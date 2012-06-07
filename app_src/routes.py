#!/usr/bin/python
# -*- coding: utf-8 -*-

default_application = 'shorturl'    # ordinarily set in base routes.py
default_controller = 'default'  # ordinarily set in app-specific routes.py
default_function = 'convert'      # ordinarily set in app-specific routes.py

routes_in = (
  ('/convert', '/shorturl/default/convert'),
  ('/reset','/shorturl/default/reset'),
  ('/$id','/shorturl/default/get?id=$id')
)

routes_out = [(x, y) for (y, x) in routes_in]