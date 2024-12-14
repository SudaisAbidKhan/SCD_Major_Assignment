from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

# Enable CORS before route definitions
CORS(app, resources={r"/get_recipes": {"origins": "*"}})

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    try:
        data = request.get_json()
        user_ingredients = data.get('ingredients', [])
        user_dietary = data.get('dietary', [])

        # Load and clean the dataset
        df = pd.read_csv('C:\\Users\\admin\\Desktop\\CSV\\archive\\RecipeNLG_dataset.csv')
        df['ingredients'] = df['ingredients'].fillna('').str.lower().str.replace(r'[^\w\s]', '', regex=True)
        df['NER'] = df['NER'].str.lower().str.replace(r'[^\w\s]', '', regex=True)

        # Search for recipes that match user input
        matching_recipes = df[
            df['ingredients'].apply(lambda x: any(ingredient in x for ingredient in user_ingredients)) &
            df['NER'].apply(lambda x: any(tag in x for tag in user_dietary))
        ]

        # Format the results
        recipes = matching_recipes[['ingredients', 'NER', 'directions']].to_dict(orient='records')

        return jsonify({'recipes': recipes})
    except Exception as e:
        print("Error:", e)
        return jsonify({'error': 'Something went wrong'}), 500

if __name__ == '__main__':
    print("Server is starting...")
    app.run(debug=True, port=5001)
