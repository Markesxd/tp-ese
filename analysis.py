import pandas as pd
from sys import argv 

file = argv[1]

db = pd.read_csv('data/' + file)

print(db.info())

print(db.describe())
