#!/usr/bin/env python
# coding: utf-8
import numpy as np
dir_list = ["Tristan", "Ancel", "Noble", "Mirone", "Ming", "Miras", "Peng-Wei", "Delaunay", "Plazen2"]
dir_list = ["peng-wei", "peng-wei_baseline"]

color_list = ["\033[92m", "\033[93m", "\033[94m", "\033[91m", "\033[0m"]

participant_dic = {}
for participant in dir_list:
    participant_dic[participant] = []

for dir_ in dir_list:
    with open(dir_ + "/estimation.txt", "r") as f:
        ans = float(f.readline())
    participant_dic[dir_].append(ans)

for i in range(3):
    print(color_list[i] + str(i+1), end=color_list[4] + "\t")
print(color_list[3] + "worst", end=color_list[4] + "\n")

print("\t", end="")
for dir_ in dir_list:
    print(dir_, end="\t")
print()

print("Score", end="\t")
act = []
for dir_ in dir_list:
    act.append(participant_dic[dir_][0])
order = np.sort(act)
for value in act:
    if value == order[0]:
        print(color_list[0] + "%2.1f" %value, end="\033[0m\t\t")
    elif value == order[1]:
        print(color_list[1] + "%2.1f" %value, end="\033[0m\t\t")
    elif value == order[2]:
        print(color_list[2] + "%2.1f" %value, end="\033[0m\t\t")
    elif value == order[-1]:
        print(color_list[3] + "%2.1f" %value, end="\033[0m\t\t")
    else:
        print("%2.1f" %value, end="\t")

print()

print("Rank", end="\t")
for value in act:
    index = np.where(order == value)[0][0]
    print(index + 1, end="\t\t")
