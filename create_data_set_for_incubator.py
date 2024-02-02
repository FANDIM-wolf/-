import csv
import random
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Определение нечетких переменных для каждого входа и выхода
# В качестве примера представлены 2 входных параметра - "input1" и "input2" и 1 выходной параметр - "output"
input1 = ctrl.Antecedent(np.arange(0, 10, 1), 'input1')
input2 = ctrl.Antecedent(np.arange(38, 64, 1), 'input2')
output = ctrl.Consequent(np.arange(36.3, 38, 1), 'output')

# Определение нечетких множеств для каждой нечеткой переменной
input1['Q1'] = fuzz.zmf(input1.universe, 0.07443, 0.3246)
input1['Q2'] = fuzz.gbellmf(input1.universe, 0.146, 2.54, 0.3508)
input1['Q3'] = fuzz.gbellmf(input1.universe, 0.641, 2.47, 1.31)
input1['Q4'] = fuzz.gbellmf(input1.universe, 2.58, 2.5, 4.558)
input1['Q5'] = fuzz.smf(input1.universe, 5, 10)

input2['H1'] = fuzz.smf(input2.universe, 51.53, 62.8)
input2['H2_3'] = fuzz.gbellmf(input2.universe, 8, 3.01, 49.56)
input2['H4_5'] = fuzz.zmf(input2.universe, 38.1, 44.9)

output['T1'] = fuzz.smf(output.universe, 37.53, 38)
output['T2_3'] = fuzz.gbellmf(output.universe, 0.138, 2.61, 37.62)
output['T4'] = fuzz.gbellmf(output.universe, 0.245, 3, 37.24)
output['T5'] = fuzz.zmf(output.universe, 36.8, 37.17)

# Определение нечетких правил для анализируемой системы
rule1 = ctrl.Rule(input1['Q1'] & input2['H1'], output['T1'])
rule2 = ctrl.Rule(input1['Q2'] & input2['H2_3'], output['T2_3'])
rule3 = ctrl.Rule(input1['Q3'] & input2['H2_3'], output['T2_3'])
rule4 = ctrl.Rule(input1['Q4'] & input2['H4_5'], output['T4'])
rule5 = ctrl.Rule(input1['Q5'] & input2['H4_5'], output['T5'])

# Создание имитационной модели ANFIS на основе определенных нечетких переменных и правил
anfisctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
anfissimulation = ctrl.ControlSystemSimulation(anfisctrl)

# Задание входных значений для моделирования
anfissimulation.input['input1'] = 0
anfissimulation.input['input2'] = 64
def predict_temperature(energy , humidity):
    # Создание имитационной модели ANFIS на основе определенных нечетких переменных и правил
    anfisctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
    anfissimulation = ctrl.ControlSystemSimulation(anfisctrl)
    anfissimulation.input['input1'] = energy
    anfissimulation.input['input2'] = humidity

    # Выполнение имитационной модели ANFIS  
    anfissimulation.compute()

    return anfissimulation.output['output']
energy_of_egg = [0, 0, 0, 0.29, 0.29, 0.54, 0.67, 0.91, 1.34, 1.58, 2.42, 2.72, 4.63, 5.73, 7.11, 8.44, 8.86, 10.28]

with open('data.csv', mode='w', newline='') as data_file:
    fieldnames = [ 'day' ,'temperature', 'egg_of_old_chicken', 'egg_of_mature', 'egg_of_young_chicken', 'energy_of_egg', 'humidity']
    writer = csv.DictWriter(data_file, fieldnames=fieldnames)
    writer.writeheader()
    for j in range(45):
        for i in range(1, 19):
            if i == 1 or i == 2:
                day = i
                
                egg_of_old_chicken = round(random.uniform(37.8, 39.2), 2)
                egg_of_mature = round(random.uniform(37.7, 38.9), 2)
                egg_of_young_chicken = round(random.uniform(37.7, 38.3), 2)
                energy_of_egg_value = energy_of_egg[i-1]
                humidity = random.randint(61, 64)
                temperature = 38
            elif i == 3 or i == 4 or i == 5:
                day = i
            
                
                egg_of_old_chicken = 37.7
                egg_of_mature = 37.7
                egg_of_young_chicken = 37.7
                energy_of_egg_value = energy_of_egg[i-1]
                humidity = random.randint(50, 54)
                temperature =  predict_temperature(energy_of_egg_value , humidity)
            elif i == 6 or i == 7 or i == 8:
                day = i
                temperature = predict_temperature(energy_of_egg_value , humidity)
                egg_of_old_chicken = 37.7
                egg_of_mature = 37.7
                egg_of_young_chicken = 37.7
                energy_of_egg_value = energy_of_egg[i-1]
                humidity = random.randint(50, 54)
                temperature = predict_temperature(energy_of_egg_value , humidity)
            elif i == 9 or i == 10:
                day = i
                egg_of_old_chicken = 37.7
                egg_of_mature = 37.7
                egg_of_young_chicken = 37.7
                energy_of_egg_value = energy_of_egg[i-1]
                humidity = random.randint(38, 42)
                temperature = predict_temperature(energy_of_egg_value , humidity)
            elif i == 11 or i == 12 or i == 13 or i == 14 or i == 15:
                day = i
            
                
                egg_of_old_chicken = round(random.uniform(37.1, 37.7), 3)
                egg_of_mature = 37.7
                egg_of_young_chicken = round(random.uniform(37.6, 37.7), 3)
                energy_of_egg_value = energy_of_egg[i-1]
                humidity = random.randint(38, 42)
                temperature = predict_temperature(energy_of_egg_value , humidity)
            elif i == 16 or i == 17 or i == 18:
                day = i
                
                egg_of_old_chicken = round(random.uniform(37, 37.5), 3)
                egg_of_mature = 37.7
                egg_of_young_chicken = round(random.uniform(37.6, 37.7), 3)
                energy_of_egg_value = energy_of_egg[i-1]
                humidity = random.randint(38, 42)
                temperature = 36.8
            else:
                print("end")
            writer.writerow({'day': day,'temperature': temperature, 'egg_of_old_chicken': egg_of_old_chicken, 'egg_of_mature': egg_of_mature, 'egg_of_young_chicken': egg_of_young_chicken, 'energy_of_egg': energy_of_egg_value, 'humidity': humidity})