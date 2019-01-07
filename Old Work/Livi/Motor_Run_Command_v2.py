#!/usr/bin/python
from __future__ import division
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import time
import atexit
import os
import time
import tk_tools
from tkinter import *


mh = Adafruit_MotorHAT(addr=0x60)

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myMotor = mh.getMotor(1)
myMotor.run(Adafruit_MotorHAT.FORWARD)

master = Tk();
master.title("Raspberry Pi Motor Control Gui");
EntryBox1 = 0;
EntryBox2 = 0;
EntryBox3 = 0;
EntryBox4 = 0;
EntryBox5 = 0;
EntrySlider1 = 0;
speed = 0;
gauge = 0;

def increase_speed_entrybox():
    global EntryBox1;
    global master;
    label = Label(master, text="Increase Speed");
    label.grid(row=1,column=1, sticky=W);
    EntryBox1 = Entry(master);
    EntryBox1.grid(row=2, column=1);
    button = Button(master,text="Ok",command=increase_speed);
    button.grid(row=3,column =1);

def increase_speed():
    global EntryBox1;
    global speed;
    global master;
    global guage;
    val = EntryBox1.get();
    if int(val)+speed < 0 or int(val)+speed > 255:
        print("error: Speed must be GREATER than 1 and LESS THAN 255");
        print("current speed: " + str(speed));
    else:
        speed += int(val);
        gauge.set_value(int(speed));
        myMotor.run(Adafruit_MotorHAT.FORWARD);
        myMotor.setSpeed(int(speed));
        print(speed);

def decrease_speed_entrybox():
    global EntryBox2;
    global master;
    label = Label(master, text="Decrease Speed");
    label.grid(row=1,column=2, sticky=W);
    EntryBox2 = Entry(master);
    EntryBox2.grid(row=2, column=2);
    button = Button(master,text="Ok",command=decrease_speed);
    button.grid(row=3,column=2);

def decrease_speed():
    global EntryBox2;
    global speed;
    global master;
    global gauge;
    val = EntryBox2.get();
    if speed-int(val) < 0 or speed-int(val) > 255:
        print("error: Speed must be GREATER than 1 and LESS THAN 255");
        print("current speed: " + str(speed));
    else:
        speed -= int(val);
        gauge.set_value(int(speed));
        myMotor.run(Adafruit_MotorHAT.FORWARD);
        myMotor.setSpeed(int(speed));
        print(speed);

def decrease_percentage_speed_entrybox():
        global EntryBox3;
        global master;
        label = Label(master, text="Decrease Speed By Percentage");
        label.grid(row=1,column=4, sticky=W);
        EntryBox3 = Entry(master);
        EntryBox3.grid(row=2, column=4);
        button = Button(master,text="Ok",command=decrease_percentage_speed);
        button.grid(row=3,column=4);

def decrease_percentage_speed():
        global EntryBox3;
        global speed;
        global master;
        global gauge;
        percent = EntryBox3.get();
        if speed-(speed*(int(percent)/100)) < 0 or speed-(speed*(int(percent)/100)) > 255:
            print("error: Speed must be GREATER than 1 and LESS THAN 255");
            print("current speed: " + str(speed));
        else:
            speed = speed-(speed*(int(percent)/100));
            gauge.set_value(int(speed));
            myMotor.run(Adafruit_MotorHAT.FORWARD);
            myMotor.setSpeed(int(speed));
            print(speed);

def increase_percentage_speed_entrybox():
        global EntryBox4;
        global master;
        label = Label(master, text="Increase Speed By Percentage");
        label.grid(row=1,column=3, sticky=W);
        EntryBox4 = Entry(master);
        EntryBox4.grid(row=2, column=3);
        button = Button(master,text="Ok",command=increase_percentage_speed);
        button.grid(row=3,column=3);

def increase_percentage_speed():
        global EntryBox4;
        global speed;
        global master;
        global gauge;
        percent = EntryBox4.get();
        if speed+(speed*(int(percent)/100)) < 0 or speed+(speed*(int(percent)/100)) > 255:
            print("error: Speed must be GREATER than 1 and LESS THAN 255");
            print("current speed: " + str(speed));
        else:
            speed = speed+(speed*(int(percent)/100));
            gauge.set_value(int(speed));
            myMotor.run(Adafruit_MotorHAT.FORWARD);
            myMotor.setSpeed(int(speed));
            print(speed);

def set_speed_entrybox():
        global EntryBox5;
        global master;
        label = Label(master, text="Set Speed");
        label.grid(row=5,column=4, sticky=W);
        EntryBox5 = Entry(master);
        EntryBox5.grid(row=6, column=4);
        button = Button(master,text="Ok",command=set_speed);
        button.grid(row=7,column=4);

def set_speed():
        global EntryBox5;
        global speed;
        global master;
        global gauge;
        val = EntryBox5.get();
        if int(val) < 0 or int(val) > 255:
            print("error: Speed must be GREATER than 1 and LESS THAN 255");
            print("current speed: " + str(speed));
        else:
            speed = int(val);
            gauge.set_value(int(speed));
            myMotor.run(Adafruit_MotorHAT.FORWARD);
            myMotor.setSpeed(int(speed));
            print(speed);

def set_speed_entryslider():
        global EntrySlider1;
        global master;
        label = Label(master, text="Set Speed By Slider");
        label.grid(row=5,column=3, sticky=W);
        EntrySlider1 = Scale(from_=0, to=255, resolution=1, orient=HORIZONTAL, sliderlength = 90);
        EntrySlider1.grid(row=6, column=3,sticky= E + W);
        button = Button(master,text="Ok",command=set_speed_slider);
        button.grid(row=7,column=3);

def set_speed_slider():
        global EntrySlider1;
        global speed;
        global master;
        global gauge;
        val = EntrySlider1.get();
        if int(val) < 0 or int(val) > 255:
            print("error: Speed must be GREATER than 1 and LESS THAN 255");
            print("current speed: " + str(speed));
        else:
            speed = int(val);
            gauge.set_value(int(speed));
            myMotor.run(Adafruit_MotorHAT.FORWARD);
            myMotor.setSpeed(int(speed));
            print(speed);
            
    
increase_speed_entrybox();
decrease_speed_entrybox();
decrease_percentage_speed_entrybox();
increase_percentage_speed_entrybox();
set_speed_entryslider();
set_speed_entrybox();
gauge = tk_tools.Gauge(master, max_value=255.0,
                       label='speed', unit=' rmp/sec')
gauge.grid(row=8,column=1)
gauge.set_value(0)
mainloop();

