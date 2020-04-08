#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[11]:



def swap(my_str, i ,j):
    my_str[i],my_str[j] = my_str[j], my_str[i]
    return my_str

def rever(my_str):
    i = 0
    j = len(my_str) - 1
    my_str = list(my_str)
    while i < j:
        my_str = swap(my_str,i,j)
        i += 1
        j -= 1
        
    return my_str
if __name__ == "__main__":
    my_str = input('Enter Your String\n').strip()
    print(rever(my_str))
    


# In[ ]:




