import numpy as np
import statistics as stt
import scipy.stats as sc
import streamlit as st
import soundfile as sf
import re

def operaciones(info,file):
    mean = stt.mean(info)
    median = stt.median(info)
    desviacions = stt.pstdev(info)
    desviacionabs = np.mean(np.absolute(info - np.mean(info)))
    cuar1 = np.quantile(info,.25)
    cuar2 = np.quantile(info,.75)
    rincuar = cuar2-cuar1
    simetria = sc.skew(info)
    courtois = sc.kurtosis(info)
    coefdesv = desviacions/mean
    out = 0
    for inf in info:
        out = abs(inf) ** 2 + out
    potencia = out * (1 / (2 * len(info) + 1))
    file=file.name
    file= re.sub('[^S01234567]', '', file)
    return mean, median, desviacions, desviacionabs, cuar2, cuar1, rincuar, simetria, courtois, coefdesv, potencia,file


option = st.selectbox(
    'Tipo de archivo',
    ('En que lo puedo ayudar?','CSV', 'WAV'))
if option == 'CSV':
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    if st.button('Analizar'):
        if uploaded_files is not None:
            n = 0
            datav = [0] * len(uploaded_files)
            dataft = [0] * len(uploaded_files)
            dataft2 = [0] * len(uploaded_files)
            datamult = [0] * len(uploaded_files)
            t = [0] * len(uploaded_files)

            ft = [0] * len(uploaded_files)
            fs1=10
            for uploaded_file in uploaded_files:
                inf2 = str(uploaded_file.read(), 'utf-8')
                text = inf2.split("\n")
                del text[-1]

                data = [0] * len(text)
                i = 0
                for number in text:
                    data[i] = float(number)
                    i = i + 1
                vector = np.array(data)
                print(uploaded_file.name)
                #numerodedatos=len(vector)
                ft1 = np.fft.fft(vector)
                ft1=ft1.real
                ft[n] = ft1.real
                t1=np.fft.fftfreq(len(vector)) * fs1
                t[n] = np.fft.fftfreq(len(vector)) * fs1
                datav[n]=operaciones(vector,uploaded_file)
                dataft[n]=operaciones(ft1,uploaded_file)
                dataft2[n]=operaciones(t1,uploaded_file)
                print(datav[n])
                #datamult[n]= dataft2[n]*dataft[n]
               # print(datav[n])
                #print(dataft[n])
                #print(dataft2[n])
                n=n+1


                #print('-------------------------------------------------------------------------------------------------------')
        else:
            pass
else:
    uploaded_files = st.file_uploader("Choose a WAV file",accept_multiple_files=True)
    if st.button('Analizar'):
        if uploaded_files is not None:
            n = 0
            datav = [0] * len(uploaded_files)
            dataft = [0] * len(uploaded_files)
            for uploaded_file in uploaded_files:
                #vector, fs1 = sf.read(uploaded_files, dtype='float64')

                info, fs = sf.read(uploaded_file, dtype='float32')
                #print(info[20])
                print('hola')
            #    print(uploaded_file.read())
                #inf2 = str(uploaded_file.read(), 'utf-8')
             #   text = info.split("\n")
              #  del text[-1]
               # data = [0] * len(text)
                #i = 0
                #for number in text:
                 #   data[i] = float(number)
                   # i = i + 1
                vector=np.array(info)
                #print(vector)
                ft = np.fft.fft(vector)
                ft = ft.real


                datav[n] = operaciones(vector,uploaded_file)
                dataft[n] = operaciones(ft)
                #print(datav[n])
                #print(dataft[n])
                n = n + 1
            #print(operaciones(vector))
            #print(operaciones(ft))
        else:
            pass
#print(datav[0][1])
def sanita(uploaded_files,datav):
    numerodedatos=len(uploaded_files)
    longlist=len(datav[0])
    media=[0]*longlist
    sum=[0]*longlist
    longlist=longlist-1
    #print(numerodedatos)
    #print(longlist)
    for x in range(longlist):
        suma=1
        mediadat=0
        for m in range(numerodedatos):
            mediadat=datav[m][x]
            #suma=(mediadat-suma)
            #error=(suma)*100/mediadat
            suma=mediadat/suma
            error=suma
        print('-----------------------------------error--------------------------------------------------------------')
        print(error)
            #print(x)
        sum[m] =  suma
        media[x]=suma/numerodedatos
    return media,sum
print(datav)
print('-------------------------------------------------------------------------------------------------------')
nof, sif=sanita(uploaded_files,datav)
#print(uploaded_files)
print('-------------------------------------------------------------------------------------------------------')








#mean, median, desviacions, desviacionabs, cuar2, cuar1, rincuar, simetria, courtois, coefdesv, potencia = operaciones(info)





