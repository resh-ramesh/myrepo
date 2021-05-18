import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns

#st.set_option('deprecation.showPyplotGlobalUse',False)
df=pd.read_csv('titanic.csv')
from PIL import Image
img=Image.open("titanic.jpg")
st.image(img,width=300)
st.title("Details Of Titanic Passengers")
tips=df.head(5)
tips
st.text("Name of passengers who did not survive ")
man=df.loc[(df.Survived ==0)]
man
st.text("Name of passengers who were survived and are male ")
man=df.loc[(df.Survived ==1) & (df.Sex=='male')]
man.Name
st.text("Name of passengers who were survived and are female ")
w=df.loc[(df.Survived ==1) & (df.Sex=='female')]
w.Name
st.text("Name of passengers who were children ")
c=df.loc[(df.Survived ==1) & (df.Age <15)]
c.Name
st.text("Number of Passengers in each Class")
no=df.groupby('Pclass')
n=no.size()
n
clas=st.selectbox("To get the details of Passengers ,select PassengerClass",[1,2,3])
c1=no.get_group(clas)
c1

st.header("visualisation using seaborn")
st.subheader("BarPlot")
tips.plot(kind='bar')
st.pyplot()
#joinplot
st.subheader("joinplot")
sns.jointplot(x='Pclass',y='Fare',data=tips,kind='scatter')
st.pyplot()
#pairplot
st.subheader("pairplot")
sns.pairplot(tips,hue='Sex',palette='rainbow')
st.pyplot()
sns.pairplot(tips,hue='Survived',palette='rainbow')
st.pyplot()
#correation
st.subheader("heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()

