methods=dir(__builtins__)


with open("builtinmethods.txt","w") as f:
    for method in methods:
        f.write(method)
        f.write("\n")
        #to skip above 2 lines use below print both of these work same
        #print(method,file=f)
    
