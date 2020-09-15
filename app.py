#code taken from traffic light python tutorial on raspberrypi.org
#flask code was taken from tutorialspoint.com/flask/flask_quick_guide.html
from flask import Flask, render_template
from gpiozero import LED
from time import sleep
import threading 

red = LED(17)
yellow = LED(27)
green = LED(22) 

app = Flask(__name__)

global temp
temp = False

@app.route('/')
def index():
    temp = False
    return render_template('index.html') 

@app.route('/red', methods=['POST'])
def redLight():
    temp = False
    green.off()
    yellow.off()
    red.off()
    red.blink()
    #return render_template('index.html') 
    return ('',204)   

@app.route('/yellow', methods=['POST'])
def yellowLight():
    temp = False
    green.off()
    yellow.off()
    red.off()
    yellow.blink()
    #return render_template('index.html') 
    return ('',204)   

@app.route('/green', methods=['POST'])
def greenLight():
    temp = False
    red.off()
    yellow.off()
    green.off()
    green.blink()
    #return render_template('index.html') 
    return ('',204)   

@app.route('/cycle', methods=['POST'])
def run():
     green.off()
     yellow.off()
     red.off()
     temp = True
     while temp:
         if temp == False:
             break
         else: 
            green.on()
            sleep(10)
            green.off()
            yellow.on()
            sleep(3)
            yellow.off()
            red.on()
            sleep(10)
            red.off()
   # thread = threading.Thread(target=run) 
   # thread.start()
     return ('',204)   
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
