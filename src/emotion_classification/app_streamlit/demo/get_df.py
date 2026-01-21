import pandas as pd
import numpy as np

def get_df_plot(df):
    # lay danh sach cac cot chua du lieu
    list_columns = df.select_dtypes(include='object').columns
    
    df = df.dropna().reset_index(drop=True)
    
    df = pd.get_dummies (
        df,
        columns=list_columns,
        dtype=int,
        drop_first=True
    )
    # Ma hoa du lieu tu object sang du lieu so
    
    df_plot = df.iloc[0:50, 0:10]
    return df_plot