import pandas as pd
from Angrybird import AngryBird

vents = pd.read_csv("ventETU.csv")


for i in range(1, 101):
    env = AngryBird()
    env.reset()
    vents.vent_x = env.vent[:, 0]
    vents.vent_y = env.vent[:, 1]
    vents.to_csv("vent_{}.csv".format(i))
