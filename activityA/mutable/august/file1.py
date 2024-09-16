import pickle

# Create a Python object
data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Open a file to write the serialized object
with open('data.pickle', 'wb') as file:
    # Use pickle.dump() to serialize the object and write it to the file
    pickle.dump(data, file)