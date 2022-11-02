#1/usr/bin/python
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from scipy import signal
fig, ax = plt.subplots()
def graphdisc(r,y):
	fig, ax = plt.subplots()
	ax.plot(r,y)
	ax.legend()
	the_plot3.pyplot(fig)
def graph(r,y,r2,y2):
        fig, ax = plt.subplots()
        ax.plot(r, y, label="Signal")
        ax.plot(r2, y2, label="System")
        ax.legend()
        the_plot.pyplot(fig)
def graph2(r,y):
	fig, ax = plt.subplots()
	ax.plot(r, y, label="Convolution")
	ax.legend()
	the_plot2.pyplot(fig)
def option_type():
	option_type = st.selectbox(
	'Type',
	('En que lo puedo ayudar?','Serie', 'Transformada',))
	return option_type
one='1'
two='2'
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
			li,ls,a=contrec(one)

		if a=='Rampa1':
			li,a=contrec(one)
		if a=='Rampa2':
			li,a=contrec(one)
		if a == 'Exponencial Ae^-bt':
			li, a= contrec(one)
	if option_type== 'Transformada':
		contrec(one)
with col2:
	if st.button('Graficar '): 
		if option_type== 'Serie':
			try:
				the_plot=st.pyplot(fig)
			except:
				pass
		if option_type== 'Transformada':
				try:
					the_plot3=st.pyplot(fig)
					the_plot=st.pyplot(fig)
					the_plot2=st.pyplot(fig)
				except:

					pass

