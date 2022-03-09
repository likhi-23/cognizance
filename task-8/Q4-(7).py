import pandas as pd



ser = pd.Series(['amrita', 'school', 'of','engineering','chennai','campus'])
modified_ser= ser.str.title()  
print("The original series: ")
print(ser)
print("\nThe modified series: ")
print(modified_ser)


