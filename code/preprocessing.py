import os
import re
import pandas as pd
import argparse
from utils import text_cleaner
    
    
if __name__ == '__main__':
    parser =argparse.ArgumentParser(description='Preprocess recipe dataset')
    
    parser.add_argument(
        '--input',
        type=str,
        required=True,
        help='Path to input JSON file'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help='Path to save processed CSV'
    )
    
    
    args = parser.parse_args()
    
    df_json = pd.read_json(args.input, lines=True)
    data = df_json[['recipe_title', 'ingredients', 'description', 'directions']].copy()
    
    data['title_clean'] = data['recipe_title'].apply(text_cleaner)
    data['ingredients_clean'] = data['ingredients'].apply(text_cleaner)
    
    # Saving output
    
    data.to_csv(args.output, index=False)
    
    print(f'Save processed data to: {args.output}')
    
    