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
<<<<<<< HEAD
        if i==0 or i==19 or j==0 or j==19:
            deger=kenarlik(i,j)
        else:
            deger=area(i,j)
        #deger=random.randint(0,7)
        liste[i].append(deger)
print (liste)


with open('/Users/furkanceran/Desktop/adventure-game/level0_data', 'wb') as f:
=======
        deger=random.randint(0,7)
        liste[i].append(deger)

with open('/Users/furkanceran/Desktop/adventure-game/level10_data', 'wb') as f:
>>>>>>> parent of e47e9bf... last
    pickle.dump(liste, f)