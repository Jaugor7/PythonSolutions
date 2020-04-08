#!/usr/bin/env python
# coding: utf-8

# In[4]:


def rezero(matrix, n, m):
    row_zero = []
    column_zero = []
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i not in row_zero:
                    row_zero.append(i)
                if j not in column_zero:
                    column_zero.append(j)
                    
    print(row_zero)
    print(column_zero)
    
    for i in range(n):
        for j in range(m):
            if i in row_zero or j in column_zero:
                matrix[i][j] = 0
            
    return matrix

if __name__ == "__main__":
    matrix = []
    n = int(input("Enter No of Rows"))
    m = int(input("Enter No of Columns"))
    print("Enter Your Matrix row wise")
    for _ in range(n):
        inp_str = input().strip()
        matrix.append(list(map(int, inp_str.split())))
        
    print(rezero(matrix, n, m))


# In[ ]:





# In[ ]:





# In[ ]:




