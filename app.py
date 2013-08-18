import tornado.ioloop
import tornado.web
import os
from tornado import template
from handle import radio

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader=template.Loader("www")
        self.write(loader.load("index.html").generate())

class RadioONHandler(tornado.web.RequestHandler):
    def post(self):
        radio.radioON()

class RadioOFFHandler(tornado.web.RequestHandler):
    def post(self):
        radio.radioOFF()

class RadioHandler(tornado.web.RequestHandler):
    def post(self):
        message = self.get_argument("volume", None)
        vol=message+'%'
	#print message
	print vol
        radio.volumeSet(vol)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/radio-on",RadioONHandler),
        (r"/radio-off",RadioOFFHandler),
        (r"/radio",RadioHandler),
    ])
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

