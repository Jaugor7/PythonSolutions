#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[15]:


def rotation_is_substr(main_str, sub_str):
    if sub_str in main_str+main_str:
        return "Rotation True"
    return "Rotation False"

if __name__ == "__main__":
    main_str = input('Enter Your Main String\n').strip()
    sub_str = input("Enter Your Sub String\n").strip()
    print(rotation_is_substr(main_str, sub_str))
    


# In[ ]:




