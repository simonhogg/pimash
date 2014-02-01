from flask import Flask, render_template
import simpleTemp
app = Flask(__name__)

@app.route("/")
def hello():
	tempData = {
		'temp' : repr(simpleTemp.getTemp())
	}
	return render_template('main.html', **tempData)

if __name__ == "__main__":
	app.run(host='10.0.1.33', port=80, debug=True)
