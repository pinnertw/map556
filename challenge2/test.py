from Angrybird import AngryBird
import numpy as np
import mon_controle as MC
import pandas as pd
from tqdm import tqdm

env = AngryBird()
cost = 0.
nul = np.zeros(2)
for i in tqdm(range(1, 1001)):
    state = env.reset()
    vents = pd.read_csv("../data/vent_{}.csv".format(i))
    env.vent[:, 0] = vents.vent_x
    env.vent[:, 1] = vents.vent_y
    for j in range(10):
        state, _, _, _ = env.step(MC.main(int(state[0]), state[1:]))
    env.step(nul)
    cost += np.sum(env.cost)
cost /= 1000

with open("estimation.txt", "w") as f:
    f.write("{:.6f}".format(cost))
print(cost)
