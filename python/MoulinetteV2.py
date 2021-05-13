import pandas as pd
import sqlite3 as sql
import os

folder_path = '../../dow-master/data/public'

L = []

for dirpath, dirnames, filenames in os.walk(folder_path):
  for filename in filenames:
      L.append(pd.read_excel(os.path.join(dirpath, filename),header=0))

print(L)