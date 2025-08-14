import pandas as pd
from functions.file_readers import read_csv
from functions.data_merger import merge_df
import pytest_cov
'''
As a user i want to be able to read the stock and sales files and have them as panda dataframes
TDD format, write the test first then the function
'''
#comments
def test_read_csv_type():
    # Arrange
    filename = "data/test_stock.csv"
    expected_datatype = pd.DataFrame
    
    # Act
    ouput = read_csv(filename)
    
#as a user I want to be able to merge 2 datafame by a product_id field then subtract sales from stock
def test_merge_data_column_count():
    # Arrange
    stock_filename = "data/test_stock.csv"
    sales_filename = "data/test_sales.csv"
    
    stock_df = read_csv(stock_filename)
    sales_df = read_csv(sales_filename)
    
    #Act
    merged_df = merge_df(stock_df, sales_df)
    
    #Assert
    
    # Assert
    assert len(merged_df.columns)==11

def test_read_csv_content_id():
    # Arrange
    filename = "data/test_stock.csv"
    expected_id = 123
    
    # Act
    output = read_csv(filename)
    id = output.iloc[0]['id']
    
    # Assert
    assert id == expected_id