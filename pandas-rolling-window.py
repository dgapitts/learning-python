# As per https://stackoverflow.com/questions/67444424/jupyter-notebook-for-csv-file-to-select-3-window-rolling

text = """first
1
2
3
4
5
6
7
8
9
10"""

import pandas as pd
import io

df = pd.read_csv(io.StringIO(text))
#df = pd.DataFrame(range(1,11), columns=['first'])
print(df)

df['second'] = df['first'].shift(-1) #, fill_value=0)
df['third'] = df['first'].shift(-2)
print(df)

#df = df.dropna().astype(int)
df = df[:-2].astype(int)
print(df)
