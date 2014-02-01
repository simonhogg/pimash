import RPi.GPIO as GPIO

# Global to define which pin is used as the relay output
OUTPUT_PIN = 2

class PimashIO:

	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		print(OUTPUT_PIN)
		GPIO.setup(OUTPUT_PIN, GPIO.OUT)
		GPIO.output(OUTPUT_PIN, GPIO.LOW)


	def get_temp(self):
	# Open the file that we viewed earlier so that python can see what is in it
		tfile = open("/sys/bus/w1/devices/28-000004a1c1e6/w1_slave")
	# Read all of the text in the file. 
		text = tfile.read() 
	# Close the file now that the text has been read. 
		tfile.close() 
	# Split the text with new lines (\n) and select the second line. 
		secondline = text.split("\n")[1] 
	# Split the line into words, referring to the spaces, and select the 10th word (counting from 0). 
		temperaturedata = secondline.split(" ")[9] 
	# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
		temperature = float(temperaturedata[2:]) 
	# Put the decimal point in the right place and display it. 
		temperature = temperature / 1000
		temperatureF = 9.0/5.0 * temperature + 32 
		return temperatureF


	def element_on(self):
		GPIO.output(OUTPUT_PIN, GPIO.HIGH)

	def element_off(self):
		GPIO.output(OUTPUT_PIN, GPIO.LOW)
