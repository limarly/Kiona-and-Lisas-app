import streamlit as st
import time

# import definitions from source files
from src.helpers import sidebar_color
from src.map import (render_map_1, render_map_2, render_map_3, render_map_4, render_map_5, render_map_6, render_map_7,
                     render_map_8, render_map_9)
from src.backpack import (render_backpack_empty, render_backpack_1, render_backpack_2, render_backpack_3,
                          render_backpack_4, render_backpack_5, render_backpack_6, render_backpack_7, render_backpack_8)
from src.introduction import render_introduction
from src.eisenhower_q1 import render_eisenhower_q1
from src.eisenhower_method import render_eisenhower_method
from src.eisenhower_q2 import render_eisenhower_q2
from src.pirate import render_pirate
from src.cornell_method import render_cornell_method
from src.blurting_method import render_blurting_method
from src.pomodoro_q1 import render_pomodoro_q1
from src.pomodoro_method import render_pomodoro_method
from src.pomodoro_q2 import render_pomodoro_q2
from src.sail_away import render_sail_away
from src.exit import render_exit

# set up streamlit page configuration
st.set_page_config(
    page_title="PIERATS - Productivity Island Expedition",
    page_icon="🐢",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "#Kiona and Lisa's Game!"
    }
)

# add image and color to the sidebar
st.sidebar.image("pictures/shelly_ahoi.png")
sidebar_color()

# create a progress bar inside the sidebar
# with the help from streamlit docs: https://docs.streamlit.io/library/api-reference/status/st.progress
progress_0 = st.sidebar.progress(0)
for percent_complete_0 in range(0):
    time.sleep(0.01)
    progress_0.progress(percent_complete_0)

# variable to check if the user entered their name and the game can start
start = False

# set session state to track the place the user is at and start with introduction
# with the help from streamlit docs: https://docs.streamlit.io/library/api-reference/session-state
if "place" not in st.session_state:
    st.session_state["place"] = "introduction"

# set up welcome page with layout settings
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    # display logo and title of the game
    logo = st.image("pictures/logo_banner.png")
    welcome = st.markdown(f""" <p style="font-family: serif; font-size:3vw; color:white; 
    text-align:center;"><strong>Welcome to PIERATS<br>the Productivity Island Expedition!</strong></p>""",
                          unsafe_allow_html=True)

    # add a divider for layout separation
    divider = st.divider()

    # create user input for their name and save it
    input_text = st.markdown(f"""<p style="line-height:160%; font-size: 1.5vw; color: white; text-align:center">Are 
    you ready for your adventure?<br>Let me know your name and hit enter to start the game:</p>""",
                             unsafe_allow_html=True)
    player_name_container = st.empty()
    player_name_container.text_input(
        "Text Input", key="player_name",
        label_visibility="hidden"
    )


# if player has provided an input, clear the welcome page widgets and set start to true to start the game
if st.session_state.player_name != "":
    welcome.empty()
    divider.empty()
    input_text.empty()
    player_name_container.empty()
    logo.empty()
    progress_0.empty()

    start = True


# change between the places according to the session state and render the new place
if start:
    if st.session_state.place == "introduction":
        render_introduction()
    elif st.session_state.place == "map_1":
        render_map_1()
    elif st.session_state.place == "backpack_empty":
        render_backpack_empty()
    elif st.session_state.place == "eisenhower_q1":
        render_eisenhower_q1()
    elif st.session_state.place == "map_2":
        render_map_2()
    elif st.session_state.place == "backpack_1":
        render_backpack_1()
    elif st.session_state.place == "eisenhower_method":
        render_eisenhower_method()
    elif st.session_state.place == "map_3":
        render_map_3()
    elif st.session_state.place == "backpack_2":
        render_backpack_2()
    elif st.session_state.place == "eisenhower_q2":
        render_eisenhower_q2()
    elif st.session_state.place == "map_4":
        render_map_4()
    elif st.session_state.place == "backpack_3":
        render_backpack_3()
    if st.session_state.place == "pirate":
        render_pirate()
    elif st.session_state.place == "cornell_method":
        render_cornell_method()
    elif st.session_state.place == "map_5":
        render_map_5()
    elif st.session_state.place == "backpack_4":
        render_backpack_4()
    elif st.session_state.place == "blurting_method":
        render_blurting_method()
    elif st.session_state.place == "map_6":
        render_map_6()
    elif st.session_state.place == "backpack_5":
        render_backpack_5()
    elif st.session_state.place == "pomodoro_q1":
        render_pomodoro_q1()
    elif st.session_state.place == "map_7":
        render_map_7()
    elif st.session_state.place == "backpack_6":
        render_backpack_6()
    elif st.session_state.place == "pomodoro_method":
        render_pomodoro_method()
    elif st.session_state.place == "map_8":
        render_map_8()
    elif st.session_state.place == "backpack_7":
        render_backpack_7()
    elif st.session_state.place == "pomodoro_q2":
        render_pomodoro_q2()
    elif st.session_state.place == "map_9":
        render_map_9()
    elif st.session_state.place == "backpack_8":
        render_backpack_8()
    elif st.session_state.place == "sail_away":
        render_sail_away()
    elif st.session_state.place == "exit":
        render_exit()
