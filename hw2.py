#!/usr/bin/env python
# coding: utf-8

# In[1]:


def exchange(money):                          
    a500 = money // 500          
    money %= 500    
    a100 = money // 100            
    money %= 100    
    a50 = money // 50            
    money %= 50    
    a10 = money // 10   
    print('','500원 동전의 개수:', a500,'\n',
          '100원 동전의 개수:', a100,'\n',
          '50원 동전의 개수:', a50,'\n',
          '10원 동전의 개수:', a10)
    
def get_integer(prompt):
    res = int(input(prompt))
    return res

input_money = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(input_money)


# In[ ]:




