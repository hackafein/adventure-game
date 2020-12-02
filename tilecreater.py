import pickle
from os import path
import random
level=0

#pickle_in = open('/Users/furkanceran/Desktop/adventure-game/level0_data', 'rb')
#world_data = pickle.load(pickle_in)
#print(world_data)
liste=[]
for i in range(0,20):
    liste.append([])
    for j in range(0,20):
        deger=random.randint(0,7)
        liste[i].append(deger)

with open('/Users/furkanceran/Desktop/adventure-game/level10_data', 'wb') as f:
    pickle.dump(liste, f)