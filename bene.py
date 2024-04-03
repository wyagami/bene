import streamlit as st
from streamlit_option_menu import option_menu

st.set_option('deprecation.showPyplotGlobalUse', False)


# Interface do Streamlit
with st.sidebar:
    st.sidebar.subheader('BENE (Beneficios)')
    st.sidebar.markdown("versão 1.0")

    choose = option_menu("Menu", ["Sobre", "Login", "Cadastro", "Serviços", "Contato"],
                         icons=['house', 'camera fill', 'kanban', 'person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
