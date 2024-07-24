# Python file to cleaning dataset

# Importing all necessary library
import pandas as pd
import numpy as np
import re

# Loading the dataset
data=pd.read_csv(r'C:\Users\nayan\test_conda\kaggle_competition\data\external\train.csv')
df=pd.DataFrame(data)

# Define the cleaning function
def remove_unwanted_characters(text):
    return re.sub(r'[^\w\s]', '', text)

# Apply the cleaning function to relevant columns
df['clean_prompt'] = df['prompt'].apply(remove_unwanted_characters)
df['clean_response_a'] = df['response_a'].apply(remove_unwanted_characters)
df['clean_response_b'] = df['response_b'].apply(remove_unwanted_characters)

# Because of cleaninng unwanted character from the given dataset we also have to remove the original columns
columns_to_remove = ['prompt', 'response_a', 'response_b']
df=df.drop(columns=columns_to_remove)

# to change the posiiton of the column as the original once
new_column_order = ['id', 'model_a', 'model_b', 'clean_prompt', 'clean_response_a', 'clean_response_b', 'winner_model_a', 'winner_model_b', 'winner_tie']
df = df[new_column_order]

# Function to detect Cyrilic text in a dataset
def contains_cyrilic(text):
    cyrillic_pattern = re.compile('[\u0400-\u04FF\u0500-\u052F\u2DE0-\u2DFF\uA640-\uA69F\u1C80-\u1C8F]')
    return bool(cyrillic_pattern.search(text))
# Applying the function to the dataframe
df['clean_prompt'] = df[]

df.head(10)


