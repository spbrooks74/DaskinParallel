import dask.dataframe as ddf
from dask import delayed

df = ddf.read_csv("Activity_22.2/data/2000*.csv")

df.compute()
print(df.head())

mean = df['x'].mean().compute()
print(f'mean: {mean}')


cols = len(df.columns)
print(f'columns: {cols}')


rows = len(df.index)
print(f'rows:{rows}')