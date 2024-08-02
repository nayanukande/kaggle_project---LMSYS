import pandas as pd
import numpy as np
import re
import codecs

# Loading the dataset(by defeault )
df=pd.read_csv(r'C:\Users\nayan\test_conda\kaggle_competition\data\external\train.csv')
# Identify columns that start with 'Unnamed'
unnamed_columns = [col for col in df.columns if col.startswith('Unnamed')]
# Drop the unwanted columns
df.drop(columns=unnamed_columns, inplace=True)
# Function to detect Unicode escape sequence
def contains_unicode_escape(text):
    if isinstance(text, str):
        unicode_escape_pattern = re.compile(r'\\u[0-9A-Fa-f]{4}')
        return bool(unicode_escape_pattern.search(text))
    return False
# Applying this function to response_a column to get the count of UES
df.to_csv('decoded_output_file_v2.csv', index=False, encoding='utf-8-sig')


