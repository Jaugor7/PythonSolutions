#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


def unique(main_str):
    main_str = ''.join(sorted(main_str))
    print(main_str)
    flag= 0
    
    for i in range(len(main_str)-1):
        if main_str[i] == main_str[i+1]:
            flag = 1
            break
            
    if flag == 1:
        return "False"
    else:
        return "True"

if __name__ == "__main__":
    my_str = input('Enter Your String\n').strip()
    print(unique(my_str))
    


# In[ ]:




