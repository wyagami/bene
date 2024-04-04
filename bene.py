import streamlit as st
from streamlit_option_menu import option_menu

st.set_option('deprecation.showPyplotGlobalUse', False)



# Interface do Streamlit
with st.sidebar:
    st.image('Calculadora.jpeg', width=120)

    st.sidebar.subheader('CALCULADORA DE BENEFICIOS')
    st.sidebar.markdown("versão 1.1")

    choose = option_menu("Menu", ["Sobre", "Bolsa Familia", "Cestas Basicas", "Auxilio Leite", "Fraldas"],
                         icons=['house', 'camera fill', 'kanban', 'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == "Sobre":
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Sobre</p>', unsafe_allow_html=True)
    st.markdown('CALCULADORA DE BENEFICIOS')
    st.markdown('')
    st.markdown('''
                A "Calculadora de Benefícios" é uma aplicação ou ferramenta projetada para ajudar indivíduos a determinar os benefícios financeiros ou assistenciais a que têm direito com base em certos critérios específicos. Esses critérios podem incluir idade, estado civil, renda, número de dependentes, entre outros fatores relevantes.

                Funcionalidades Principais:

                Cálculo de Benefícios: A principal funcionalidade da calculadora é calcular os benefícios disponíveis para um determinado usuário com base nas informações fornecidas. Isso pode incluir benefícios previdenciários, benefícios assistenciais do governo, subsídios, abonos, entre outros.

                Entrada de Dados: A calculadora permite que o usuário insira informações relevantes, como renda familiar, 
                número de dependentes, entre outros. Essas informações são essenciais para determinar os benefícios aos quais o usuário pode ter direito.                
                ''')
elif choose == "Bolsa Familia":
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Bolsa Familia</p>', unsafe_allow_html=True)
    st.text('Valor Base por pessoa: 218,00')
    st.text('Valor Minimo: 600,00')
    st.text('Salário Minimo: 1412,00')
    sal_minimo = 1412.00
    base = 218.00
    minimo = 600.00
    renda = st.number_input('Renda da Familia')
    n_pessoas = st.number_input('Numero de Pessoas',min_value=1)
    gestantes = st.number_input('Numero de Gestantes',min_value=0)

    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(10)

    with col1:
        idade_1 = st.number_input('Idade',min_value=0,key=1)
    with col2:
        idade_2 = st.number_input('Idade',min_value=0,key=2)
    with col3:
        idade_3 = st.number_input('Idade',min_value=0,key=3)
    with col4:
        idade_4 = st.number_input('Idade',min_value=0,key=4)
    with col5:
        idade_5 = st.number_input('Idade',min_value=0,key=5)
    with col6:
        idade_6 = st.number_input('Idade',min_value=0,key=6)
    with col7:
        idade_7 = st.number_input('Idade',min_value=0,key=7)
    with col8:
        idade_8 = st.number_input('Idade',min_value=0,key=8)
    with col9:
        idade_9 = st.number_input('Idade',min_value=0,key=9)
    with col10:
        idade_10 = st.number_input('Idade',min_value=0,key=10)
    t=0
    if st.button("Calcular"):
        if idade_1 > 0:
            t += 1
        if idade_2 > 0:
            t += 1
        if idade_3 > 0:
            t += 1
        if idade_4 > 0:
            t += 1
        if idade_5 > 0:
            t += 1
        if idade_6 > 0:
            t += 1
        if idade_7 > 0:
            t += 1
        if idade_8 > 0:
            t += 1
        if idade_9 > 0:
            t += 1
        if idade_10 > 0:
            t += 1
        if t != n_pessoas:
            st.error('O numero total de pessoas não confere !')
        else:
            st.text('Renda percapita: ' + str(renda/n_pessoas))
            if renda/n_pessoas <= base:
                st.markdown('BENEFICIOS DA FAMILIA')
                t1 = t2 = t3 = t4 = t5 = t6 = t7 = t8 = t9 = t10 =0
                if idade_1 > 0 and idade_1 < 7 and renda/n_pessoas <= base:
                    t1 = 150.00
                if idade_1 > 0 and idade_1 >= 7 and idade_1 <= 15 and renda/n_pessoas <= base:
                    t1 = 50.00
                if idade_2 > 0 and idade_2 < 7 and renda/n_pessoas <= base:
                    t2 = 150.00
                if idade_2 > 0 and idade_2 >= 7 and idade_2 <= 15 and renda/n_pessoas <= base:
                    t2 = 50.00
                if idade_3 > 0 and idade_3 < 7 and renda/n_pessoas <= base:
                    t3 = 150.00
                if idade_3 > 0 and idade_3 >= 7 and idade_3 <= 15 and renda/n_pessoas <= base:
                    t3 = 50.00
                if idade_4 > 0 and idade_4 < 7 and renda/n_pessoas <= base:
                    t4 = 150.00
                if idade_4 > 0 and idade_4 >= 7 and idade_4 <= 15 and renda/n_pessoas <= base:
                    t4 = 50.00
                if idade_5 > 0 and idade_5 < 7 and renda/n_pessoas <= base:
                    t5 = 150.00
                if idade_5 > 0 and idade_5 >= 7 and idade_5 <= 15 and renda/n_pessoas <= base:
                    t5 = 50.00
                if idade_6 > 0 and idade_6 < 7 and renda/n_pessoas <= base:
                    t6 = 150.00
                if idade_6 > 0 and idade_6 >= 7 and idade_6 <= 15 and renda/n_pessoas <= base:
                    t6 = 50.00
                if idade_7 > 0 and idade_7 < 7 and renda/n_pessoas <= base:
                    t7 = 150.00
                if idade_7 > 0 and idade_7 >= 7 and idade_7 <= 15 and renda/n_pessoas <= base:
                    t7 = 50.00
                if idade_8 > 0 and idade_8 < 7 and renda/n_pessoas <= base:
                    t8 = 150.00
                if idade_8 > 0 and idade_8 >= 7 and idade_8 <= 15 and renda/n_pessoas <= base:
                    t8 = 50.00
                if idade_9 > 0 and idade_9 < 7 and renda/n_pessoas <= base:
                    t9 = 150.00
                if idade_9 > 0 and idade_9 >= 7 and idade_9 <= 15 and renda/n_pessoas <= base:
                    t9 = 50.00
                if idade_10 > 0 and idade_10 < 7 and renda/n_pessoas <= base:
                    t10 = 150.00
                if idade_10 > 0 and idade_10 >= 7 and idade_10 <= 15 and renda/n_pessoas <= base:
                    t10 = 50.00
                st.text('Idade: ' + str(idade_1) + ' Valor: ' + str(t1))
                st.text('Idade: ' + str(idade_2) + ' Valor: ' + str(t2))
                st.text('Idade: ' + str(idade_3) + ' Valor: ' + str(t3))        
                st.text('Idade: ' + str(idade_4) + ' Valor: ' + str(t4))
                st.text('Idade: ' + str(idade_5) + ' Valor: ' + str(t5))
                st.text('Idade: ' + str(idade_6) + ' Valor: ' + str(t6))
                st.text('Idade: ' + str(idade_7) + ' Valor: ' + str(t7))
                st.text('Idade: ' + str(idade_8) + ' Valor: ' + str(t8))
                st.text('Idade: ' + str(idade_9) + ' Valor: ' + str(t9))
                st.text('Idade: ' + str(idade_10) + ' Valor: ' + str(t10))
                st.text('Gestante: ' + str(gestantes*50.00) )
                st.markdown('TOTAL DOS BENEFICIOS: ' + str(t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+minimo+(gestantes*50.00)))
            elif renda/n_pessoas > base and renda <= sal_minimo:
                st.markdown('PROCURE O CRAS !!!')


elif choose == "Cestas Basicas":
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Cestas Basicas</p>', unsafe_allow_html=True)
elif choose == "Auxilio Leite":
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Auxilio Leite</p>', unsafe_allow_html=True)
elif choose == "Fraldas":
    st.markdown(""" <style> .font {
    font-size:25px ; font-family: 'Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Fraldas</p>', unsafe_allow_html=True)

