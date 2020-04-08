#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[3]:


def anagram(main_str, ana_str):
    main_str = sorted(main_str)
    ana_str = sorted(ana_str)
    if main_str == ana_str:
        return "Same"
    else:
        return 'Different'

if __name__ == "__main__":
    my_str = input('Enter Your String\n').strip()
    sub_str = input("Enter Your Sub String\n").strip()
    
    print(anagram(my_str,sub_str))
    


# In[ ]:




