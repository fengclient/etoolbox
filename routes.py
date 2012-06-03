#!/usr/bin/python
# -*- coding: utf-8 -*-

routes_in = (
  ('/convert', '/shorturl/default/convert'),
  ('/reset','/shorturl/default/reset'),
  ('/$id','/shorturl/default/get?id=$id')
)

routes_out = [(x, y) for (y, x) in routes_in]