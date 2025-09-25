import pandas as pd 
dfs = pd.read_html("https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub", encoding='utf-8')
for df in dfs:
    for index, row in df.iterrows():
        print(f"Index: {index}, Row: {row[0]} {row[1]} {row[2]}")
