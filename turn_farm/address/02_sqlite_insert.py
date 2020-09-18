import sqlite3 as db
import pandas as pd

df = pd.read_json('road_name.json')
con = db.connect('./road_name.db')

df.to_sql('t_road_name', con=con)