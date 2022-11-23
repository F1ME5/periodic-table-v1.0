# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

#Module for construct the window and all the buttons and labels needed

#Python modules
from tkinter import Button, Label, Tk, font, Entry, StringVar

#Project modules
from dimensions_data import *
from util import *
import buttons_data
import api_data

#Global variables
root = Tk()
elements_buttons = []
elements_labels = []

def main_window_settings():
    global root
    root.geometry("1800x920")
    root.title("Periodic Table v1.0")

def elements_buttons_creation():
    global elements_buttons, root

    elements = api_data.get_elements_list()
    
    for element in elements:
        element = dict(element)

        #Element data shown in button
        symbol = element["symbol"]
        atomicNumber = element["atomicNumber"]
        element_mass = str(element["atomicMass"])
        aux_mass = element_mass[:6]
        mass = aux_mass.replace('(', '')

        groupBlock = element["groupBlock"]
        element["cpkHexColor"] = buttons_data.get_element_color(groupBlock)
        
        #Button values
        element_font = font.Font(family="Arial Black", size=15)
        text = f"{atomicNumber}\n{symbol}\n{mass}"
        bg = element["cpkHexColor"]

        #Button creation
        elements_buttons.append(Button(root, text=text, width=4, height=3, bg=bg, font=element_font))

        #Button command
        element_button_command(element=element, atomicNumber=atomicNumber)

        #Button position
        x, y = buttons_data.get_x_y(element=element, atomicNumber=atomicNumber, groupBlock=groupBlock)
        elements_buttons[atomicNumber - C_1].place(x=x, y=y)

def elements_labels_settings():   
    global root

    #Auxiliary variables
    correction_actinoid_x = 7
    correction_groups_y = 15
    aux_x = X_3 + X_1 - correction_actinoid_x
    lanthanoid_x = aux_x
    actinoid_x = aux_x - correction_actinoid_x

    #Labels Fonts
    title_font = font.Font(family="Lexend", size=20)
    period_font = font.Font(family="Courier New", size=12)
    group_font = font.Font(family="Courier New", size=12)
    aux_font = font.Font(family="Arial Black", size=15)

    #Title label
    Label(root, text="PERIODIC TABLE", font=title_font).place(x=X_8, y=Y_1)

    #Periods labels
    i = C_1
    for y in y_positions[:7]:
        Label(root, text=i, font=period_font).place(x=period_x_position, y=y + X_1)
        i += C_1

    #Groups labels
    i = C_1
    for x, y in group_aux_dict.items():
        Label(root, text=i, font=group_font).place(x=x + X_1 - correction_groups_y, y=y - X_1 + correction_groups_y)
        i += C_1

    #lanthanoid & actinoid labels
    Label(root, text="*", font=aux_font).place(x=lanthanoid_x, y=Y_6 + X_1)
    Label(root, text="**", font=aux_font).place(x=actinoid_x, y=Y_7 + X_1)
    Label(root, text="*", font=aux_font).place(x=lanthanoid_x, y=Y_8 + X_1)
    Label(root, text="**", font=aux_font).place(x=actinoid_x, y=Y_9 + X_1)

def element_info_labels_settings():
    global root, elements_labels

    #Labels Fonts
    element_title_font = font.Font(family="Lexend", size=18)
    text_font = font.Font(family="Courier New", size=15)
    label_font = font.Font(family="Courier New", size=14)

    #Title label
    Label(root, text="ELEMENT INFORMATION", font=element_title_font).place(x=X_18 + X_4, y=Y_1)

    #Elements labels
    text_x = X_18 + X_2
    text_y = Y_2
    for text in element_texts:
        Label(root, text=text, font=text_font).place(x=text_x, y=text_y)
        text_y += 35

    #Display labels
    i = C_0
    while i < element_texts.__len__():
        elements_labels.append(StringVar())
        i += C_1

    label_x = X_18 + X_6 + X_1
    label_y = Y_2
    for label in elements_labels:
        label.set("")
        Entry(textvariable=label, state="readonly", font=label_font).place(x=label_x, y=label_y)
        label_y += 35

def element_button_command(element, atomicNumber):
    global elements_buttons
    elements_buttons[atomicNumber - C_1]["command"] = lambda:show_element_info(element)

def show_element_info(element):
    i = C_0
    for value in element.values():
        elements_labels[i].set(value)
        i += C_1

        if i == elements_labels.__len__():
            break