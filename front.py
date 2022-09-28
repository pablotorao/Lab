#1/usr/bin/python
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from scipy import signal
fig, ax = plt.subplots()
def rampt(li,ls,a,p):
	t=rang(li,ls,p)
	y  = t*0
	dis=ls-li
	m=a/(ls-dis*2/3-li)
	y[(t<ls- dis*2/3) ] =(t[t<ls-dis*2/3]-li)*m 
	y[(t> ls-dis*2/3)&(t<ls-dis/3) ] = a 
	y[(t>ls- dis/3) ] =(t[t>ls-dis/3]-ls)*-m
	return t,y
def graphdisc(r,y):
	fig, ax = plt.subplots()
	ax.scatter(r,y)
	ax.legend()
	the_plot2.pyplot(fig)
def graphdisc2(r,y,r2,y2):
        fig, ax = plt.subplots()
        ax.scatter(r, y, label="Signal")
        ax.scatter(r2, y2, label="System")
        ax.legend()
        the_plot.pyplot(fig)
def rec(li,ls,a,p):
	t=rang(li-1,ls+1,p)
	y  = t*0
	y[(t> li)& (t< ls) ] = a 
	return t,y
def sen(li,ls,a,f,p):
	t=rang(li,ls,p)
	y = a*np.sin(f*t)
	return t,y
def expo(li,ls,b,a,p):
	t=rang(li,ls,p)
	y=a*(np.exp(b*t))
	return t,y
def trian(li,ls,a,f,p):
	t=rang(li,ls,p)
	y = a*signal.sawtooth(f * t)
	return t,y
def rang(li,ls,p):
        r=np.arange(li,ls,p)
        return r
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
def conv(r,s):
        n=0
        rl=len(r)
        rs=len(s)
        j=n
        i=0
        mult=0
        con=0
        conv=np.zeros(rl+rs)
        while n< rl+rs:
                while j>=0:
                        try:
                                mult=s[i]*r[j]
                                con=con+mult
                                j=j-1
                                i=i+1

                        except:
                                mult=0
                                j=j-1
                                i=i+1
                conv[n]=con
                i=0
                n=n+1
                j=n
                con=0
        return conv

def option_type():
	option_type = st.selectbox(
	'Type',
	('choose','Continuous', 'Discreta',))
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
def type(one,two):
	option1 = st.selectbox(
        'Funcion'+one,
        ('Exponencial Ae^-bt', 'Senoidal', 'Triangular', 'Rectangular', 'Rampa'))
	option2 = st.selectbox(
        'Funcion '+two,
        ('Exponencial Ae^-bt', 'Senoidal', 'Triangular', 'Rectangular', 'Rampa'))
	return option1,option2
def contp(which):
	st.header("Funcion"+': '+which)
	li = st.slider('Limite inferior'+' '+which,-10,10, -5)
	ls = st.slider('Limite superior'+' '+which,-10, 10, 5)
	a = st.slider('Amplitud'+' '+which,0,20, 1)
	f = st.slider('Frecuencia'+' '+which, 0, 100, 5)
	return li, ls, a, f
def contrec(which):
	st.header("Funcion"+': '+which)
	li = st.slider('Limite inferior'+' '+which,-10,10, -5)
	ls = st.slider('Limite superior'+' '+which,-10, 10, 5)
	a = st.slider('Amplitud'+' '+which,0,20, 1)
	return li,ls,a
def contexp(which):
	st.header("Funcion"+': '+which)
	li = st.slider('Limite inferior'+' '+which,-10,10, -5)
	ls = st.slider('Limite superior'+' '+which,-10, 10, 5)
	b = st.slider('b'+' '+which,0,20, 1)
	a = st.slider('A'+' '+which,0,20, 1)
	return li, ls, a, b
