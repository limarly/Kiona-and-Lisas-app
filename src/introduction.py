import streamlit as st


# Function to render the introduction
def render_introduction():
    # Creating a progress bar in the sidebar; set to no progress
    st.sidebar.progress(0)

    # Markdown to display the current page in the sidebar
    st.sidebar.markdown(
                f"""
                <p style="line-height: 100%; font-size: 1.3vw;">
                    <strong>Introduction</strong>
                </p>
                """, unsafe_allow_html=True
    )

    # Retrieving the player name from session state
    player_name = st.session_state.player_name
    if player_name is not None:
        player_name = player_name.upper()

    # Layout with two columns to display the title and logo
    col1, col2 = st.columns((7, 1))
    col1.title("PIERATS - Productivity Island Expedition")
    col2.image("pictures/logo.png")

    # Layout with four columns; 1 and 4 are just for lay outing reasons
    col1, col2, col3, col4 = st.columns((1, 4, 4, 1), gap="small")
    # display picture of shelly with a speech bubble
    with col2:
        st.image("pictures/shelly_speech.png")

    # Markdown to greet the player, getting the name, introduce them to the game
    with col3:
        st.markdown(
            f""" <br><br>
            <p style="line-height:130%; font-size:2vw;">AHOI {player_name}! ⛵️️︎</p>
            <p style="line-height:150%; font-size: 1.5vw;">
                I am Productivishelly, but you can call me Shelly!<br>I will join you on your journey today where you 
                will learn about time management and productivity while playing fun mini games!<br>Click on the button 
                below to start your adventure of the productivity island expedition. <br><br>I'll see you there!
            </p>
            """, unsafe_allow_html=True
        )

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Let's start | >>"):
            st.session_state.place = "map_1"
            st.rerun()
