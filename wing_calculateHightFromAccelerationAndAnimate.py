from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pandas as pd
import os
import math
import ffmpeg


color_s = ['b','g','r','c','m','y']
line_s = ['-', '--', '-.', ':']
marker_s = ['.',',','1','2','3','4']

Tk().withdraw()
path = askopenfilename()
filename = os.path.basename(path)
print(filename)
csvFile = pd.read_csv(filename)

calibrationFile = pd.read_csv("GyroCalibration.csv")


imus = 8

x1 = 0
x2 = 90
x3 = 180
x4 = 270
x5 = 360
x6 = 450
x7 = 540
x8 = 630

time = csvFile['T']


if imus >= 1:
    ax1 = csvFile['AX1']
    ay1 = csvFile['AY1']
    az1 = csvFile['AZ1']
    p1Offset = calibrationFile['P0']
    r1Offset = calibrationFile['R0']
    p1 = []
    r1 = []
if imus >= 2:
    ax2 = csvFile['AX2']
    ay2 = csvFile['AY2']
    az2 = csvFile['AZ2']
    p2Offset = calibrationFile['P1']
    r2Offset = calibrationFile['R1']
    p2 = []
    r2 = []
    h2 = []
if imus >= 3:
    ax3 = csvFile['AX3']
    ay3 = csvFile['AY3']
    az3 = csvFile['AZ3']
    p3Offset = calibrationFile['P2']
    r3Offset = calibrationFile['R2']
    p3 = []
    r3 = []
    h3 = []
if imus >= 4:
    ax4 = csvFile['AX4']
    ay4 = csvFile['AY4']
    az4 = csvFile['AZ4']
    p4Offset = calibrationFile['P3']
    r4Offset = calibrationFile['R3']
    p4 = []
    r4 = []
    h4 = []
if imus >= 5:
    ax5 = csvFile['AX5']
    ay5 = csvFile['AY5']
    az5 = csvFile['AZ5']
    p5Offset = calibrationFile['P4']
    r5Offset = calibrationFile['R4']
    p5 = []
    r5 = []
    h5 = []
if imus >= 6:
    ax6 = csvFile['AX6']
    ay6 = csvFile['AY6']
    az6 = csvFile['AZ6']
    p6Offset = calibrationFile['P5']
    r6Offset = calibrationFile['R5']
    p6 = []
    r6 = []
    h6 = []
if imus >= 7:
    ax7 = csvFile['AX7']
    ay7 = csvFile['AY7']
    az7 = csvFile['AZ7']
    p7Offset = calibrationFile['P6']
    r7Offset = calibrationFile['R6']
    p7 = []
    r7 = []
    h7 = []
if imus >= 8:
    ax8 = csvFile['AX8']
    ay8 = csvFile['AY8']
    az8 = csvFile['AZ8']
    p8Offset = calibrationFile['P7']
    r8Offset = calibrationFile['R7']
    p8 = []
    r8 = []
    h8 = []

for i in range(len(time)): 
    if imus >= 1:
        p1.append(math.atan2(ay1[i],az1[i]) * 180/math.pi)
        r1.append(math.atan2(ax1[i], math.sqrt(ay1[i]**2 +  az1[i]**2) ) * 180/math.pi)
    if imus >= 2:
        p2.append(math.atan2(ay2[i],az2[i]) * 180/math.pi)
        r2.append(math.atan2(ax2[i], math.sqrt(ay2[i]**2 +  az2[i]**2) ) * 180/math.pi)
        #p2Offset = p2[0]
        #r2Offset = r2[0]
        h2.append(x2 * math.sin( (r2[i] - r2Offset) * math.pi / 180 )) 
    if imus >= 3:
        p3.append(math.atan2(ay3[i],az3[i]) * 180/math.pi)
        r3.append(math.atan2(ax3[i], math.sqrt(ay3[i]**2 +  az3[i]**2) ) * 180/math.pi)
        #p3Offset = p3[0]
        #r3Offset = r3[0]
        h3.append(x3 * math.sin( (r3[i] - r3Offset) * math.pi / 180 ))
    if imus >= 4:
        p4.append(math.atan2(ay4[i],az4[i]) * 180/math.pi)
        r4.append(math.atan2(ax4[i], math.sqrt(ay4[i]**2 +  az4[i]**2) ) * 180/math.pi)
        #p4Offset = p4[0]
        #r4Offset = r4[0]
        h4.append(x4 * math.sin( (r4[i] - r4Offset) * math.pi / 180 ))
    if imus >= 5:
        p5.append(math.atan2(ay5[i],az5[i]) * 180/math.pi)
        r5.append(math.atan2(ax5[i], math.sqrt(ay5[i]**2 +  az5[i]**2) ) * 180/math.pi)
        #p5Offset = p5[0]
        #r5Offset = r5[0]
        h5.append(x5 * math.sin( (r5[i] - r5Offset) * math.pi / 180 ))
    if imus >= 6:
        p6.append(math.atan2(ay6[i],az6[i]) * 180/math.pi)
        r6.append(math.atan2(ax6[i], math.sqrt(ay6[i]**2 +  az6[i]**2) ) * 180/math.pi)
        #p6Offset = p6[0]
        #r6Offset = r6[0]
        h6.append(x6 * math.sin( (r6[i] - r6Offset) * math.pi / 180 ))
    if imus >= 7:
        p7.append(math.atan2(ay7[i],az7[i]) * 180/math.pi)
        r7.append(math.atan2(ax7[i], math.sqrt(ay7[i]**2 +  az7[i]**2) ) * 180/math.pi)
        #p7Offset = p7[0]
        #r7Offset = r7[0]
        h7.append(x7 * math.sin( (r7[i] - r7Offset) * math.pi / 180 ))
    if imus >= 8:
        p8.append(math.atan2(ay8[i],az8[i]) * 180/math.pi)
        r8.append(math.atan2(ax8[i], math.sqrt(ay8[i]**2 +  az8[i]**2) ) * 180/math.pi)
        #p8Offset = p8[0]
        #r8Offset = r8[0]
        h8.append(x8 * math.sin( (r8[i] - r8Offset) * math.pi / 180 ))

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on=False, xlim=(0, 650), ylim=(-200, 200))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    thisx = [x1, x2, x3, x4, x5, x6, x7, x8]
    thisy = [0, h2[i], h3[i], h4[i], h5[i], h6[i], h7[i], h8[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (time[i]))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, np.arange(1, len(h2)), interval=2
, blit=True, init_func=init)

ani.save(filename[:-4] + '_wingExcitation.gif', fps=20)
plt.show()
