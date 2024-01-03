import matplotlib.pyplot as plt
import streamlit as st
import cv2
import dataexploration as dexpl

def exec_page1(self):
  data = dexpl.init_raw_dataset()
  st.header('Exploration et Pré-Traitement')

  tab1, tab2, tab3 , tab4 = st.tabs(["Data structure","Diagnostics", "Dog", "Preprocessing"])

  with tab1:
    st.image(cv2.imread('arborescence_data2.png'),caption = 'Jeu de donnée brut')
    

    file = dexpl.any_random_file(data)  
    fig = plt.figure(figsize=(16,8))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax1.set_axis_off()
    ax2.set_axis_off()
    ax1.imshow(dexpl.load(file), cmap='gray')
    ax2.imshow(dexpl.load_mask(file), cmap='gray')
    st.pyplot(fig)
    

  with tab2:
     st.image(cv2.imread('Data pie.png'),caption = 'Classes du Jeu de donnée brut')
     st.image(cv2.imread('Mean Class.png'),caption = 'Image moyenne par classes')

  with tab3:
     st.header("An owl")
     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

  with tab4:
     st.header("A monsters")
     st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

  
  
