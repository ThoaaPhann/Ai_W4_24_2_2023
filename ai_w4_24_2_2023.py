# -*- coding: utf-8 -*-
"""Ai_W4_24_2_2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vMjytQtwbadnzgOq0NXki4vPdpmMnNv-
"""

pip install scikit-fuzzy

import numpy as np

import skfuzzy as fuzz

import matplotlib.pyplot as plt

x = np.arange(30,81,1)
slow = fuzz.trimf(x,[30,30,50])
medium = fuzz.trimf(x,[30,50,70])
medium_fast = fuzz.trimf(x,[50,60,80])
full_speed = fuzz.trimf(x,[60,80,80])

plt.figure()
plt.plot(x,slow,'#8c564b',linewidth = 1.5, label = 'slow' )
plt.plot(x,medium,'b',linewidth = 1.5, label = 'medium' )
plt.plot(x,medium_fast,'g',linewidth = 1.5, label = 'medium_fast' )
plt.plot(x,full_speed,'y',linewidth = 1.5, label = 'full_speed' )

x = np.arange (30,81,1)
slow = fuzz.trapmf (x,[30,30,40,50])
medium = fuzz.trapmf(x,[30,50,55,70])
medium_fast = fuzz.trapmf(x,[50,60,70,80])
full_speed = fuzz.trapmf(x,[60,65,70,80])

plt.figure()
plt.plot(x,slow,'#8c564b',linewidth = 1.5, label = 'slow' )
plt.plot(x,medium,'b',linewidth = 1.5, label = 'medium' )
plt.plot(x,medium_fast,'g',linewidth = 1.5, label = 'medium_fast' )
plt.plot(x,full_speed,'y',linewidth = 1.5, label = 'full_speed' )

import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl 
x = np.arange(30,81,1)
slow3 = fuzz.gaussmf(x,30,5)
medium3 = fuzz.gaussmf(x,50,5)
medium_fast3 = fuzz.gaussmf(x,65,5)
full_speed3 = fuzz.gaussmf(x,80,5)
plt.figure()
plt.plot(x,slow3,'#8c564b',linewidth = 1.5, label = 'slow3' )
plt.plot(x,medium3,'b',linewidth = 1.5, label = 'medium3' )
plt.plot(x,medium_fast3,'g',linewidth = 1.5, label = 'medium_fast3' )
plt.plot(x,full_speed3,'y',linewidth = 1.5, label = 'full_speed3' )

import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl 

food = ctrl.Antecedent(np.arange(0,11,1),'food')
service = ctrl.Antecedent(np.arange(0,11,1),'service')
tip = ctrl.Consequent(np.arange(10,31,1),'tip')

food ['poor'] = fuzz.trimf(food.universe, [0,0,5])
food ['average'] = fuzz.trimf(food.universe, [0,5,10])
food ['good'] = fuzz.trimf(food.universe, [5,10,10])

service ['poor'] = fuzz.trimf(service.universe, [0,0,5])
service ['average'] = fuzz.trimf(service.universe, [0,5,10])
service ['good'] = fuzz.trimf(service.universe, [5,10,10])

tip ['less'] = fuzz.trimf(tip.universe, [0,0,5])
tip ['normal'] = fuzz.trimf(tip.universe, [0,5,10])
tip ['much'] = fuzz.trimf(tip.universe, [5,10,10])

food.view()
service.view()
tip.view()

food['poor'].view()

rule1 = ctrl.Rule(food['poor'] & service['poor'], tip['less'])
rule2 = ctrl.Rule(food['poor'] & service['average'], tip['less'])
rule3 = ctrl.Rule(food['poor'] & service['good'], tip['normal'])
rule4 = ctrl.Rule(food['average'] & service['poor'], tip['less'])
rule5 = ctrl.Rule(food['average'] & service['average'], tip['normal'])
rule6 = ctrl.Rule(food['average'] & service['good'], tip['much'])
rule7 = ctrl.Rule(food['good'] & service['poor'], tip['normal'])
rule8 = ctrl.Rule(food['good'] & service['average'], tip['normal'])
rule9 = ctrl.Rule(food['good'] & service['good'], tip['much'])
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['food'] = 6.5 ##tin hieu vao
tipping.input['service']= 9.8
tipping.compute()
print (tipping.output['tip'])
tip.view(sim=tipping)

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['food'] = 9 ##tin hieu vao
tipping.input['service']= 10
tipping.compute()
print (tipping.output['tip'])
tip.view(sim=tipping)

