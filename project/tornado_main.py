#!/usr/bin/env python

from tornado.options import options, define
import django.core.handlers.wsgi
import tornado.httpserver, tornado.ioloop
import tornado.web, tornado.wsgi
import project.echosockjs

define('port', type=int, default=8000)

wsgi_app = tornado.wsgi.WSGIContainer(
               django.core.handlers.wsgi.WSGIHandler())

tornado_app = tornado.web.Application(
    project.echosockjs.EchoSockjsRouter('/echo') + [
        ('.*', tornado.web.FallbackHandler,
               dict(fallback=wsgi_app)),
    ])
server = tornado.httpserver.HTTPServer(tornado_app)
server.listen(options.port)
print "[*] Listening at 0.0.0.0:%i" % (options.port,)
tornado.ioloop.IOLoop.instance().start()

