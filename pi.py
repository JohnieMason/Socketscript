import socket
import RPi.GPIO as GPIO
import time
#setting the BCM GPIO Numbering
GPIO.setmode(GPIO.BCM)
#Setting the PWM Pin as pin 18
Servo_Pin=18
Solenoid_Pin=24

#setting the servo_pin as the output
GPIO.setup(Servo_Pin, GPIO.OUT)
GPIO.setup(Solenoid_Pin, GPIO.OUT)
#Setting the PWM frequency from 20ms period
pwm=GPIO.PWM(Servo_Pin, 50)
pwm.start(2.0)

def set_servo_angle(angle):
    #Door to open to an angle of 105 degrees
    #Duty Cycle=(angle/18)+2.0
    #OPENING THE DOOR TO 105 degrees
    #Duty cycle=(105/18)+2.0=7.8
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(Servo_Pin, False)
    pwm.ChangeDutyCycle(0)

def processAction(gesture):
    if gesture=="du":
        print("Door Opening")
        pwm.ChangeDutyCycle(7.8)
    elif gesture=="ud":
        print("Door Closing")
        pwm.ChangeDutyCycle(0)


#creating the socket
soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("192.168.137.1", 12345)) # connecting to the server
soc.settimeout(1) #set timeout into 1 second
ful="" #Holds the data we receive
while True:
    try:
        mystr=soc.recv(1).decode() #Receiving 1 byte otherwise timeout
        if len(mystr)==0:
            break #Socet has disconnected,so exit
        if mystr=="\n": #end of received messsage
            print(ful)
            processAction(ful)
            ful="" #Reset the message
            continue #ignore next lines
        ful+=mystr #Add received byte to full message
    except socket.timeout:
        pass #ignore timeout
