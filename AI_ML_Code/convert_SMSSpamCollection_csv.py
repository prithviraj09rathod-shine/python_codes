import pandas as pd

df = pd.read_csv("SMSSpamCollection", sep='\t', header=None)
df.columns = ['label', 'text']
df.to_csv("spam.csv", index=False)