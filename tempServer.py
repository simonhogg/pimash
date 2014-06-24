from flask import Flask, render_template, jsonify, request
from pimashio import PimashIO
app = Flask(__name__)

setpoint = 80.0
element = False
io = PimashIO()

@app.route("/")
def index():
    tempdata = get_tempdata()
    return render_template('main.html', **tempdata)

@app.route('/_refresh')
def refresh():
    return jsonify(get_tempdata())

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
        'element' : e
        }
    return tempdata

@app.route('/_updateSetPoint/<sp>')
def update_setpoint(sp):
    global setpoint
    setpoint = float(sp)
    print(repr(setpoint))
    return sp

if __name__ == "__main__":
    app.run(host='10.0.1.33', port=80, debug=True)
