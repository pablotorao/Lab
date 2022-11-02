#1/usr/bin/python
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from scipy import signal
fig, ax = plt.subplots()
def graph3(r,y):
	fig, ax = plt.subplots() #graph para cont (los invocas en el boton)
	ax.plot(r,y)
	ax.legend()
	the_plot3.pyplot(fig)
def graph(r,y,r2,y2):
        fig, ax = plt.subplots()
        ax.plot(r, y, label="Signal") #graph para serie
        ax.plot(r2, y2, label="System")
        ax.legend()
        the_plot.pyplot(fig)
def graph2(r,y):
	fig, ax = plt.subplots()
	ax.plot(r, y, label="Convolution") #graph para cont
	ax.legend()
	the_plot2.pyplot(fig)
def graph2disc(r,y):
	fig, ax = plt.subplots()
	ax.scatter(r, y, label="Convolution") #graph para disc
	ax.legend()
	the_plot2.pyplot(fig)
def graphdisc(r,y):
	fig, ax = plt.subplots()
	ax.scatter(r, y, label="Convolution") #graph para disc
	ax.legend()
	the_plot1.pyplot(fig)
def graph3disc(r,y):
	fig, ax = plt.subplots()
	ax.scatter(r, y, label="Convolution") #graph para disc
	ax.legend()
	the_plot3.pyplot(fig)
def graph1(r,y):
	fig, ax = plt.subplots()
	ax.plot(r, y, label="Convolution") #graph para cont
	ax.legend()
	the_plot1.pyplot(fig)
def option_type():
	option_type = st.selectbox(
	'Type',
	('En que lo puedo ayudar?','Serie', 'Transformada',))
	return option_type
ones='1.'
one='1'
two='2'
three= '3'
p1=0.04
option_type=option_type()
def graph(r,y,r2,y2):
	fig, ax = plt.subplots()
	ax.plot(r, y, label="Signal")
	ax.plot(r2, y2, label="System")
	ax.legend()
	the_plot.pyplot(fig)
def type(one):
	option1 = st.selectbox(
        'Funcion'+one,
        ('Exponencial Ae^-bt', 'Senoidal', 'Triangular', 'Rectangular', 'Rampa1','Rampa2','Rampa3')) #lo que cambies aqui toca cambiarlo en los if de abajo
	return option1
def discorcont(one):
	option2 = st.selectbox(
        'Funcion'+one,
        ('Discreta','Continua')) #lo que cambies aqui toca cambiarlo en los if de abajo
	return option2

def contrec(which):

	st.header("Funcion"+': '+which)
	li = st.slider(' Periodo'+' '+which,-10,10, -5)
	a = st.slider('Amplitud'+' '+which,-20,20, 1)
	return li,a

col1, col2 = st.columns(2)
with col1:	
	if option_type== 'Serie':
		a =type(one)
		if a== 'Senoidal':  #a estos if me referia
			li , a = contrec(one)

		if a== 'Triangular':
			li,a =contrec(one)

		if a=='Rectangular':
			li,a = contrec(one)

		if a=='Rampa3':
			li,a=contrec(one)

		if a=='Rampa1':
			li,a=contrec(one)
		if a=='Rampa2':
			li,a=contrec(one)
		if a == 'Exponencial Ae^-bt':
			li, a= contrec(one)
	if option_type== 'Transformada':
		c = discorcont(one)
		if c=='Discreta':
			contrec(one)
			contrec(two)
			contrec(three)
			st.header('------------------------------')
			nm1 = st.slider('# de muestras', -20, 20, 1)
			fm = st.slider(' Frecuencia de muestreo', -10, 10, -5)
		else:
			contrec(one)
			contrec(two)
			contrec(three)
			st.header('------------------------------')
			fm = st.slider(' Frecuencia de muestreo', -10, 10, -5)
with col2:
	if st.button('Graficar '): 
		if option_type== 'Serie':
			try:
				the_plot=st.pyplot(fig)
			except:
				pass
		if option_type== 'Transformada':
				try:
					if c == 'Discreta':
						the_plot3=st.pyplot(fig)
						the_plot1=st.pyplot(fig)
						the_plot2=st.pyplot(fig)
					else:
						the_plot3 = st.pyplot(fig)
						the_plot1 = st.pyplot(fig)
						the_plot2 = st.pyplot(fig)
				except:

					pass

