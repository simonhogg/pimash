from flask import Flask
import simpleTemp
app = Flask(__name__)

@app.route("/")
def hello():
	return repr(simpleTemp.getTemp())

if __name__ == "__main__":
	app.run(host='10.0.1.33', port=80, debug=True)
