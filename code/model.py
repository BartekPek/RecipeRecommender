import os
import argparse
import pandas as pd
import mlflow
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from scipy import sparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train TF-IDF model for recipe recommendation')
    
    parser.add_argument('--data', type=str, required=True, help='Path to processed CSV file')
    parser.add_argument('--save_dir', type=str, required=True, help='Directory to save model and matrix')
    
    args = parser.parse_args()

    os.makedirs(args.save_dir, exist_ok=True)
    
    data = pd.read_csv(args.data)
    ingredients = data['ingredients_clean']
    
    mlflow.set_experiment('Recipe_recommendation')
    with mlflow.start_run():
    
        # TF-IDF #
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(ingredients)
        
        # Logging params
        mlflow.log_param('vocab_size', len(vectorizer.get_feature_names_out()))
        mlflow.log_param('ngram_range', vectorizer.ngram_range)
        mlflow.log_param('tfidf_rows', X.shape[0])
        mlflow.log_param('tfidf_cols', X.shape[1])
    
        # Save vectorizer #
        vectorizer_path = os.path.join(args.save_dir, 'vectorizer.pkl')
        with open(vectorizer_path, 'wb') as f:
            pickle.dump(vectorizer, f)
        
        # Save matrix #
        matrix_path = os.path.join(args.save_dir, 'tfidf_matrix.npz')
        sparse.save_npz(matrix_path, X)

        mlflow.log_artifact(vectorizer_path)
        mlflow.log_artifact(matrix_path)
        
        print('Model and matrix saved successfully.')
        print(f'- Vectorizer: {vectorizer_path}')
        print(f'- Matrix: {matrix_path}')
