import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()


pages = st.sidebar.selectbox('Pilih Halaman', ['Visualisasi', 'Hypothesis Testing'])
    
if pages == 'Visualisasi' :
    
    with header :
       st.title('Penjualan Supermarket')
       st.text ('Catatan data penjualan di 3 supermarket berbeda')
    with dataset :

        supermarket = pd.read_csv('ss_s1.csv')
    
    if 'number_of_rows' not in st.session_state :
        st.session_state['number_of_rows'] = 2
        st.session_state['type'] = 'Categorical'

    supermarket = pd.read_csv('ss_s1.csv')
    
    
    st.table(supermarket.iloc[:,np.r_[:10,17]].head(st.session_state['number_of_rows']))

    increment = st.button('Tampilkan lebih banyak')
    if increment :
        st.session_state.number_of_rows += 4

    decrement = st.button('Tampilkan lebih sedikit')
    if decrement :
        st.session_state.number_of_rows -= 4

    st.header ('Silahkan pilih data yang ingin dibandingkan : ')
    types = {'Categorical' : ['Product line', 'Branch', 'City', 'Customer type','Gender','Invoice ID'],'Numerical' : ['revenue', 'gross income','Tax 5%', 'Rating']}

    column = st.selectbox('Pilih Data', types[st.session_state['type']])
    
    def handle_click(new_type) :
        st.session_state.type = new_type
    
    type_of_column = st.radio('Silahkan pilih perbandingan yang diinginkan', ['Categorical', 'Numerical'])
    change = st.button('Change', on_click=handle_click, args = [type_of_column])

    if st.session_state['type'] == 'Categorical' :
        dist = pd.DataFrame(supermarket[column].value_counts()).head(50)
        st.bar_chart(dist)
    else :
        st.table(supermarket[column].describe())

    values2 = st.slider(
        'Melihat berdasarkan Rentang Nilai dari Peringkat Supermarket',
        0.0, supermarket.Rating.max(), (0.0, 10.0))
    st.write('Values:' , values2)
    st.write(supermarket[(supermarket.Rating>= values2[0]) & (supermarket.Rating<= values2[1])])
    st.write(supermarket[(supermarket.Rating>= values2[0]) & (supermarket.Rating<= values2[1])].shape)

   


    
else :
        st.title('Hipotesis testing')

        supermarket = pd.read_csv('ss_s1.csv')

        

        with features :
            st.subheader('Rata-rata reneuve dari tipe kostumer normal dan member')
            
            
            chart_data = pd.Series({"Normal": 303, "Member": 312})
            st.bar_chart(chart_data)
            st.subheader('P-value: 0.53')

            

            st.line_chart({"data": [0.005, 0.53]}) #revisi dash nya
        with st.expander("Penjelasan"):
            st.write("""
        dikarenakan P-value yang didapat sebesar 0.53 antara tipe kostumer Normal dengan Member, 
        yang berarti besar dari 0.05 critical value nya 
        Sehingga rata-rata seluruh pemasukan yang didapat dari semua saluran penjualan supermarket 
        yang dibeli tipe kostumer Normal dan Member tidak berbeda secara signifikan. H0 diterima.
        """)
