import pandas as pd 
url1 = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub";
url2 = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
dfs = pd.read_html(url2, encoding='utf-8')
output = []
for df in dfs:
    for index, row in df.iterrows():
       # x = row[0]
       # char = row[1]
       # y = row[2]
       # print char,
       print(f"Index: {index}, Row: {row[0]} {row[1]} {row[2]}")
