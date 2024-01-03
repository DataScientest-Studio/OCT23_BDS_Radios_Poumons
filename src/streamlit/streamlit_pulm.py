import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from str_page0 import exec_page0
from str_page1 import exec_page1
from str_page2 import exec_page2
from str_page3 import exec_page3
from str_page4 import exec_page4


st.title("Oct23 Bootcamp DS  Radios pulmonaires ")
st.sidebar.title("Sommaire")
pages=["Introduction", "Exploration et Pré Traitement","Modelisation Approche directe","Approfondissement","Conclusion"]
page=st.sidebar.radio("Aller vers", pages)

if page == pages[0] :
  exec_page0(st)
 

if page == pages[1] :
  exec_page1(st)



if page == pages[2] :
  exec_page2(st)


if page == pages[3] :
  exec_page3(st)



if page == pages[4] :
  exec_page4(st)
