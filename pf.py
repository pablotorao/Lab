import matplotlib.pyplot as plt
import numpy as np
import statistics as stt
import scipy.stats as sc
import streamlit as st
import soundfile as sf
import re
import librosa
from scipy import signal
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
def ES(st):
    l=len(st)
    vt=[0]*l
    for i in range(l):
        if st[i]<=0:

            aux=0
        else:
            aux=-(st[i]**2)*np.log(st[i]**2)
        vt[i]=aux
    print(vt)
    #xbarra=np.mean(vt)
    return vt
def operaciones2(info):
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

    return mean, median, desviacions, desviacionabs, cuar2, cuar1, rincuar, simetria, courtois, coefdesv, potencia
def outp(datos,data):
    st.line_chart(data)
    mean=st.write('Mean: '+str(datos[0]))
    median=st.write('Median: '+str(datos[1]))
    desviacions=st.write('Desvia: '+str(datos[2]))
    desviacionabs=st.write('Desviabs:'+str(datos[3]))
    cuar2=st.write('Cuar 2: '+str(datos[4]))
    cuar1=st.write('Cuar 1: '+str(datos[5]))
    rincuar=st.write('Rincuar: '+str(datos[6]))
    simetria=st.write('Symetry: '+str(datos[7]))
    courtois=st.write('Kourtosis: '+str(datos[8]))
    coefdesv=st.write('CoefDesv: '+str(datos[9]))
    potencia=st.write('Power: '+str(datos[10]))


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
def intento():
    if st.button('Analizar sensor'):
        if option==selet[0]:
            outp(datav[0])
        if option==selet[1]:
            outp(datav[1])


option = st.selectbox(
    'Tipo de archivo',
    ('CSV', 'WAV'))
if option == 'CSV':
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    if st.button('Analizar'):
        if uploaded_files is not None:
            n = 0
            datav = [0] * len(uploaded_files)
            dataft = [0] * len(uploaded_files)
            dataft2 = [0] * len(uploaded_files)
            datavector = [0] * len(uploaded_files)
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
                datavector[n]=vector

                ft1 = np.fft.fft(vector)
                ft1=ft1.real
                ft[n] = ft1.real
                t1=np.fft.fftfreq(len(vector)) * fs1
                t[n] = np.fft.fftfreq(len(vector)) * fs1
                datav[n]=operaciones(vector,uploaded_file)
                dataft[n]=operaciones(ft1,uploaded_file)
                print(datav[n])


                n=n+1

        else:
            pass
else:
    uploaded_files = st.file_uploader("Choose a WAV file",accept_multiple_files=True)
    if st.button('Analizar'):
        if uploaded_files is not None:
            n = 0
            datav = [0] * len(uploaded_files)
            dataft = [0] * len(uploaded_files)
            datavector = [0] * len(uploaded_files)
            for uploaded_file in uploaded_files:
                info, fs = sf.read(uploaded_file, dtype='float32')
                vector=np.array(info)
                ft = np.fft.fft(vector)
                ft = ft.real
                datav[n] = operaciones(vector,uploaded_file)
                dataft[n] = operaciones(ft,uploaded_file)
                datavector[n] = vector
                n = n + 1
        else:
            pass
try:
    selet=[0]*len(datav)
    n=0
    for dato in datav:
        if dato[-1]=='1S0':
            if 300<dato[-2]<360:
                st.title('!!!!!!!!!!!!!!!!!!!!Rock!!!!!!!!!!!!!!!!!!')
            else:
                st.title('!!!!!!!!!!!!!!!!!!!!!!PAPER!!!!!!!!!!!!!!!!!!!!!')
        selet[n]=dato[-1]
        n=n+1
    ndatos=len(datavector[1])
    numerodedatos = len(uploaded_files)
    media = [0] * ndatos
    for x in range(ndatos):
        suma = 0
        #mediadat = 0
        for m in range(numerodedatos):
            mediadat = int(datavector[m][x])
            # suma=(mediadat-suma)
            # error=(suma)*100/mediadat
            suma = mediadat+suma
            error = suma

        media[x] = suma
    salidita=operaciones2(media)
    fourier=np.fft.fft(media)
    fourier=fourier.real
    t1=np.fft.fftfreq(len(vector)) * 10
    salidita2=operaciones2(fourier)
    col1, col2= st.columns(2)
    holi=ES(media)
    holi2 = ES(fourier)

    with col1:
        with st.expander('Signal data'):
            outp(salidita,media)
        with st.expander('Signal Shannon'):
            st.line_chart(holi)
    with col2:
        with st.expander('Fourier data'):
            outp(salidita2, fourier)
        with st.expander('Fourier Shannon'):
            st.line_chart(holi2)
    media=np.array(media)
    f, t, Sxx = signal.spectrogram(media, 500)
    plt.figure(figsize=(8,10))
    plt.pcolormesh(t, f, Sxx, shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time ')
    plt.savefig('.desesperacion.png')
    plt.show()
    with st.expander('Spectogram'):
        st.image('.desesperacion.png')

except:

    pass








