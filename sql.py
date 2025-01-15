import pandas as pd

# Load the Excel file
input_file = 'translated_file.xlsx'  
df = pd.read_excel(input_file)

# Open a file to write the SQL queries with UTF-8 encoding
output_file = 'queries.sql' 
with open(output_file, 'w', encoding='utf-8') as f:

    f.write("INSERT INTO `language_phrases` (`language_id`, `phrase`, `translated`) VALUES\n")

    for index, row in df.iterrows():
        language_id = row['language_id']
        phrase = str(row['phrase'])  
        translated = str(row['translated'])
        phrase = phrase.replace("'", "''")
        translated = translated.replace("'", "''")
        
        sql_query = f"({language_id}, '{phrase}', '{translated}')"
        
        if index == len(df) - 1:
            f.write(sql_query + ";")
        else:
            f.write(sql_query + ",\n")

print(f"SQL queries have been written to {output_file}.")
