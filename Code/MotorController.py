#//location of python 3
# File name:	MotorController.py
# Description:	To test Motor Controll theory
# Author:		Taylor Brady
# Date:			3/2/2020
# Code from *adeept/Adeept_RaspTank/blob/master/server/move.py* referenced
import time
import RPi.GPIO as GPIO

#Motor A? 4 or 7?
Rt_Motor = 4
#Rt_Motor = 7

#could be switched OR could be 8,10
Rt_Motor_R = 14
Rt_Motor_F = 15	

pwm_A = 0
pwm_B = 0


def setup():
    
    
    global pwm_A, pwm_B
    
    #disables warnings when pins are defined in multiple scripts
    #GPIO.setwarnings(False)
    
    #Broadcom SOC
    #change to BOARD??
    GPIO.setmode(GPIO.BCM)
    
    #define pin mode
    GPIO.setup(Rt_Motor, GPIO.OUT)
    GPIO.setup(Rt_Motor_F, GPIO.OUT)
    GPIO.setup(Rt_Motor_R, GPIO.OUT)
    
    
    #motorstop()
    GPIO.output(Rt_Motor, GPIO.LOW)
    GPIO.output(Rt_Motor_F, GPIO.LOW)
    GPIO.output(Rt_Motor_R, GPIO.LOW)
    #end motorstop()
    
    #error check
    try:
        pwm_A = GPIO.PWM(Rt_Motor, 1000)
    except:
        pass
        
def motor_right(status, dir, speed):
    if status == 0:
        GPIO.output(Rt_Motor, GPIO.LOW)
        GPIO.output(Rt_Motor_F, GPIO.LOW)
        GPIO.output(Rt_Motor_R, GPIO.LOW)
    else:
        if dir == 0:
            GPIO.output(Rt_Motor_F, GPIO.LOW)
            GPIO.output(Rt_Motor_R,GPIO.HIGH)
            pwm_B.start(0)
            pwm_B.ChangeDutyCycle(speed)
        elif dir == 1:
            GPIO.output(Rt_Motor_R, GPIO.LOW)
            GPIO.output(Rt_Motor_F,GPIO.HIGH)
            pwm_B.start(0)
            pwm_B.ChangeDutyCycle(speed)



def destroy():
    #motorstop()
    GPIO.output(Rt_Motor, GPIO.LOW)
    GPIO.output(Rt_Motor_F, GPIO.LOW)
    GPIO.output(Rt_Motor_R, GPIO.LOW)
    #end motorstop()
    
    GPIO.cleanup()
    
if __name__ == '__main__':
    try:
        setup()
        motor_right(1, 0, 6)
        time.sleep(500)
        motor_right(1, 1, 6)
        time.sleep(500)
        motor_right(0,1,1)
    except KeyboardInterrupt:
        destroy()
        