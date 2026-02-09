import re

units = [
    'cup', 'cups',
    'tablespoon', 'tablespoons', 'tbsp',
    'teaspoon', 'teaspoons', 'tsp',
    'ounce', 'ounces', 'oz',
    'pound', 'pounds', 'lb', 'lbs',
    'gram', 'grams', 'g',
    'kilogram', 'kilograms', 'kg',
    'ml', 'l', 'liter', 'litre', 'liters'
]

def text_cleaner(text):
    if isinstance(text, list):
        text = " ".join(text)
    text_clean = text.lower().strip()
    text_clean = re.sub(r'[^a-zA-Z\s]', '', text_clean)
    text_clean = re.sub(r'\d+', '', text_clean)
    text_clean = re.sub(r'\s+', ' ', text_clean)
    text_clean = text_clean.split()

    words = []
    
    for word in text_clean:
        if len(word) > 1 and word not in units:
            words.append(word)
    text_clean = " ".join(words)
    
    return text_clean