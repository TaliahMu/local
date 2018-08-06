import numpy as np
numbers = np.arange(1,58)[...,None]
file = open('data3.txt')
names = file.readlines()
del(names[0])
with open("data3.txt") as file:
    names = []
    for line in file:
        # The rstrip method gets rid of the "\n" at the end of each line
        names.append(line.rstrip().split(","))
flat_list = [item for sublist in names for item in sublist]
team_names = np.array(flat_list)[...,None]
