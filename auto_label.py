#!/usr/bin/python3

# The following code automatocally puts xml tags in the text on the provided list of words. The output is to be used for GATE.

import re
import os, glob

unlabeled = 'new1.txt'
labeled = 'new2.txt'


# labeling function
def labelme(temp1,nam,list1):
    for i in list1:
        j = i.strip()
        if len(j)>0 and j.lower() in temp1.lower():
            temp1 = re.sub(j,'<'+nam+'>'+j+'</'+nam+'>',temp1,flags=re.I)
    return temp1




# function getting the catgories and their associated words
def get_cat():
    # get all the names of the catgories from the file names
    path = 'files/'
    cat_list = []
    for f in os.listdir(path):
        cat_list.append(re.sub('_',' ',f[:f.rfind(".")]))
    # get the list of the lists of category values
    list_of_list =[]
    for filename in glob.glob(os.path.join(path, '*.txt')):
        f1 = open(filename,'r')
        list_of_list.append(f1.readlines())
        f1.close()
    # create a dictionary of labeling categories and their values
    master_dict = dict(zip(cat_list, list_of_list))
    return master_dict


def main():
    # open and read the file to be labeled
    file = open(unlabeled,'r')
    text = file.readlines()
    file.close()
    # open a file to write the labeled text
    fnew = open(labeled, 'w')
    temp = ''
    #get the dictionary of categories
    cat_dict = get_cat()
    print('Dictionary of categories:   ',cat_dict)
    # take each line of the file to be labeled and check for each list of category values
    for line in text:
        temp = line
        for k,v in cat_dict.items():
            temp = labelme(temp,k,v)
        #print(temp)
        fnew.write(temp)
    fnew.close()



if __name__ == "__main__":main()