import numpy as np 
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl 

time = ctrl.Antecedent(np.arange(10,180,1),'time')
rice = ctrl.Antecedent(np.arange(200,2001,1),'rice')
power = ctrl.Consequent(np.arange(0,110,1),'power')

time ['VF'] = fuzz.trimf(time.universe, [10,10,20])
time ['F'] = fuzz.trimf(time.universe, [20,30,70])
time ['AV'] = fuzz.trimf(time.universe, [20,50,100])
time ['S'] = fuzz.trimf(time.universe, [80,100,160])
time ['VS'] = fuzz.trimf(time.universe, [130,180,180])

rice ['VL'] = fuzz.trimf(rice.universe, [200,550,600])
rice ['L'] = fuzz.trimf(rice.universe, [400,900,900])
rice ['AV'] = fuzz.trimf(rice.universe, [800,1300,1300])
rice ['M'] = fuzz.trimf(rice.universe, [1200,1700,1700])
rice ['VM'] = fuzz.trimf(rice.universe, [1600,2000,2000])

power ['small'] = fuzz.trimf(power.universe, [0,50,50])
power ['average'] = fuzz.trimf(power.universe, [40,80,80])
power ['high'] = fuzz.trimf(power.universe, [60,100,100])

rule1 = ctrl.Rule(time['VF']&rice['VL'],power['average'])
rule2 = ctrl.Rule(time['VF']&rice['L'],power['average'])
rule3 = ctrl.Rule(time['VF']&rice['AV'],power['high'])
rule4 = ctrl.Rule(time['VF']&rice['M'],power['high'])
rule5 = ctrl.Rule(time['VF']&rice['VM'],power['high'])
rule6 = ctrl.Rule(time['F']&rice['VL'],power['average'])
rule7 = ctrl.Rule(time['F']&rice['L'],power['average'])
rule8 = ctrl.Rule(time['F']&rice['AV'],power['average'])
rule9 = ctrl.Rule(time['F']&rice['M'],power['high'])
rule10 = ctrl.Rule(time['F']&rice['VM'],power['high'])
rule11 = ctrl.Rule(time['AV']&rice['VL'],power['small'])
rule12 = ctrl.Rule(time['AV']&rice['L'],power['small'])
rule13 = ctrl.Rule(time['AV']&rice['AV'],power['small'])
rule14 = ctrl.Rule(time['AV']&rice['M'],power['high'])
rule15 = ctrl.Rule(time['AV']&rice['VM'],power['high'])
rule16 = ctrl.Rule(time['S']&rice['VL'],power['average'])
rule17 = ctrl.Rule(time['S']&rice['L'],power['average'])
rule18 = ctrl.Rule(time['S']&rice['AV'],power['average'])
rule19 = ctrl.Rule(time['S']&rice['M'],power['high'])
rule20 = ctrl.Rule(time['S']&rice['VM'],power['high'])
rule21 = ctrl.Rule(time['VS']&rice['VL'],power['average'])
rule22 = ctrl.Rule(time['VS']&rice['L'],power['average'])
rule23 = ctrl.Rule(time['VS']&rice['AV'],power['high'])
rule24 = ctrl.Rule(time['VS']&rice['M'],power['high'])
rule25 = ctrl.Rule(time['VS']&rice['VM'],power['high'])

powering_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule21,rule22,rule23,rule24,rule25])
powering = ctrl.ControlSystemSimulation(powering_ctrl)
powering.input['time'] = 80
powering.input['rice'] = 550
time.view()
rice.view()
power.view()
powering.compute()
print(powering.output['power'])
power.view(sim = powering)