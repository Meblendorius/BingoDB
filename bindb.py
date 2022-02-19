from random import random
import sqlite3
import random
import csv
banco= sqlite3.connect('bingo.db')
cursor= banco.cursor()
cursor.execute("select * from Inovabingo")
c= cursor.fetchall()

#cursor.execute("CREATE TABLE Inovabingo (Produto TEXT UNIQUE)")
#cursor.execute("drop table Inovabingo")
#cursor.execute("insert into Inovabingo VALUES ('Fone de ouvido'), ('Carregador'), ('Câmera'), ('Valvula hidraulica'), ('Motor'),('Suporte de parede'),('Carregador veicular'),('Suporte veicular'),('Dvr'),('Power bank'),('Mouse'),('Headset'),('Controle'),('Caixa de som'),('Roteador'),('Cabo usb')")
#banco.commit()


quantidade= int(input("Quantas pessoas irão participar do bingo: "))

for nomes in range(quantidade): 
    
    nome=input("Digite seu nome: ")
    f= open('%s.csv'%nome, 'w', newline='', encoding='utf-8')
    w= csv.writer(f)

    sort= random.sample(range(1,17),len(c))
    g=1

    for i in range(4):    
        w.writerow([c[sort.index(g)][0],c[sort.index(g+1)][0],c[sort.index(g+2)][0],c[sort.index(g+3)][0]])
        g=g+4

    f.close()