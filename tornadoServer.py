import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.template

import random
import os.path

from pimashio import PimashIO

# Variables


g = dict(
    temperature = 72.0
    setpoint = 80.0
    element_status = '~'
    )

io = PimashIO()

# App Logic

def check_temp():
    global g
    try:
        # get the current temperature
        g.temperature = io.get_temp()
        # check if we need to turn the element or not
        if temp > setpoint:
            io.element_off()
            g.element_status = 'Off'
        else:
            io.element_on()
            g.element_status = 'On'
    except:
        g.temperature = random.randint(72,212)+0.1
        g.element_status = "Error"
        
        

def get_tempdata():
    global g
    # create the tempdata packet
    tempdata = {'temp' :  '%.1f' % g.temperature,
        'setpoint' : '%.1f' % g.setpoint,
        'element' : g.element_status
        }
    print(tempdata)
    return tempdata

# Server Code
class MainHandler(tornado.web.RequestHandler):
    global g
    def get(self):
        global g
       #self.render('main.html', temp=temp, setpoint=setpoint, element=element)
       self.render('ngindex.html', temp=g.temperature, setpoint=g.setpoint, element=g.element_status)

class RefreshHandler(tornado.web.RequestHandler):
    def get(self):
        #self.write(tornado.escape.json_encode(get_tempdata()))
        self.write(get_tempdata())

class UpdateSetpointHandler(tornado.web.RequestHandler):
    def get(self, sp):
        global setpoint
        setpoint = float(sp)
        self.finish()

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
) 

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/_refresh', RefreshHandler),
    (r'/_temperature', RefreshHandler),
    (r"/_updateSetPoint/([0-9]+)", UpdateSetpointHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': './static'})
    ], **settings)

if __name__ == "__main__":
    application.listen(80)
    main_loop = tornado.ioloop.IOLoop.instance()
    # Create a periodic timer for our control loop
    scheduler = tornado.ioloop.PeriodicCallback(check_temp, 1000, io_loop = main_loop)
    # Start the timer and then the IOloop
    scheduler.start()
    main_loop.start()
