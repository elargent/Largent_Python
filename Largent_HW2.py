
# coding: utf-8

# In[6]:

# ----------------------------------------------------------------------------- #
# --------------------------------- Homework 2 -------------------------------- #
# ----------------------------------------------------------------------------- #

get_ipython().system('ipython nbconvert --to script Largent_HW2.ipynb')

# 1) Define a function 'fib' that takes a number, 'n', as a parameter
#    and prints all the Fibonacci numbers less than 'n' to the screen.

def fib(n):
    temp1 = 0
    temp2 = 1
    if n > 0:
        print(temp1)
    while n > temp2:
        print(temp2)
        temp2 += temp1
        temp1 = temp2 - temp1
    return;

# 2) Define a function mymax() that takes two numbers as arguments and
#    returns the largest of them. Use the if-then-else construct available
#    in Python. 

def mymax(num1,num2):
    if num1 >= num2:
        return num1
    elif num2 > num1:
        return num2
    return;

# 3) Define a function max_of_three() that takes three numbers as arguments
#    and returns the largest of them.

def mymax3(num1,num2,num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        if num3 > num1:
            return num3
    elif num2 > num1:
        if num2 >= num3:
            return num2
        if num3 > num2:
            return num3;
    return;

# 4) Define a function mylen() that computes the length of a given list or
#    string.

def mylen(str1):
    count = 0
    for i in str1:
        count += 1
    return count;
    
# 5) Write a function that takes a character (i.e. a string of length 1) and 
#    and returns True if it is a vowel, False otherwise.

def myvowel(char):
    if char == "a" or char == "e" or char == "i" or        char == "u" or char == "y": 
        return True
    else:
        return False;
    
# 6) Write a function translate() that will translate a text into
#    "rovarspraket" (Swedish for "robber's language"). That is,
#    double every consonant and place an occurence of "o" in between.
#    For example, translate("this is fun") should return the string
#    "tothohisos isos fofunon".

def translate(str1):
    str2 = ""
    for i in str1:
        if i == "a" or i == "e" or i == "i" or            i == "u" or i == "y" or i == " ": 
            str2 += i
        else:
            str2 += i + "o" + i
    return str2;

# 7) Define a function sum() and a function multiply() that sums and
#    multiplies (respectively) all the numbers in a list of numbers. 
#    For example, sum([1,2,3,4]) should return 10, and multiply([1,2,3,4])
#    should return 24.

def sum(list1):
    my_sum = 0
    for i in list1:
        my_sum += i
    return my_sum;

def multiply(list1):
    my_prod = 1
    for i in list1:
        my_prod = my_prod * i
    return my_prod;
    
# 8) Define a function reverse() that computes the reversal of a string. 
#    For example, revere ("I am testing") should return the string 
#   "gnitset ma I".

def reversal(str1):
    str2 = ""
    for i in reversed(range(len(str1))):
        str2 += str1[i]
    return str2;
    
# 9) Define a function is_palindrome() that recognizes palindromes (i.e.
#    words that look the same written backwords). For example,
#    is_palindrome("radar") should return True.

def is_palindrome(str1):
    str2 = ""
    for i in reversed(range(len(str1))):
        str2 += str1[i]
    if str1 == str2:
        return True
    else:
        return False;
    
# 10) Write a function is_member() that takes a value (i.e. a number,
#     string, etc) x and a list of values a, and returns True if x is a 
#     member of a, False otherwise.

def is_member(var1,list1):
    for i in range(len(list1)):
       if var1 == list1[i]:
            return True
            break
    return False;

# 11) Define a function overlapping() that takes two lists and returns True
#     if they have at least one member in common, False otherwise. You may  
#     use your is_member() function, or the in operator, but for the sake of
#     the exercise you should also write it using two nested for-loops.

def overlapping(list1,list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                return True
                break
    return False;

# 12) Define a function generate_n_chars() that takes an integer n and a 
#     character c and returns a string, n characters long, concisting only
#     of c:s. For example, generate_n_chars(5,"x") should return the string 
#     "xxxxx". (Python is unusual in that you can actually write an 
#     expression 5*"x" that will evaluate to "xxxxx". For the sake of the 
#     exercise you should ignore that the problem can be solved in this 
#     manner.)

def generate_n_chars(int1,char1):
    str1 = ""
    for i in range(int1):
        str1 += char1
    return str1;


