import pandas as pd 

def print_text_art(matrix,vertical_flip=False):
    """
    Helper function that accepts a matrix of characters
    and prints them out. Optional parameter `vertical_flip`
    will flip the art vertically
    """
    if (vertical_flip): matrix.reverse();
    for line in matrix:
        for char in line:
            print(char,end="")
        print("")

def display_text_art_from_gdoc(url):
    """
    Main function that accepts a url containing an html table
    of text art data. This function loads data from provided url
    and prints it out.
    """
    # use pandas to load data from html table at gdoc url
    dfs = pd.read_html(str(url), header=0, encoding='utf-8')
    data = pd.concat(dfs)
    
    # initialize matrix that will hold text art
    rows = data['y-coordinate'].max() + 1 
    cols = data['x-coordinate'].max() + 1
    matrix = [[" " for i in range(cols)] for j in range(rows)]
    
    # loop through data and build output matrix
    for index,row in data.iterrows():
        line = int(row['y-coordinate'])
        char = int(row['x-coordinate'])
        matrix[line][char] = row['Character']
    
    # print text art matrix, flipped vertically (y=0 is at the bottom)
    print_text_art(matrix,vertical_flip=True)
    
url1 = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub";
url2 = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
url3 = "x"

display_text_art_from_gdoc(url2);