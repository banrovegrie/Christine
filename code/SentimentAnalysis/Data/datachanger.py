import pandas as pd


# colnames = ['SENTIMENT', 'TEXT']
df = pd.read_csv('training.1600000.processed.noemoticon.csv')
zero = df[df.SENTIMENT == 0]
four = df[df.SENTIMENT == 4]
