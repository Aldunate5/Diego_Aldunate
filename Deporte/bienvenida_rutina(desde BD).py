import os
import random

abs=[]
rutina=[]


def base():
    file=open("core.txt") ##directorio##
    core=[]
    aux=[]
    for line in file:
        line=line.split(",")
        line = [x.strip().split("\n") for x in line]
        aux.append(line) ####buscar como hacer espacios y tabs de forma mas eficiente
    file.close()
    for a in range (len(aux)):
        core.append([])
        for b in range (len(aux[a])):
            for c in range (len(aux[a][b])):
                core[a].append(aux[a][b][c])
    lista_abs(core)

def lista_abs(core):
    global abs
    aux=[]
    for i in range (len(core)):    
        aux.append(core[i][1])
        zonas=list(set(aux))    
    for j in range (len(zonas)):
        aux=[]
        for i in range (len(core)):
            if zonas[j]==core[i][1]:
                aux.append(core[i][0])
        abs.append(aux)
    greetings()
            
    
def generar_lista(x,count,lista):
    i=0
    while i<count:
        lista_corta(x,count,lista[i])
        i+=1
    if len(rutina)<x:
        while len(rutina)<x:
            value=random.randint(0,count-1)
            new=random.choice(lista[value])
            rutina.append(new)
            if rutina.count(new)>1:
                rutina.remove(new)
    return rutina
    
def lista_corta(x,count,lista):
    random.shuffle(lista)
    a=int(x/count)
    if x%count!=0:
        for i in range (a):
            rutina.append(lista[i])
    else:
        for i in range (a):
            rutina.append(lista[i])    

def listo():
    a=0
    while a<1:
        print("Estas listo?")
        print("1. Si")
        print("2. No")
        listo=int(input())
        if listo==1:
            a+=1
            x=greetings()
        else:
            print("Sigue!")

def greetings():
    print("Que quiere hacer?")
    print("1. Abdominales")
    print("2.Informacion")
    print("3.Agregar Ejercicio")
    print("4. Salir:")
    greet=input()#separar, recursion
    count=len(abs)
    if greet == 1:
        x=int(input("Cantidad de ejercicios:"))
        generar_lista(x,count,abs)
        rutina_orden=random.sample(rutina,len(rutina))
        for i in range(len(rutina_orden)):
            print(rutina_orden[i])
        listo()
    elif greet==2:
        print("En proceso")
    elif greet==3:
        print("En proceso")
        #agregar_ejercicio()
    elif greet==4:
        print("Adios")
        os._exit(0)
    else:
        print("incorrecto")
        greetings()

#def agregar_ejercicio():
#    file=open("C:\Users\Diego\Desktop\core.txt","a")
#    x=input("Ejercicio, zona, dificultad:")
#    print(x)
#    for line in file:
#        file.readlines()
#    file.close()

   
base()
