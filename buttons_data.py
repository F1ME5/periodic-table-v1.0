# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

#Module for setting bg, x and y values in Tkinter Button

#Project modules
from dimensions_data import x_positions, y_positions
from util import C_0, C_1

aux1, aux2 = C_0, C_0

def get_element_color(groupBlock):
    color = ""
    if groupBlock == "alkaline earth metal":
        color = "AB5CF2"
    elif groupBlock == "alkali metal":
        color = "EB0026"
    elif groupBlock == "transition metal":
        color = "5CB8D1"
    elif groupBlock == "noble gas":
        color = "F090A0"
    elif groupBlock == "nonmetal":
        color = "FFFF30"
    elif groupBlock == "metalloid":
        color = "9eaF51"
    elif groupBlock == "metal":
        color = "3DFF00"
    elif groupBlock == "lanthanoid":
        color = "94FFFF"
    elif groupBlock == "actinoid":
        color = "1FFFC7"
    elif groupBlock == "halogen":
        color = "DBDB56"
    else:#post-transition metal
        color = "60C73F"

    return "#" + color

def get_x_y(element, atomicNumber, groupBlock):
    global aux1, aux2

    #Element data used to get X & Y positions. Also atomicNumber and groupBlock
    period = element["period"]
    group = element["group"]

    #Auxiliary index variables
    y_positions_index, x_positions_index = C_0, C_0

    #setting X & Y positions
    if groupBlock == "lanthanoid":
        y_positions_index = period + C_1
        x_positions_index = group + aux1
        aux1 += C_1
    elif groupBlock == "actinoid":
        y_positions_index = period + C_1
        x_positions_index = group + aux2
        aux2 += C_1 
    else:
        y_positions_index = period - C_1
        x_positions_index = group - C_1

    #Correcting stuff
    if atomicNumber == 5:#Boron
        y_positions_index = period
    elif atomicNumber == 103:#Lawrencium
        y_positions_index = y_positions.__len__() - C_1
        x_positions_index = x_positions.__len__() - C_1
    
    x = x_positions[x_positions_index]
    y = y_positions[y_positions_index]

    return x, y