col1, col2 = st.columns(2)
with col1:	
	if option_type== 'Continuous':
		a,b =type(one,two)
		if a== 'Senoidal':
			li , ls, a, f = contp(one)
			t,y=sen(li,ls,a,f,p1)
		if a== 'Triangular':
			li, ls, a, f=contp(one)
			t,y=trian(li,ls,a,f,p1)
		if a=='Rectangular':
			li,ls,a = contrec(one)
			t,y=rec(li,ls,a,p1)	
		if a=='Rampa':
			li,ls,a=contrec(one)
			t,y=rampt(li,ls,a,p1)
		if a=='Exponencial Ae^-bt':
			li, ls, a , bex = contexp(one)
			t,y=expo(li,ls,bex,a,p1)
		if b== 'Senoidal':
			li2 , ls2, a2, f2 = contp(two)
			t2,y2=sen(li2,ls2,a2,f2,p1)
			print(t2)
		if b== 'Triangular':
			li2,ls2,a2,f2=contp(two)
			t2,y2=trian(li2,ls2,a2,f2,p1)
		if b=='Rectangular':
			li2,ls2,a2=contrec(two)
			t2,y2=rec(li2,ls2,a2,p1)    
		if b=='Rampa':
			li2,ls2,a2=contrec(two)
			t2,y2=rampt(li2,ls2,a2,p1)
		if b=='Exponencial Ae^-bt':
			li2, ls2, a2, b2 = contexp(two)
			t2,y2=expo(li2,ls2,b2,a2,p1)
			print(t2)
	if option_type== 'Discreta':
		a,b =type(one,two)
		if a== 'Senoidal':
			li , ls, a, f = contp(one)
			p2=1/(4*f)
			t,y=sen(li,ls,a,f,p2)
		if a== 'Triangular':
			li, ls, a, f=contp(one)
			p2=1/(4*f)
			t,y=trian(li,ls,a,f,p2)
		if a=='Rectangular':
			li,ls,a=contrec(one)
			p2=0.5
			t,y=rec(li,ls,a,p2)     
		if a=='Rampa':
			li,ls,a=contrec(one)
			p2=0.5
			t,y=rampt(li,ls,a,p2)
		if a=='Exponencial Ae^-bt':
			li, ls, a , bex = contexp(one)
			p2=0.2
			t,y=expo(li,ls,bex,a,p2)
		if b== 'Senoidal':
			li2 , ls2, a2, f2 = contp(two)
			p2=1/(4*f2)
			t2,y2=sen(li2,ls2,a2,f2,p2)
		if b== 'Triangular':
			li2,ls2,a2,f2=contp(two)
			p2=1/(4*f2)
			t2,y2=trian(li2,ls2,a2,f2,p2)
		if b== 'Rectangular':
			li2,ls2,a2=contrec(two)
			p2=0.5
			t2,y2=rec(li2,ls2,a2,p2)   
		if b=='Rampa':
			li2,ls2,a2=contrec(two)
			p2=0.5
			t2,y2=rampt(li2,ls2,a2,p2)

		if b=='Exponencial Ae^-bt':
			li2, ls2, a2, b2 = contexp(two)
			p2=0.2
			t2,y2=expo(li2,ls2,b2,a2,p2)

with col2:
	if st.button('Graficar '): 
		the_plot=st.pyplot(fig)
		if option_type== 'Continuous':
			try:
				graph(t,y,t2,y2)
			except:
				pass
		if option_type== 'Discreta':
                        try:
                                graphdisc2(t,y,t2,y2)
                        except:
                                pass
	if st.button('conv'):
		if option_type== 'Continuous':
			the_plot2=st.pyplot(fig)
			the_plot=st.pyplot(fig)	
			a=conv(y,y2)
			lr1=len(t2)
			lr=len(t)
			r1=lr1+lr
			r1=r1*0.04
			ta=np.arange(t2[0]+t[0],r1+t2[0]+t[0],0.04)
			tb=ta
			t=t-li2-li
			t=-t
			i=1
			desp=t2[lr1-1]-t[lr-1]
			r1=r1/10
			desp=desp/10    
			for i in range(11):
				rg=t+desp*i
				b=conv(y,y2)
				graph(rg,y,t2,y2)
				ta2=np.arange(t2[0]+t[0],r1*i+t2[0]+0.04+t[0],0.04)
				lt1=len(ta2)
				b[ta>ta2[lt1-1]]=0
				graph2(ta,b) 
			graph2(tb,a)
		if option_type== 'Discreta':
                        the_plot2=st.pyplot(fig)
                        the_plot=st.pyplot(fig) 
                        a=conv(y,y2)
                        lr1=len(t2)
                        lr=len(t)
                        r1=lr1+lr
                        r1=r1*p2
                        ta=np.arange(t2[0]+t[0],r1+t2[0]+t[0],p2)
                        tb=ta
                        t=t-li2-li
                        t=-t
                        i=1
                        desp=t2[lr1-1]-t[lr-1]
                        r1=r1/10
                        desp=desp/10
                        try:
                                for i in range(11):
                                        rg=t+desp*i
                                        b=conv(y,y2)
                                        graphdisc2(rg,y,t2,y2)
                                        ta2=np.arange(t2[0]+t[0],r1*i+t2[0]+0.04+t[0],0.04)
                                        lt1=len(ta2)
                                        b[ta>ta2[lt1-1]]=0
                                        graphdisc(ta,b) 
                        except:
                                pass
                        graphdisc(tb,a)



