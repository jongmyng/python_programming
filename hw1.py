#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 과제 조건_1
def get_radius(prompt):
    r = int(input(prompt))
    return r
print('넓이를 구하고자 하는 원의 반지름은?')
prompt = int(input())
print('반지름' , prompt , '인 원의 넓이', 
      '=', '3.14 *' ,prompt,'*' ,prompt ,'=' , prompt * prompt * 3.14 )


# In[2]:


# 과제 조건_2
def get_cicle_area(prompt):
    r= int(input(prompt))
    return r*r*3.14  
get_cicle_area(prompt)


# In[ ]:





# In[ ]:




