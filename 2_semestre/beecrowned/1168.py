# -- coding: utf-8 --

vezes = int(input())
for j in range(0,vezes):
  num = list(input())
  qtdLeds = 0 
  for i in num:
    if i == '0':
      qtdLeds+=6
    if i == '1':
      qtdLeds+=2
    if i == '2':
      qtdLeds+=5
    if i == '3':
      qtdLeds+=5
    if i == '4':
      qtdLeds+=4
    if i == '5':
      qtdLeds+=5
    if i == '6':
      qtdLeds+=6
    if i == '7':
      qtdLeds+=3
    if i == '8':
      qtdLeds+=7
    if i == '9':
      qtdLeds+=6
  print(qtdLeds,"leds")