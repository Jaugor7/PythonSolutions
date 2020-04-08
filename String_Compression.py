#!/usr/bin/env python
# coding: utf-8

# In[10]:


def string_compress(inp_str, n):
    count_var = 1
    output_len = 0
    output_str = []

    for i in range(n-1):

        if inp_str[i] == inp_str[i+1]:
            count_var += 1

        else:
            output_str.append(inp_str[i])
            output_str.append(str(count_var))
            output_len += 1
            count_var = 1

    output_str.append(inp_str[n-1])
    output_str.append(str(count_var))
    output_len += 1
    
    if output_len < n:
        return ''.join(output_str)
    else:
        return inp_str


if __name__ == '__main__':
    print("String Compression")
    inp_str = input("Enter Your String").strip()
    print(string_compress(inp_str, len(inp_str)))


# In[ ]:




