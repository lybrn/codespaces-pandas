import pandas as pd 
url1 = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub";
url2 = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
dfs = pd.read_html(url1, header=0, encoding='utf-8')
print(dfs);
quit

maxx = 0;
maxy = 0;
for df in dfs:
    for index, row in df.iterrows():        
        if row[0].isdigit() and row[2].isdigit():
            x = int(row[0])
            char = row[1]
            y = int(row[2])
            #print ("[" + str(y) + " " + str(x) + " " + char + "]")
            if x > maxx: 
                #print ("maxx = " + str(x))
                maxx = x
            if y > maxy: 
                maxy = y
                #print ("maxy = " + str(y))
print("maxx " + str(maxx) + " maxy " + str(maxy) )
output = [False] * int(maxy+1)
for df in dfs:
    for index, row in df.iterrows():        
        if row[0].isdigit() and row[2].isdigit():
            x = int(row[0])
            char = row[1]
            y = int(row[2])
            print (str(y) + " " + str(x) + char)
            if not output[y]: output[y] = [" "] * int(maxx+1)
            output[y][x] = char;

# output the result
for line in output:
    for char in line:
        print(char,end="")
    print("");

       #print (y + " " + x char)
       #if y == "1":
       # output.insert(int(x),char);
        # output[int(x)] = x + " : " + char
        #print (output[int(x)])
       # print char,
       #print(f"Index: {index}, Row: {row[0]} {row[1]} {row[2]}",end="")
