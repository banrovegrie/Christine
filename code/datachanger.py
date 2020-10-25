import pandas as pd
colnames = ['SENTIMENT', 'TEXT']
df = pd.read_csv('../betterdata.csv',usecols=colnames)

zero = df[df.SENTIMENT == 0]
four = df[df.SENTIMENT == 4]

zero = zero.head(40000)
four = four.head(40000)

final_data = pd.concat([zero, four], ignore_index=True)
final_data.to_csv('../betterdata_1.csv', index=False)