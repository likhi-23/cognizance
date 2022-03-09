import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
k=ser.str.capitalize()
for j in k:
 print(j,end=' ')
