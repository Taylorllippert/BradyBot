#!/usr/bin/env python3.8
# File name:	Tester.py
# Description:	To test input to output 
# Author:		Taylor Brady
# Date:			3/2/2020
# Code from *adeept/Adeept_RaspTank/blob/master/* referenced

import time
#import RPi.GPIO as GPIO

   
        
def SinglePinTest():
    print("Starting Single Pin Test")
	#request pin to test from user
		pin=input("enter pin")
	
	#set pin high
		#GPIO.output(pin, GPIO.HIGH)

	#wait for user to acknowledge and/timer
		temp=input("select Enter to continue")
	#set pin low
 		#GPIO.output(pin, GPIO.LOW)
		
   return 0


def testSelector():
    print("      Test Menu     ")
    print("0....End Test")
    print("1....Single Pin Test")
    print("")
    
    x=input()
    x=int(x)
    print(x)
    if x == 0:
        return 0
    elif x == 1:
        return SinglePinTest()
    else:
        print('Invalid Choice')
        return 0
    
def checkPinCap(pin):
    #which numbering is being used? GPIO or board
    #MUST add usable pins 
    #this is NOT complete
    usablePins = [2,3,4,5,6]
    gndPins = [6,9]
    if x in usablePins:
        return true
    if x not in gndPins:
        return true
    
    


if __name__ == '__main__':
    x = testSelector()
    print (x)