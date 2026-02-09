import os
import argparse
import pickle
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from utils import text_cleaner


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Recipe recommendation')
    
    parser.add_argument(
        '--ingredients',
        type=str,
        required=True,
        help='Ingredients provided by user'
    )
    
    parser.add_argument(
        '--model_dir',
        type=str,
        required=True,
        help='Directory containing vectorizer and tfidf matrix'
    )
    
    parser.add_argument(
        '--data',
        type=str,
        required=True,
        help='Path to processed CSV file'
    )
    
    args = parser.parse_args()
    
    vectorizer_path = os.path.join(args.model_dir, 'vectorizer.pkl')
    matrix_path = os.path.join(args.model_dir, 'tfidf_matrix.npz')
    
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
        
    matrix = sparse.load_npz(matrix_path)
    
    recipes = pd.read_csv(args.data)
    
    ingredients_raw = args.ingredients
    ingredients_clean = text_cleaner(ingredients_raw)
    
    query_vec = vectorizer.transform([ingredients_clean])
    
    scores = cosine_similarity(query_vec, matrix).flatten()

    top_n = 5
    top_idx = scores.argsort()[::-1][:top_n]

    print('Top recommended recipes: \n')
    for idx in top_idx:
        title = recipes.loc[idx, "recipe_title"]
        desc = recipes.loc[idx, "description"]
        ingr = recipes.loc[idx, "ingredients"]
        direc = recipes.loc[idx, "directions"]

        print("\n============================")
        print(f"  {title}")
        print("----------------------------")
        print(f" Description:\n{desc}\n")
        print(" Ingredients:")
        print(ingr)
        print("\n Directions:")
        print(direc)
        print("============================\n")

