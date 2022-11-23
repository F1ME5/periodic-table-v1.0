# Copyright 2022 by Néstor Nahuatlato
# <soy_nestor@hotmail.com>
# Licensed under GNU General Public License 3.0 or later.
# @license GPL-3.0+

#Module for setting x and y values in elements buttons

#Modify
C_X_INCREASING = 70
C_Y_INCREASING = 96
C_BEGIN = 40

#Do not modify
X_1 = C_BEGIN
X_2 = X_1 + C_X_INCREASING
X_3 = X_2 + C_X_INCREASING
X_4 = X_3 + C_X_INCREASING
X_5 = X_4 + C_X_INCREASING
X_6 = X_5 + C_X_INCREASING
X_7 = X_6 + C_X_INCREASING
X_8 = X_7 + C_X_INCREASING
X_9 = X_8 + C_X_INCREASING
X_10 = X_9 + C_X_INCREASING
X_11 = X_10 + C_X_INCREASING
X_12 = X_11 + C_X_INCREASING
X_13 = X_12 + C_X_INCREASING
X_14 = X_13 + C_X_INCREASING
X_15 = X_14 + C_X_INCREASING
X_16 = X_15 + C_X_INCREASING
X_17 = X_16 + C_X_INCREASING
X_18 = X_17 + C_X_INCREASING

Y_1 = C_BEGIN
Y_2 = Y_1 + C_Y_INCREASING
Y_3 = Y_2 + C_Y_INCREASING
Y_4 = Y_3 + C_Y_INCREASING
Y_5 = Y_4 + C_Y_INCREASING
Y_6 = Y_5 + C_Y_INCREASING
Y_7 = Y_6 + C_Y_INCREASING
Y_8 = Y_7 + C_Y_INCREASING + 30
Y_9 = Y_8 + C_Y_INCREASING

period_x_position = X_1 - (C_BEGIN / 2)
x_positions = [X_1, X_2, X_3, X_4, X_5, X_6, X_7, X_8, X_9, X_10, X_11, X_12, X_13, X_14, X_15, X_16, X_17, X_18]
y_positions = [Y_1, Y_2, Y_3, Y_4, Y_5, Y_6, Y_7, Y_8, Y_9]
group_aux_dict = {
    X_1 : Y_1,
    X_2 : Y_2, 
    X_3 : Y_4,
    X_4 : Y_4, 
    X_5 : Y_4, 
    X_6 : Y_4, 
    X_7 : Y_4, 
    X_8 : Y_4, 
    X_9 : Y_4, 
    X_10 : Y_4, 
    X_11 : Y_4, 
    X_12 : Y_4, 
    X_13 : Y_2, 
    X_14 : Y_2, 
    X_15 : Y_2,
    X_16 : Y_2,
    X_17 : Y_2,
    X_18 : Y_1
}