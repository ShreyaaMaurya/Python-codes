#unique element function
def unique_element(list1):
    print(set(list1))
unique_element([1,2,2,3,4,1,5])
 
#List rotation

def list_rotation(list1, k):
    list2 = []
    for i in range(len(list1)-k, len(list1)):
        list2.append(list1[i])
    for i in range(len(list1)-k):
        list2.append(list1[i])
    print(list2)
list_rotation([1,2,3,4,5], 2)

#Find longest word

def longest_word(str1):
    str2 = str1.split()
    longest = str2[0]
    for str in str2:
        if len(str) > len(longest):
            longest = str 
            print(longest)
longest_word("Python is amazing Programming language")


#Sum of digit

def sum_of_digits(n):
    sum = 0
    for i in range (1, n+1):
        sum = sum + i 
        print(sum)
sum_of_digits(5)

#character frequency counter

def char_frequency(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
        print(freq)
char_frequency("hello")

#Numbers divisible by 3 or 5 

def divisible_or_not(n):
    for i in range(1, n+1):
        if (i%3==0) ^ (i%5==0):
            print(i)
divisible_or_not(15)

#reverse word
'''
def reverse(string):
    str = " "
    str1 = []
    for ch in string:
        if ch == " ":
            str.append(str)
        else:
            str += ch
    str1.append(str)
    reversed_sentence = ""
    for i in range (len(str1) -1, -1, -1):
        reversed_sentence += str1[i]
        if i != 0:
            reversed_sentence += ""
        print(reversed_sentence)
reverse("my name is shreya")
'''
#star diamond pattern

def pattern(n):
   for i in range(1, n+1, 2):
      spaces = (n-i)//2
      print(" " *spaces + "*" * i)
pattern(5)

# count consonent

def count_consonent(s):
    vowel = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in vowel:
            count += 1
        print(count)
count_consonent("hello world")

#number guessing game 

key = 8

while True:
    guess = int(input("Guess the number: "))
    if guess == key:
        print("Correct! You guessed it :)")
        break
    else:
        print("Wrong try again :/")