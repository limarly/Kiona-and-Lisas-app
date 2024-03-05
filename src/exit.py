import streamlit as st


# Function to render the exit message
def render_exit():

    # Creating three columns for layout
    col1, col2, col3 = st.columns((1, 5, 1))

    # Display the logo banner and the exit message inside the middle column (col2)
    with col2:
        st.markdown(
            f""" 
            <p style="font-family: serif; font-size:2vw; text-align:center;">
                Thanks for playing!<br>See you next time ☺︎<br><br>You can close the window now.<br>
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/logo_banner.png")
