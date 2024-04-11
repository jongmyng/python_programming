#!/usr/bin/env python
# coding: utf-8

# In[5]:


def rep_char(c,n):
    print(c*n)
    
    
def draw_line_string(word):
    if len('hello' + word) > len('Welcome to seoul'):
        rep_char('-', 2*len('hello' + word))
    else: rep_char('-', 3+len('Welcome to seoul'))
    
    print(f' Hello, {word}' '\n'
          '','Welcome to Seoul.')
    
    if len('hello' + word) > len('Welcome to seoul'):
        rep_char('-', 2*len('hello' + word))
    else: rep_char('-', 3+len('Welcome to seoul'))

    

msg1= input('input his/her name:')

draw_line_string(msg1)            
    


# In[ ]:




