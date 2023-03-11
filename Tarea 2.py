# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 17:42:42 2022

@author: jorge
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as manimation


random.seed(10)
np.random.seed(10)

def bubblesort(lista):
    iterations = 0
    for i in range(len(lista)):
        iterations+=1
        for j in range(0, len(lista) - i - 1):
            iterations+=1
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
    return lista, iterations

def mergesort(lista):
    iterations = 0
    if len(lista) > 1:
        mid = len(lista)//2
        L = lista[:mid]
        R = lista[mid:]
        iterations+=mergesort(L)
        iterations+=mergesort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
            iterations+=1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1
            iterations+=1
  
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
            iterations+=1
            
    return iterations

elementNumArray=[100,200,400,800,1600,3200,6400,12800,25600,51200,102400,204800,204800*2,204800*4]

elementNumArray=[100,200,400,800,1600,3200,6400,12800]
#elementNumArray=np.arange(100,204800,100)
tiemposBi=[]
iteracionesBi=[]
tiemposLi=[]
iteracionesLi=[]

FFMpegWriter = manimation.writers['ffmpeg']

metadata = dict(title='BubbleSort vs MergeSort', artist='Jorge Amaro',comment='Deja tu  like')
writer = FFMpegWriter(fps=24, metadata=metadata)

fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(18,9))
ax1.title.set_text('BubbleSort')
ax2.title.set_text('MergeSort')
ax1.set_ylabel("Consultas")
ax1.set_xlabel("# Elementos")
ax2.set_xlabel("# Elementos")

with writer.saving(fig, "BubbleSortvsMergeSort.mp4", 100):

    plt.ion()
    for idx,elementNum in enumerate(elementNumArray):
        lista=np.sort(np.linspace(0,100000,elementNum))
        
        start=time.time()
        # Almacena el arreglo de datos ordenados
        # res = metodo(lista de python), para convertir numpy arr a lista de python
        # usa lista.tolist()
        r_bubblesort,it=bubblesort(lista.tolist())
        finish=time.time()
        iteracionesBi.append(it)
        tiemposBi.append(finish-start)
        
        start=time.time()
        it=mergesort(lista.tolist())
        finish=time.time()
        iteracionesLi.append(it)
        tiemposLi.append(finish-start)
        
        ax1.plot(elementNumArray[:idx+1], iteracionesLi, 'r-',label='merge')
        ax2.plot(elementNumArray[:idx+1], iteracionesBi, 'b--',label='Bubble')

        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.show(block=False)

        time.sleep(.1)
        for i in range(24):
         writer.grab_frame()

#fig, ax = plt.subplots()
#line1, =ax.plot(elementNumArray,tiempos)
#line1, =ax.plot(elementNumArray,iteraciones)
#plt.show()
