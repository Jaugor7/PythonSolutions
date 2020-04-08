#!/usr/bin/env python
# coding: utf-8

# In[20]:


def remove_space(main_str):
    i = 0
    
    while main_str[i] != '&':
        if main_str[i] == ' ':
            main_str = main_str[:i] + '%20' + main_str[i+1:]
        i += 1
        
    main_str = main_str[:i]
    return main_str

if __name__ == "__main__":
    main_str = input("Enter Your String\n").strip() + '&'
    print(remove_space(main_str))


# In[ ]:





# In[ ]:





# In[ ]:




