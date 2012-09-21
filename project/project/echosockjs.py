import sockjs.tornado

class EchoSockjsConnection(sockjs.tornado.SockJSConnection):
    def on_open(self, request):
        print "sockjs: open"

    def on_message(self, data):
        print "data: %r" % (data,)
        self.send(data)

    def on_close(self):
        print "sockjs: close"

def EchoSockjsRouter(prefix):
    return sockjs.tornado.SockJSRouter(EchoSockjsConnection, prefix).urls

