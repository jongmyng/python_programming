# -*- coding: utf-8 -*-
"""hw7

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KuZ5jJGyVp6FeYDkutFkixKj4BSWzNZ2
"""

shopping_bag = []
while True :
  print('[구입]')
  pro = input('상품명?')
  num = input('수량은?')
  if pro == '':
    break
  shopping_bag.append({pro : num})
  print(f'장바구니에 {pro}가 {num}개 담겼습니다 \n')

print(f'장바구니 보기 >> {shopping_bag} \n')

while True:
  print(['검색'])
  find=input('장바구니에서 확인하고자하는 상품은? \n')
  if find == '':
    break
  for item in shopping_bag:
    if find in item:
      cnt = item[find]
      print(f'[{find}]는 {cnt}개 있습니다')