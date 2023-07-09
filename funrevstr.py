def rev_str(string):
    r_str=""    
    for i in string:
        r_str=i+r_str 
    return r_str
print("The revrse string is :",rev_str(("1234abcd")))