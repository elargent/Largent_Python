
# coding: utf-8

# In[174]:

# ----------------------------------------------------------------------------- #
# --------------------------------- Homework 3 -------------------------------- #
# ----------------------------------------------------------------------------- #

#1

def histogram(list1):
    
    """
    This function, histogram, takes a list of integers and 
    prints a histogram. 
    
    Parameters:
    list1 - a list composed of integers
    
    Return:
    Histogram formed by printing asterisks
    """
    
    for i in list1:
        temp1 = i
        while 0 < temp1:
            print("*", end = "")
            temp1 -= 1
        print()

#2

def max_in_list(list1):
    
    """
    This function, max_in_list, takes a list of integers or
    decimals and returns the largest number in that list.
    
    Parameters:
    list1 - a list composed of integers or decimals
    
    Return:
    maxval - integer or decimal
    """
    
    max_val = list1[0]
    for i in list1:
        if i > max_val:
            max_val = i
    return max_val

#3

def list_converter(list1):
    
    """
    This function, list_converter, takes a list of words
    and returns a list of integers which correspond to the
    length of each word.
    
    Parameters:
    list1 - a list composed of words
    
    Return:
    list2 - a list composed of integers
    """
        
    list2 = [0] * len(list1)
    for i in range(0,len(list1)):
        list2[i] = len(list1[i])
    return list2

#4

def find_longest_word(list1):

    """
    This function, find_longest_word, takes a list of words
    and returns the longest word in that list
    
    Parameters:
    list1 - a list composed of words
    
    Return:
    long_str - string
    """    
    
    long_str = len(list1[0])
    for i in range(0,len(list1)):
        if len(list1[i]) > long_str:
            long_str = len(list1[i])
    return long_str
    
#5

def filter_long_words(list1,int1):
    
    """
    This function, filter_long_words, takes a list of words
    and an integer and then returns a list composed of
    the words that have a length larger than the integer. 
    
    Parameters:
    list1 - a list composed of words
    int1 - integer
    
    Return:
    list2 - a list composed of words
    """        
    
    list2 = []
    for i in range(0,len(list1)):
        if len(list1[i]) > int1:
            list2.append(list1[i])
    return list2

#6

def palindrome_rec(string1):
    
    """
    This function, palindrome_rec, takes a string
    and then tests to see if it is a palindrome
    irrespective of punctuation and case. It returns 
    'True' if the string is a palindrome, and 'False'
    if it is not. 
    
    Parameters:
    string1 - string
    
    Return:
    True/False
    """     
    
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
    
#palindrome_rec("Was it a rat I saw?")
        
#7

def pangram_test(string1):
    
    """
    This function, pangram, takes a string and tests
    if it contains all the letters in the alphabet. 
    It returns 'True' if it does contain all letters, 
    and 'False' if it does not. 
    
    Parameters:
    string1 - string
    
    Return:
    True/False
    """     
    
    string2 = string1.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for j in alphabet:
        if j not in string2:
            return False
    return True

#8

def bottles_99():
    
    """
    This function, bottles_99, does not take any parameters.
    It prints the song, '99 Bottles of Coke'. 
    
    Parameters:
    None
    
    Return:
    "99 Bottles of Coke" via print statements
    """       
    
    count = 9
    while count != 0:
        print(str(count) + " bottles of coke on the wall, " + str(count) + " bottles of coke.")
        print("Take one down, pass it around, " + str(count-1) + " bottles of coke on the wall.")
        count -= 1
        
#9
## Specifications require a list of words, not a single string containing multiple words = Prof G
def translate(string1):
    
    """
    This function, translate, takes a string that contains
    the words, "merry christmas and happy new year," and 
    returns the phrase in Swedish. The words can be in any order,
    but why butcher a traditional greeting?
   
    Parameters:
    string1 - string containing above words
    
    Return:
    string2 - string containing swedish words
    """   
    
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
## Should only return counts for characters in the string. More helpful if the list is in alphabetical order.
def char_freq(string1):
    
    """
    This function, char_freq, takes a string and then returns
    the frequency of each letter in the string. The frequency
    is returned as a dictionary.
    
    Parameters:
    string1 - string
    
    Return:
    dictionary - dictionary indicating how many times each letter appears
    """  
    
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
    
    """
    This function, decoder, takes a string and then either encodes or
    decodes it based on a 13-letter Caesar cypher. 
    
    Parameters:
    string1 - string
    
    Return:
    string2 - encoded/decoded string
    """
    
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
    
    """
    This function, correct, takes a string and returns a string
    that corrects any incorrect spacing between words and ensures
    there is a space after every period. 
    
    Parameters:
    string1 - string
    
    Return:
    string3 - string
    """
    
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
    
    """
    This function, make_3sg_form, takes a singular verb and then 
    returns the third-person singular form of the word. Note that
    the function does not work in all cases.
    
    Parameters:
    verb1 - string
    
    Return:
    verb2 - string
    """
    
    if verb1.endswith("y") == True:
        verb2 = verb1[:-1] + "ies"
    elif verb1.endswith(("o","ch","s","sh","x","z")) == True:
        verb2 = verb1 + "es"
    else:
        verb2 = verb1 + "s"
    return verb2
    
#14

def make_ing_form(verb1):
    
    """
    This function, make_ing_form, takes a verb in infinitive form and then 
    returns the present participle form of the verb. Note that
    the function does not work in all cases.
    
    Parameters:
    verb1 - string
    
    Return:
    verb2 - string
    """    
    
    if verb1.endswith("ie") == True:
        verb2 = verb1[:-2] + "ying"
    elif verb1.endswith("e") == True and verb1 != "be" and verb1.endswith("ee") == False:
        verb2 = verb1[:-1] + "ing"
    elif len(verb1) >= 3 and verb1[-3] not in "aeiouy" and verb1[-1] not in "aeiouy" and verb1[-2] in "aeoiouy":
            verb2 = verb1 + verb1[-1] + "ing"
    else:
        verb2 = verb1 + "ing"
    return verb2


##Test Cases

print("1 Histogram ", histogram([1,2,3,5,6,7,6,5,4,3,2,1]), '\n')

print("2 Max in List 77 ", max_in_list([1,2,3,77,4,5,6,7]), '\n')

print("3 word to length map 3,5,7,4 ", list_converter(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("4 Longest word 7 ", find_longest_word(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("5 filter long words snake, dolphin ", filter_long_words(['dog', 'snake', 'dolphin', 'cats'],4), '\n')

print("6 Palindrome phrase TRUE ", palindrome_rec("Go hang a salami I'm a lasagna hog."), '\n')

print("7 Pangram TRUE ", pangram_test("The quick brown fox jumps over the lazy dog."), '\n')

print("8 Cokes \n", bottles_99())

##print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate(['merry', 'christmas', 'happy']), '\n')
print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate('merry christmas happy'), '\n')

print("10 Char Freq {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')

print("11 Decoder Caesar cipher? I much prefer Caesar salad!", decoder("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"), '\n')

print("12 correct This is very funny and cool. Indeed!", correct("This is very funny and cool.Indeed!"), '\n')

print("13 3ps brushes ", make_3sg_form("brush"), '\n')
print("13 3ps tries ", make_3sg_form("try"), '\n')
print("13 3ps runs ", make_3sg_form("run"), '\n')
print("13 3ps fixes ", make_3sg_form("fix"), '\n')

print("14 ing lying ", make_ing_form("lie"), '\n')
print("14 ing seeing ", make_ing_form("see"), '\n')
print("14 ing moving ", make_ing_form("move"), '\n')
print("14 ing hugging ", make_ing_form("hug"), '\n')