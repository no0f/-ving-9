class spørrespill:
    
    def __init__(self, para_tekst, para_svarer, para_tall):
        self.tekst= para_tekst
        self.svar=para_svarer
        self.tall=para_tall
    def __str__(self):
        return'Spørsmålstekst er: {} '.format(self.tekst)
    #def question(self):
        #return '{},{},{}'.format(self.tekst,self.svar,self.tall)
    def new_question(self,ny_tekst,nye_svarer):
        self.tekst=ny_tekst
        self.svar=nye_svarer
        print(spørsmål)
        nye_svarer=input('Skriv inn ditt svar: \n')
        if self.svar==nye_svarer:
            print('Korrekt')
        else:
            print('Prøve på nytt')
        return
        
spørsmål=spørrespill('Hvor mange dager er det i et år','\nA.365\nB.366\n\
C.364\nD.360' ,'A')
#print(spørsmål)
spørsmål.new_question('Hvor bor du nå','Stavanger')



