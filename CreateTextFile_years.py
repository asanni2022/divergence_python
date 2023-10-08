years = [1980, 1981,1982,1983,1984,1988,2001]
with open("testyears.txt", "w") as years_file:
    for year in years:
        years_file.write(f"{year}\n")