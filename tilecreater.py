import pickle
from os import path
import random
level=0
def kenarlik(i,j):
    v=random.randint(0,100)
    if v<80:
        deger=1
    else:
        deger=0
    return deger
def area(i,j):
    v=random.randint(0,100)
    if v<10:
        deger=0
    elif 10<v<20:
        deger=1
    elif 20<v<30:
        deger=2
    elif 95<v:
        deger=7
    else:
        deger=random.randint(3,6)
    return deger
#pickle_in = open('/Users/furkanceran/Desktop/adventure-game/level0_data', 'rb')
#world_data = pickle.load(pickle_in)
#print(world_data)
liste=[]
for i in range(0,20):
    liste.append([])
    for j in range(0,20):
        if i==0 or i==19 or j==0 or j==19:
            deger=kenarlik(i,j)
        else:
            deger=area(i,j)
        #deger=random.randint(0,7)
        liste[i].append(deger)
print (liste)


with open('/Users/furkanceran/Desktop/adventure-game/level0_data', 'wb') as f:
    pickle.dump(liste, f)