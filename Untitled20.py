#!/usr/bin/env python
# coding: utf-8

# TOPIC: Python Basics Variable

# In[12]:


#1 swap variables
x = 2
y = 3
x=x+1
y=x-1


# In[13]:


x


# In[14]:


y


# Other method

# In[15]:


x=2
y=3
x=y
y=x-1


# In[16]:


x


# In[18]:


y


# 2.AREA OF TRIANGLE

# In[5]:


#area of triangle
length = float(input("enter length value:"))


# In[6]:


width = float(input("enter width value:"))


# In[7]:


area  = (length * width) / 2
print("area:",area)


# 3.CELCIUS TO FAHRENHEIT

# In[12]:


Celcius = float(input("enter temperature in celcius:"))


# In[13]:


fahrenheit = (Celcius * 9/5)+32
print("temperature in fahrenheit:",fahrenheit)


# II.String based questions

# In[22]:


# 1. length of string
s1 = str(input())
length = len(s1)
print(length)


# In[ ]:





# In[5]:


# 2. count vowel
string = str(input())
vowels = "aeiou"
vowel_count=0
for char in string:
    if char in vowels:
        vowel_count +=1
print(vowel_count)


# In[10]:


#3.reverse the given string
string = "vamshi"
string[::-1]


# In[20]:


#4 check if string is palindrome or not
def palindrome(s1):
    if(s1==s1[::-1]):
        return "palindrome"
    else:
        return "not palindrome"
s1 = str(input())
print(palindrome(s1))


# In[23]:


#5 remove all spaces
s1 = str(input())
s1[0::2]


# In[ ]:




