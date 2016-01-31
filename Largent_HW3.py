
# coding: utf-8

# In[174]:

# ----------------------------------------------------------------------------- #
# --------------------------------- Homework 3 -------------------------------- #
# ----------------------------------------------------------------------------- #

get_ipython().system('ipython nbconvert --to script Largent_HW3.ipynb')

#1

def histogram(list1):
    for i in list1:
        temp1 = i
        while 0 < temp1:
            print("*", end = "")
            temp1 -= 1
        print()

#2

def max_in_list(list1):
    max_val = list1[0]
    for i in list1:
        if i > max_val:
            max_val = i
    return max_val

#3

def list_converter(list1):
    list2 = [0] * len(list1)
    for i in range(0,len(list1)):
        list2[i] = len(list1[i])
    return list2

#4

def find_longest_word(list1):
    long_str = len(list1[0])
    for i in range(0,len(list1)):
        if len(list1[i]) > long_str:
            long_str = len(list1[i])
    return long_str
    
#5

def filter_long_words(list1,int1):
    list2 = []
    for i in range(0,len(list1)):
        if len(list1[i]) > int1:
            list2.append(list1[i])
    return list2

#6

def palindrome_rec(string1):
    string2 = string1.lower()
    frwd, bkwd = "", ""
    for i in string2:
        if i in "abcdefghijklmnopqrstuvwxyz":
            frwd = frwd + i
            bkwd = i + bkwd
    if frwd == bkwd:
        return True
    else:
        return False
    
palindrome_rec("Was it a rat I saw?")
        
#7

def pangram_test(string1):
    string2 = string1.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for j in alphabet:
        if j not in string2:
            return False
    return True

#8

def bottles_99():
    count = 99
    while count != 0:
        print(str(count) + " bottles of coke on the wall, " + str(count) + " bottles of coke.")
        print("Take one down, pass it around, " + str(count-1) + " bottles of coke on the wall.")
        count -= 1
        
#9

def translate(string1):
    string1_list = string1.split()
    dictionary = {'merry':'god','christmas':'jul','and':'och',
                  'happy':'gott','new':'nytt','year':"år"}
    string2 = ""
    for word in string1_list:
        if word in dictionary and word != string1_list[-1]:
            string2 += dictionary[word] + " "
        elif word in dictionary:
            string2 += dictionary[word]
    
    return string2

#10

def char_freq(string1):
    dictionary = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,
                  'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,
                  'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,
                  'y':0,'z':0}
    for char in string1.lower():
        if char in dictionary:
            dictionary[char] += 1
    return dictionary
    
#11

def decoder(string1):
    key ={'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u',
          'i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c',
          'q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k',
          'y':'l','z':'m','A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S',
          'G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A',
          'O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I',
          'W':'J','X':'K','Y':'L','Z':'M'}
    string2 = ""
    for char in string1:
        if char in key:
            string2 += key[char]
        else:
            string2 += char
    return string2

#12

def correct(string1):
    string2 = ""
    for char in string1:
        if char == ".":
            string2 += char + " "
        else:
            string2 += char
    
    string2_list = string2.split()
    string3 = ""
    for word in string2_list:
        if word in word != string2_list[-1]:
            string3 += word + " "
        else:
            string3 += word
        
    return string3


#13

def make_3sg_form(verb1):
    
    if verb1.endswith("y") == True:
        verb2 = verb1[:-1] + "ies"
    elif verb1.endswith(("o","ch","s","sh","x","z")) == True:
        verb2 = verb1 + "es"
    else:
        verb2 = verb1 + "s"
    return verb2
    
#14

def make_ing_form(verb1):
    if verb1.endswith("ie") == True:
        verb2 = verb1[:-2] + "ying"
    elif verb1.endswith("e") == True and verb1 != "be" and verb1.endswith("ee") == False:
        verb2 = verb1[:-1] + "ing"
    elif len(verb1) >= 3 and verb1[-3] not in "aeiouy" and verb1[-1] not in "aeiouy" and verb1[-2] in "aeoiouy":
            verb2 = verb1 + verb1[-1] + "ing"
    else:
        verb2 = verb1 + "ing"
    return verb2


# In[ ]:



