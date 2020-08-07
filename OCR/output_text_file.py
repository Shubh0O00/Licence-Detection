from datetime import datetime

def string_insert(*args):
    li=list(args)
    #print(li)
    string=" ".join(li)
    i=len(string)
    for i in range(25-i):
        string+=" "
    string+="  "
    string+= str(datetime.now())
    file = open('OUTPUT_FILE.txt', 'a+')
    file.write(string)
    file.write('\n\n')
    file.close()