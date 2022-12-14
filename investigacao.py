#!/usr/bin/env python
# coding: utf-8

# 
# Vamos fazer um programa para verificar quem é o assassino de um crime.
# Para descobrir o assassino, a polícia faz um pequeno questionário com 5
# perguntas onde a resposta só pode ser sim ou não:
# 

# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?

# Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
# suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
# 2 pontos são apenas suspeitos, necessitando outras investigações. Valores
# iguais ou abaixo de 1 são liberados.


total = 0

resposta1 = input('Mora perto da vítima? (sim/nao)')
resposta1 = resposta1.upper()
if(resposta1 == 'SIM'):
        total += 1 
while(resposta1 != 'SIM' and resposta1 != 'NAO'):
    print('Digite uma resposta válida: (sim/nao)')
    resposta1 = input('Mora perto da vítima? (sim/nao)')
    resposta1 = resposta1.upper()
    if(resposta1 == 'SIM'):
        total += 1     

resposta2 = input('Já trabalhou com a vítima? (sim/nao)')
resposta2 = resposta2.upper()
if(resposta2 == 'SIM'):
        total += 1 
while(resposta2 != 'SIM' and resposta2 != 'NAO'):
    print('Digite uma resposta válida: (sim/nao)')
    resposta2 = input('Já trabalhou com a vítima? (sim/nao)')
    resposta2 = resposta2.upper()
    if(resposta2 == 'SIM'):
        total += 1 
    
resposta3 = input('Telefonou para a vítima? (sim/nao)')
resposta3 = resposta3.upper()
if(resposta3 == 'SIM'):
    total += 1
while(resposta3 != 'SIM' and resposta3 != 'NAO'):
    print('Digite uma resposta válida: (sim/nao)')
    resposta3 = input('Telefonou para a vítima? (sim/nao)')
    resposta3 = resposta3.upper()
    if(resposta3 == 'SIM'):
        total += 1 
    
resposta4 = input('Esteve no local do crime? (sim/nao)')
resposta4 = resposta4.upper()
if(resposta4 == 'SIM'):
    total += 1
while(resposta4 != 'SIM' and resposta4 != 'NAO'):
    print('Digite uma resposta válida: (sim/nao)')
    resposta4 = input('Esteve no local do crime? (sim/nao)')
    resposta4 = resposta4.upper()
    if(resposta4 == 'SIM'):
        total += 1 
    
resposta5 = input('Devia para a vítima? (sim/nao)')
resposta5 = resposta5.upper()
if(resposta5 == 'SIM'):
    total += 1
while(resposta5 != 'SIM' and resposta5 != 'NAO'):
    print('Digite uma resposta válida: (sim/nao)')
    resposta5 = input('Devia para a vítima? (sim/nao)')
    resposta5 = resposta5.upper()
    if(resposta5 == 'SIM'):
        total += 1 
    
    
if(total == 5):
    print('Este suspeito é um dos assassinos.')
elif(total == 3 or total == 4):
    print('Este suspeito é um dos cúmplices.')
elif(total == 2):
    print('Continua como suspeito, faz-se necessário mais investigações')
else:
    print('O suspeito pode ser liberado.')
    
print('O total de respostas sim foi:', total)


# In[ ]:




