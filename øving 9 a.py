# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:01:46 2021

@author: Minh Tri, Huynh
"""

with open('sporsmaalsfil.txt','r',encoding = 'UTF-8') as fila:
    for line in fila:
        words =line.split(':')
        class spørrespill:
    
            def __init__(self, para_tekst, para_svarer, para_tall):
                self.tekst= para_tekst
                self.svar=para_svarer
                self.tall=para_tall
            def __str__(self):
                return'Spørsmålstekst er: {} \nSvaralternativer er {} \n'.format(self.tekst, self.svar,)
    #def question(self):
        #return '{},{},{}'.format(self.tekst,self.svar,self.tall)
            def anwser(self):
                svarer=input('Skriv inn ditt svar : \n')
                if self.tall==svarer:
                    print('Korrekt')
                else:
                    print('Feil')
                return

        spørsmål=spørrespill(words[0],words[2],words[1])
        print(spørsmål)
        spørsmål.anwser()