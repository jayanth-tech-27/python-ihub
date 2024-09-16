import pickle

data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('work22', 'wb') as file:
    pickle.dump(data, file)