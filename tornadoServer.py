import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.template

import os.path

from pimashio import PimashIO

# Variables
temp = 72.0
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
		self.render('main.html', temp=temp, setpoint=setpoint, element=element)

class RefreshHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write(tornado.escape.json_encode(get_tempdata()))
		self.write(get_tempdata())

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
) 

application = tornado.web.Application([
	(r'/', MainHandler),
	(r'/_refresh', RefreshHandler),
	(r'/static/(.*)', tornado.web.StaticFileHandler, {'path': './static'})
	], **settings)

if __name__ == "__main__":
	application.listen(80)
	tornado.ioloop.IOLoop.instance().start()
