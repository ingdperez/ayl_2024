import  re # import regular expression module

r_str =  r"(.*),(\d+)-(\d+)-(\d+)\n" # regular expression for searching
re_str_s = r"\1,\4/\3/\2" # regular expression for substitution, \1, \2, \3, \4 are groups in r_str
# \2 year, \3 month, \4 day
# \1 is all before the first comma

with open("ayl.csv", "r") as f: # open file ayl.csv for reading
    lines = f.readlines() # read all lines
    for line in lines[0:10]: # only first 10 lines are processed
        print("Original line: " + line.strip()) # print original line without \n
        print("Line after substitution: " + re.sub(r_str, re_str_s, line).strip()) # print line after substitution without \n
        print("Groups: ")
        for m in re.finditer(r_str, line): # find all matches in line
            groups = m.groups() # get all groups
            for g in groups:
               print(f"\t{g.strip()}") # print group g