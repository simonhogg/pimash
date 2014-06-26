import tornado.ioloop
import tornado.webbrowser

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, world")

application = tornado.web.Application([
	(r"/", MainHandler)
	])

if __name == "__main__":
	application.listen(80)
	tornado.ioloop.IOLoop.instance().start()