#!/usr/bin/env python
# coding: utf-8
import numpy as np
dir_list = ["Peng-Wei", "Tristan", "Ancel", "Noble"]
dir_list = ["Tristan", "Ancel", "Noble", "Delaunay", "Miras", "Mirone", "Ming", "Peng-Wei"]
dir_list = ["Tristan", "Ancel", "Noble", "Mirone", "Ming", "Miras", "Peng-Wei", "Delaunay", "Plazen2"]

i_max = 24
color_list = ["\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[0m"]

participant_dic = {}
for participant in dir_list:
    participant_dic[participant] = []

# Find theoric value
theoric = []
for i in range(1, i_max + 1):
    with open("theoric/ma_reponse_{}.txt".format(i), "r") as f:
        ans = f.readline()
    theoric.append(float(ans))

for i in range(1, i_max + 1):
    #print(i, end="\t")
    for dir_ in dir_list:
        with open(dir_+"/ma_reponse_{}.txt".format(i), "r") as f:
            ans = f.readline()
        err = abs(float(ans) - theoric[i - 1])
        #print("%2.6f" %err, end="\t")
        participant_dic[dir_].append(err)
    #print(theoric[i-1])

print("Absolute error : ", end=" ")
for i in range(3):
    print(color_list[i] + str(i+1), end=color_list[4] + "\t")
print(color_list[3] + "worst", end=color_list[4] + "\n")
print("Test :\t", end="")
for name in dir_list:
    if len(name) < 8:
        print(name, end="\t\t")
    else:
        print(name, end="\t")

print()

classement_moyen = {}
for participant in dir_list:
    classement_moyen[participant] = []

for i in range(0, i_max):
    print(i + 1, end="\t")
    act = []
    for dir_ in dir_list:
        act.append(participant_dic[dir_][i])
    act = np.array(act)
    order = np.sort(act)
    for value in act:
        if value == order[0]:
            print(color_list[0] + "%2.6f" %value, end="\033[0m\t")
        elif value == order[1]:
            print(color_list[1] + "%2.6f" %value, end="\033[0m\t")
        elif value == order[2]:
            print(color_list[2] + "%2.6f" %value, end="\033[0m\t")
        elif value == order[-1]:
            print(color_list[3] + "%2.6f" %value, end="\033[0m\t")
        else:
            print("%2.6f" %value, end="\t")
    print()
    for dir_ in dir_list:
        classement_moyen[dir_].append(np.where(order == participant_dic[dir_][i])[0][0])

print("All", end="\t")
act = []
for dir_ in dir_list:
    act.append(sum(participant_dic[dir_]))
order = np.sort(act)
for value in act:
    if value == order[0]:
        print(color_list[0] + "%2.6f" %value, end="\033[0m\t")
    elif value == order[1]:
        print(color_list[1] + "%2.6f" %value, end="\033[0m\t")
    elif value == order[2]:
        print(color_list[2] + "%2.6f" %value, end="\033[0m\t")
    elif value == order[-1]:
        print(color_list[3] + "%2.6f" %value, end="\033[0m\t")
    else:
        print("%2.6f" %value, end="\t")
print()

print("Ranking", end="\t")
act = []
for dir_ in dir_list:
    act.append(sum(classement_moyen[dir_])/len(classement_moyen[dir_]))
order = np.sort(act)
for value in act:
    if value == order[0]:
        print(color_list[0] + "%2.6f" %value, end="\033[0m\t")
    elif value == order[1]:
        print(color_list[1] + "%2.6f" %value, end="\033[0m\t")
    elif value == order[2]:
        print(color_list[2] + "%2.6f" %value, end="\033[0m\t")
    elif value == order[-1]:
        print(color_list[3] + "%2.6f" %value, end="\033[0m\t")
    else:
        print("%2.6f" %value, end="\t")
print()
