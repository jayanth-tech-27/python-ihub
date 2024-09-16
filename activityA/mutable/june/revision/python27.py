import pickle
j = 'Jayanth_vanamala'
with open('work27.txt', 'wb') as f:
    pickle.dump(j,f)











with open('work27.txt', 'rb') as f:
    c = pickle.load(f)
    print(c)
