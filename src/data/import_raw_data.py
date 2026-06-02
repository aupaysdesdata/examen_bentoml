import pandas as pd

df = pd.read_csv('https://assets-datascientest.s3.eu-west-1.amazonaws.com/MLOPS/bentoml/admission.csv')
df.to_csv('data/raw/admission.csv', index_label='Unnamed: 0')