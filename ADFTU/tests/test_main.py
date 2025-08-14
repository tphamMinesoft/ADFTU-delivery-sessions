import pandas as pd
from functions.file_readers import read_csv
import pytest_cov
'''
As a user i want to be able to read the stock and sales files and have them as panda dataframes
TDD format, write the test first then the function
'''
def test_read_csv_type():
    # Arrange
    filename = "data/test_stock.csv"
    expected_datatype = pd.DataFrame
    
    # Act
    ouput = read_csv(filename)
    
    # Assert
    assert type(output) is expected_datatype

def test_read_csv_content_id():
    # Arrange
    filename = "data/test_stock.csv"
    expected_id = 123
    
    # Act
    output = read_csv(filename)
    id = output.iloc[0]['id']
    
    # Assert
    assert id == expected_id