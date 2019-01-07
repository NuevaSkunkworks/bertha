#!/usr/bin/python
from __future__ import division
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import os
import time


mh = Adafruit_MotorHAT(addr=0x60)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor = mh.getMotor(1)
val = 0;



while(True):
    os.system('clear')
    di = raw_input(bcolors.OKGREEN + bcolors.BOLD + "Decrease (d), increase (i), increase by percentage (ibp), decrease by percentage(dbp), or set value? (sv): " + bcolors.END);
    print("")
    print(bcolors.HEADER + "Command: " + bcolors.END + di);
    myMotor.run(Adafruit_MotorHAT.FORWARD)
    
    if di == "d":
        print(bcolors.HEADER + "Current Speed: " + bcolors.END + str(val))
        inputval = input(bcolors.HEADER + "Decrease by: " + bcolors.END)
        if val-inputval < 1 or val-inputval > 255:
            print(bcolors.WARNING + "error: Speed must be GREATER than 0 and LESS than 255" + bcolors.END)
            print(bcolors.FAIL + "Speed: " + str(val-inputval) + bcolors.END)
            time.sleep(3)
            continue
        val -= inputval;
        myMotor.setSpeed(int(val));
        print(bcolors.HEADER + "Speed: " + bcolors.END + str(val))
        time.sleep(3);
        
    elif di == "i":
        print(bcolors.HEADER + "Current Speed: " + bcolors.END + str(val))
        inputval = input(bcolors.HEADER + "Increase by: " + bcolors.END)
        if val+inputval > 255 or val+inputval < 0:
            print(bcolors.WARNING + "error: Speed must be GREATER than 0 and LESS than 255" + bcolors.END)
            print(bcolors.FAIL + "Speed: " + str(val+inputval) + bcolors.END)
            time.sleep(3)
            continue
        val += inputval;
        myMotor.setSpeed(int(val));
        print(bcolors.HEADER + "Speed: " + bcolors.END + str(val))
        time.sleep(3);
        
    elif di == "sv":
        val = input(bcolors.HEADER + "1 - 255: " + bcolors.END);
        if val > 255 or val < 0:
            print(bcolors.WARNING + "error: Value must be GREATER than 0 and LESS than 255" + bcolors.END)
            time.sleep(3)
            continue
        myMotor.setSpeed(val);
        print(bcolors.HEADER + "Speed: " + bcolors.END + str(val))
        time.sleep(3);
    
    elif di == "dbp":
        percentage = input(bcolors.HEADER + "Enter Percentage(1-100%): " + bcolors.END)
        if percentage > 100 or percentage < 0 or percentage % 1 != 0:
            print(bcolors.WARNING + "error: Value must be GREATER than 1, LESS than 100, and a WHOLE number" + bcolors.END)
            time.sleep(3)
            continue
        print(bcolors.HEADER + "Percent in Decimals: " + bcolors.END + str(percentage/100))
        val = val*(percentage/100)
        myMotor.setSpeed(int(val));
        print(bcolors.OKGREEN + "Speed: " + bcolors.END + str(val));
        time.sleep(3);
        
    elif di == "ibp":
        percentage = input(bcolors.HEADER + "Enter Percentage(1-100%): " + bcolors.END)
        if percentage > 100 or percentage < 0 or percentage % 1 != 0:
            print(bcolors.WARNING + "error: Value must be GREATER than 1, LESS than 100, and a WHOLE number" + bcolors.END)
            time.sleep(3)
            continue
        print(bcolors.HEADER + "Percent in Decimals: " + bcolors.END + str(percentage/100))
        val = val + (val*(percentage/100))
        myMotor.setSpeed(int(val));
        print(bcolors.OKGREEN + "Speed: " + bcolors.END + str(val));
        time.sleep(3);




