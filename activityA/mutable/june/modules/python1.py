import pandas as pd

data_sets = pd.DataFrame([
    [1000, 'mobile-1', 23232, 's1'],
    [1002, 'mobile-2', 27100, 's2'],
    [1003, 'mobile-3', 29000, 's3'],
    [1004, 'mobile-4', 3100, 's4'],
    [1005, 'mobile-5', 3300, 's5']
], columns=['ID', 'Name', 'Value', 'Status'])

print(data_sets)
