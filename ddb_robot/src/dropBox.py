#!/usr/bin/env python3

import numpy as np
import subprocess


dropOneBox = 0
dropSquareOfBoxes = 0
dropSquareOfBoxesSeperated = 1 #1m spacing between boxes


boxNum = 0
#drop a single box
if dropOneBox:
    x_location = 0
    y_location = 0
    boxname = "boxSingle" + str(boxNum)
    suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)



#drop sqare of boxes with 1m seperation between each box
if dropSquareOfBoxesSeperated:
    sizeSquare = 50 #50m x 50m square interior dimension
    sizeBox = 1 #1m by 1m box 
    center_x = 0
    center_y = 0

    #start at the positive x positive y corner
    start_point_x = (sizeSquare/2) + (np.sqrt(.5)) #sqrt(.5) makes the inside corner of the box at 25,25
    start_point_y = (sizeSquare/2) + (np.sqrt(.5))
    

    #side 1
    for i in range((sizeSquare/2)+1):
        boxname = "boxSingle" + str(boxNum)
        if (boxNum==0):
            x_location = start_point_x
            y_location = start_point_y
        else:
            x_location = x_location - float(2*sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1

    #side 2
    for i in range((sizeSquare/2)+1):
        boxname = "boxSingle" + str(boxNum)
        if (i==0):
            x_location = x_location - float(sizeBox)
            y_location = y_location - float(sizeBox)
        else:
            y_location = y_location - float(2*sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1

    #side 3
    for i in range((sizeSquare/2)+1):
        boxname = "boxSingle" + str(boxNum)
        x_location = x_location + float(2*sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1

    #side 4
    for i in range((sizeSquare/2) + 1):
        boxname = "boxSingle" + str(boxNum)
        if (i==0):
            x_location = x_location + float(sizeBox)
            y_location = y_location + float(sizeBox)
        else:
            y_location = y_location + float(2*sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1


if dropSquareOfBoxes:
    sizeSquare = 50 #50m x 50m square interior dimension
    sizeBox = 1 #1m by 1m box 
    center_x = 0
    center_y = 0

    #start at the positive x positive y corner
    start_point_x = (sizeSquare/2) + (np.sqrt(.5)) #sqrt(.5) makes the inside corner of the box at 25,25
    start_point_y = (sizeSquare/2) + (np.sqrt(.5))
    

    #side 1
    for i in range(sizeSquare+2):
        boxname = "boxSingle" + str(boxNum)
        if (boxNum==0):
            x_location = start_point_x
            y_location = start_point_y
        else:
            x_location = x_location - float(sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1

    #side 2
    for i in range(sizeSquare+1):
        boxname = "boxSingle" + str(boxNum)
        y_location = y_location - float(sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1
        
    #side 3
    for i in range(sizeSquare+1):
        boxname = "boxSingle" + str(boxNum)
        x_location = x_location + float(sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1

    #side 4
    for i in range(sizeSquare):
        boxname = "boxSingle" + str(boxNum)
        y_location = y_location + float(sizeBox)
        print("x_location:" + str(x_location) + "  y_location:" + str(y_location) + "  boxNum:" + str(boxNum))
        suc = subprocess.check_call("./dropBoxBash.sh %s %s %s" % (str(x_location), str(y_location), str(boxname)), shell=True)
        boxNum = boxNum + 1
