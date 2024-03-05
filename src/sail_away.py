import streamlit as st
import base64
import time


# Setting up some constants for styling
line_height_sidebar = "100%"
line_height_sail = "130%"
line_height_sail_title = "160%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_sail = "1.5vw"
font_size_sail_title = "2vw"

# List of sections until current page
sections = ["Introduction",
            "Eisenhower First Try",
            "Eisenhower Method",
            "Eisenhower Applied",
            "Pirate Encounter",
            "Cornell Method",
            "Blurting Method",
            "Pomodoro First Try",
            "Pomodoro Method",
            "Pomodoro Applied",
            "<strong> Sail Away</strong>"]


# Function to autoplay the sail away audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


# Function to render the Sail Away page
def render_sail_away():
    # Creating a progress bar in the sidebar
    progress_100 = st.sidebar.progress(0)
    for percent_complete_100 in range(0, 101):
        time.sleep(0.01)
        progress_100.progress(percent_complete_100)

    # Displaying sections in the sidebar using a loop
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(
                f"""
                <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">
                    {section}
                </p>
                """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(
                f"""
                <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                    {section}
                </p>
                """, unsafe_allow_html=True)

    # Getting the player's name
    player_name = st.session_state.player_name
    if player_name is not None:
        player_name = player_name.upper()

    # Creating a layout with two columns for image of a ship and congratulating of player for finishing the game
    col1, col2 = st.columns((5, 3), gap="large")
    with col1:
        st.image("pictures/ship.png")
    with col2:
        st.markdown(
            f"""
            <p style="line-height:{line_height_sail_title}; font-size: {font_size_sail_title};">
                WELL DONE {player_name}!
            </p> 
            <p style="line-height:{line_height_sail}; font-size: {font_size_sail};">
                You can now call yourself<br>CAPTAIN PRODUCTIVITY!!!<br><br>Sail home safely!
            </p> 
            """, unsafe_allow_html=True)
        # Button to let balloons fly
        if st.button("Click here to celebrate!"):
            st.balloons()
        st.image("pictures/shelly_captain.png", width=300)

    # Layout with two columns
    col_a, col_b = st.columns((8, 1))
    with col_a:
        autoplay_audio("audio/Orinoco-Flow.mp3")
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to restart or exit the game
        if st.button("Start again"):
            st.session_state.place = "introduction"
            st.rerun()
        if st.button("Exit the game"):
            st.session_state.place = "exit"
            st.rerun()
