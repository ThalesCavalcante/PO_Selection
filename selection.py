import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint
import timeit
mpl.use('Agg')

def desenhaGrafico(x, y, nome,nome_label, xl="Entradas", yl="Saídas"):
    plt.plot(x, y, label=nome_label)
    plt.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nome)

def faz_List(size):
    list = []
    while size > 0:
        n = randint(1, size)
        list.append(n)
        size -= 1
    return list

def faz_DList(size):
    list = []
    while size > 0:
        list.append(size)
        size -= 1
    return list

op= []
op2= []

def sort(array):
    operacoes = 0
    for i in range(len(array)):
        min_idx = i 
        for j in range(i+1, len(array)): 
            if array[min_idx] > array[j]: 
                min_idx = j 
                operacoes+=1
                      
        array[i], array[min_idx] = array[min_idx], array[i]
            
    op.append(operacoes)
    
    
size = [10000, 20000, 50000, 100000]
time = []
time2=[]
for s in size:
    list = faz_List(s)
    lista = faz_DList(s)
    time.append(timeit.timeit("sort({})".format(list),setup="from __main__ import sort", number=1))
    time2.append(timeit.timeit("sort2({})".format(lista),setup="from __main__ import sort2", number=1))

    print(s)
    

desenhaGrafico(size, time,'Bubble_Time','lista_aleatória', 'Numbers', 'Time')
desenhaGrafico(size, time2,'Bubble_Time','pior caso', 'Numbers', 'Time')
desenhaGrafico(size, op,'Bubble_Op','lista_aleatoria','Numbers', 'operacoes')
desenhaGrafico(size, op2,'Bubble_Op','pior caso','Numbers', 'operacoes')
