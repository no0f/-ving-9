class sp�rrespill:
    
    def __init__(self, para_tekst, para_svarer, para_tall):
        self.tekst= para_tekst
        self.svar=para_svarer
        self.tall=para_tall
    def __str__(self):
        return'Sp�rsm�lstekst er: {} '.format(self.tekst)
    #def question(self):
        #return '{},{},{}'.format(self.tekst,self.svar,self.tall)
    def new_question(self,ny_tekst,nye_svarer):
        self.tekst=ny_tekst
        self.svar=nye_svarer
        print(sp�rsm�l)
        nye_svarer=input('Skriv inn ditt svar: \n')
        if self.svar==nye_svarer:
            print('Korrekt')
        else:
            print('Pr�ve p� nytt')
        return
        
sp�rsm�l=sp�rrespill('Hvor mange dager er det i et �r','\nA.365\nB.366\n\
C.364\nD.360' ,'A')
#print(sp�rsm�l)
sp�rsm�l.new_question('Hvor bor du n�','Stavanger')



