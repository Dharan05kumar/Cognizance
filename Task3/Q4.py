import pandas as pd
ser=pd.Series(['amrita','school','of','engineering','chennai','campus'])
print("Before Changing")
print(list(ser))
newSeries=ser.map(lambda x: x[0].upper() + x[1:])
s=list(newSeries)
Str=' '.join([str(elem) for elem in s])
print("After changing")
print(Str)
