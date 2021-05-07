import pandas as pd
import sqlite3 as sql
import os

folder_path = 'C:/Users/laure/Documents/dow-master/data/public'

for dirpath, dirnames, filenames in os.walk(folder_path):
  for filename in filenames:
      L.append(pd.read_excel(os.path.join(dirpath, filename),header=0))
