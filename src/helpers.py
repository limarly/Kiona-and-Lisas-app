import streamlit as st


# change background color of the sidebar
def sidebar_color():
    st.markdown(
        """
        <style>
            [data-testid=stSidebar] {
                background-color: #29bdbc;
            }
        </style>
        """, unsafe_allow_html=True)
