import pandas as pd 
def merge_df(df1, df2):
    merge_df = df1.merge(df2,how='left', on='product_id')
    return merge_df