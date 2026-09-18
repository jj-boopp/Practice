import pandas as pd
import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
import sqlite3

conn = sqlite3.connect('project.db')
#create a dataframe from the database
df_weather = pd.read_sql_query("SELECT * FROM WEATHER", conn)
print(df_weather.head())
print(df_weather.describe())
df_weather.plot(x = 'time', y = 'temperature_c', kind = 'line')
plt.savefig('temperature_plot.png')