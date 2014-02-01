from flask import Flask, render_template, jsonify, request
import simpleTemp
app = Flask(__name__)

_setpoint = 155.0

@app.route("/")
def index():
	tempData = {
		'temp' :  '%.1f' % simpleTemp.getTemp()
		'setpoint' : '%.1f' % _setpoint
	}
	return render_template('main.html', **tempData)

@app.route('/_refresh')
def refresh():
	tempData = {
		'temp' :  '%.1f' % simpleTemp.getTemp()
		'setpoint' : '%.1f' % _setpoint
	}
	return jsonify(tempdata)

if __name__ == "__main__":
	app.run(host='10.0.1.33', port=80, debug=True)
