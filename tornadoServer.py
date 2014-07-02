#!/usr/bin/python

import tornado.ioloop
import tornado.web
import tornado.escape
import tornado.template

import random
import os.path

from pimashio import PimashIO
from pimashdb import PimashDB

# Variables

class TempStatus:
    temperature = 72.0,
    setpoint = 80.0,
    element_status = '~',
    logging = True

g = TempStatus()

io = PimashIO()
db = PimashDB()

# App Logic

def check_temp():
    global g
    try:
        # get the current temperature
        g.temperature = io.get_temp()
        # check if we need to turn the element or not
        if g.temperature > g.setpoint:
            print('Temperature over setpoint | %.1f', g.temperature)
            io.element_off()
            g.element_status = 'Off'
        else:
            print('Temperature under setpoint | %.1f', g.temperature)
            io.element_on()
            g.element_status = 'On'
    except:
        print('No HW detected')
        g.temperature = random.randint(72,212)+0.1
        g.element_status = "Error"

def log_temp():
    global g
    if g.logging:
        # attempt to log the temperature
        db.log_temp('brewing', g.temperature)

def get_log():
    return db.get_log()

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
        self.write(get_tempdata())

class LogRefreshHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(get_log())

class UpdateSetpointHandler(tornado.web.RequestHandler):
    def get(self, sp):
        global g
        g.setpoint = float(sp)
        print('Setpoint updated to %.1f' % g.setpoint)
        self.finish()

settings = dict(
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        debug=True
) 

application = tornado.web.Application([
    (r'/', MainHandler),
    (r'/_refresh', RefreshHandler),
    (r'/_temperature', RefreshHandler),
    (r'/_log', LogRefreshHandler),
    (r"/_updateSetPoint/([0-9]+)", UpdateSetpointHandler),
    (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': './static'})
    ], **settings)

if __name__ == "__main__":
    application.listen(80)
    main_loop = tornado.ioloop.IOLoop.instance()
    # Create a periodic timer for our control loop
    temp_scheduler = tornado.ioloop.PeriodicCallback(check_temp, 1000, io_loop = main_loop)
    log_scheduler = tornado.ioloop.PeriodicCallback(log_temp, 10000, io_loop = main_loop)
    # Start the timers and then the IOloop
    temp_scheduler.start()
    log_scheduler.start()
    main_loop.start()
