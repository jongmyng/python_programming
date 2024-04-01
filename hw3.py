#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_fixed_price(discount_rate, discount_price) :
    price = discount_price / (1 - discount_rate / 100)
    return price
    
discount_rate = int(input('할인율은?'))
a_discount_price = int(input('a 상품의 할인된 가격은?'))
b_discount_price = int(input('b 상품의 할인된 가격은?'))

a_price = get_fixed_price(discount_rate, a_discount_price)
b_price = get_fixed_price(discount_rate, b_discount_price)
print('A 상품의 정가는 ', a_price, '원')
print('B 상품의 정가는', b_price, '원')


# In[ ]:




