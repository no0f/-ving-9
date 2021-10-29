# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:01:46 2021

@author: Minh Tri, Huynh
"""

with open('sporsmaalsfil.txt','r',encoding = 'UTF-8') as fila:
    for line in fila:
        #words =line.split(':')
        class spørrespill:
    
            def __init__(self, para_tekst):
                self.tekst= para_tekst
            def __str__(self):
                return'Spørsmålstekst er: {} \n'.format(self.tekst)
        listquestion=[]
        spørsmål=spørrespill(line)
        print(spørsmål)
        listquestion.append(line)