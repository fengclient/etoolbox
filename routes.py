#!/usr/bin/python
# -*- coding: utf-8 -*-

routes_in = (
  ('/convert', '/welcome/default/convert'),
  ('/$id','/welcome/default/get?id=$id')
)

routes_out = [(x, y) for (y, x) in routes_in]