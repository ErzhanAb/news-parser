import numpy as np
import pandas as pd
import os


def get_top(dataset: list, top: int) -> None:
    unique_values, counts = np.unique(dataset, return_counts=True)
    sorted_words = sorted(zip(unique_values, counts), key=lambda x: x[1], reverse=True)
    top_words = {
        'Value': [word[0] for word in sorted_words[:top]],
        'Amount': [amount[1] for amount in sorted_words[:top]]
    }
    df = pd.DataFrame(top_words)
    
    if not os.path.exists('outputs'):
        os.mkdir('outputs')
    
    print()
    print('=' * 50)
    print(f'The top-{top} list has been saved in outputs/top_words.csv')
    print('=' * 50)
    print()
    
    df.to_csv("outputs/top_words.csv", encoding="utf-8")