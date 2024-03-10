import csv
import pandas as pd

# with open("octanove-vocabulary-profile-c1c2-1.0.csv", mode='r') as csv_file:
df = pd.read_csv("octanove-vocabulary-profile-c1c2-1.0.csv")
vocab_set = set(df['headword'].unique())
# vocab_dict = {rows[0] : rows[2] for rows in reader}

with open("current-text.txt") as f: 
    text = f.read()
    text_set = set(text.lower().split())
    hard_words_set = text_set.intersection(vocab_set)

    print(hard_words_set)
