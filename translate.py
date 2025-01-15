import pandas as pd
from googletrans import Translator
import time

translator = Translator()

def translate_text(text, target_lang='ar'):
    # Skip empty or None texts
    if not text or text.strip() == "":
        return ""
    
    attempts = 3
    for attempt in range(attempts):
        try:
            translated = translator.translate(text, dest=target_lang)
            return translated.text
        except Exception as e:
            print(f"Error translating '{text}': {e}")
            time.sleep(2)  # Delay before retrying
    return "" 

# Load the Excel file
input_file = 'Book1.xlsx'  
output_file = 'translated_file.xlsx'

df = pd.read_excel(input_file)

df['translated_phrase'] = df['phrase'].apply(translate_text)

df.to_excel(output_file, index=False)

print(f"Translation complete. The translated content has been saved to {output_file}.")
