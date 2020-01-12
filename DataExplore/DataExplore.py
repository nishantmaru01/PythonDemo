import numpy as np
import pandas as pd
def outlier_Fun(x):
    per75,per25 = np.nanpercentile(x,[75,25])
    iqr = per75 -per25
    upper = per75 + (1.5*iqr)
    lower = per25 - (1.5*iqr)
    return [i for i in x if i>upper or i<lower]

def dataframeExplor(df):
    df.info()
    print("ROWS: {} COLUMNS: {}".format(str(df.shape[0]),str(df.shape[1])))
    null_df = pd.DataFrame(df.isnull().sum())
    null_df.columns = ['counts']
    null_df[null_df['counts']>0]
    df_num = df.select_dtypes(exclude='object')
    for i in df_num.columns:
        print(i)
        print(outlier_Fun(df_num[i]))
        