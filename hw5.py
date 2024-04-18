#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read_single_digit(n):
    if n== 0 :
        return '영'
    if n == 1:
        return '일'
    elif n == 2:
        return '이'
    elif n == 3:
        return '삼'
    elif n == 4:
        return '사'
    elif n == 5:
        return '오'
    elif n == 6:
        return '육'
    elif n == 7:
        return '칠'
    elif n == 8:
        return '팔'
    elif n == 9:
        return '구'
        
def read_number(a):
    hundreds = a // 100
    tens = (a // 10) % 10
    ones = a % 10
    return [hundreds, tens, ones]

num = int(input('세 제리 정수 입력:'))

a= read_number(num)
n1 =read_single_digit(a[0])
n2 = read_single_digit(a[1])
n3 = read_single_digit(a[2])
print(f'{n1} {n2} {n3}')


# In[ ]:




