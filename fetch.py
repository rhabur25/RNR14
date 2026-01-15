import sqlite3
import gradio as gr 
import pandas as pd

def fetch_points():
   conn = sqlite3.connect('my_database.db')

   cursor = conn.cursor()

   query = '''
      SELECT *
      FROM points


   '''

   cursor.execute(query)

   results = cursor.fetchall()
   conn.close()
   df = pd.DataFrame(results, columns=['id','city', 'name'])
   df['name'] = df['name'].apply(len)
   df['city'] = df['city'].apply(len)
   print(df)

   return df

iface = gr.Interface(fn=fetch_points, inputs=[], outputs=gr.LinePlot(x='name', y='city', label='id', x_lim = (0,15), y_lim = (0,15)))
iface.launch()

