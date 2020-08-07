#Defining this list to check and remove special characters from the recognised text 
#As there is no special character in a license plate

def list_cleaner(l):
    special_characters=''' !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~“ '''

    li_modified=[]

    #To create a modified list which does not contains special characters
    for i in l:
        s=""
        for j in i:
            #print(s)
            if j not in special_characters:
                s+=j
        li_modified.append(s)

    print(li_modified)
    #To remove NULL strings from the list
    for x in li_modified:
        if x == '':
            li_modified.remove(x)

    li_duplicate_removal = list(set(li_modified))
    return li_duplicate_removal
