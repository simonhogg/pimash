import tornado.ioloop
import tornado.web
from flask import jsonify

from pimashio import PimashIO

# Variables

setpoint = 80.0
element = False
io = PimashIO()

# App Logic

def get_tempdata():
    try:
        # get the current temperature
        t = io.get_temp()
        # check if we need to turn the element or not
        if t > setpoint:
            io.element_off()
            e = 'Off'
        else:
            io.element_on()
            e = 'On'
        # create the tempdata packet
        tempdata = {'temp' :  '%.1f' % t,
            'setpoint' : '%.1f' % setpoint,
            'element' : e
            }
        print(tempdata)
    except:
        print("Error getting temperature data")
        tempdata = {'temp' :  '%.1f' % 0,
        'setpoint' : '%.1f' % setpoint,
        'element' : 'Error'
        }
    return tempdata

# Server Code
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("Hello, world")

class RefreshHandler(tornado.web.RequestHandler):
	def get(self):
		self.write(jsonify(get_tempdata()))

application = tornado.web.Application([
	(r"/", MainHandler),
	(r"/_refresh", RefreshHandler)
	], debug=True)

if __name__ == "__main__":
	application.listen(80)
	tornado.ioloop.IOLoop.instance().start()
