import streamlit as st
import time


# Setting up some constants for styling
line_height_sidebar = "100%"
line_height_map = "140%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_map = "1.5vw"
font_size_map_title = "2vw"
padding_left = "30px"

# Variables for column sizing
x = 5
y = 3

# Lists of sections for different map pages
sections_1 = ["Introduction",
              "<strong>Map</strong>"]

sections_2 = ["Introduction",
              "First Quest",
              "<strong>Map</strong>"]

sections_3 = ["Introduction",
              "Eisenhower First Try",
              "Eisenhower Method",
              "<strong>Map</strong>"]

sections_4 = ["Introduction",
              "Eisenhower First Try",
              "Eisenhower Method",
              "Eisenhower Applied",
              "<strong>Map</strong>"]

sections_5 = ["Introduction",
              "Eisenhower First Try",
              "Eisenhower Method",
              "Eisenhower Applied",
              "Pirate Encounter",
              "Cornell Method",
              "<strong>Map</strong>"]

sections_6 = ["Introduction",
              "Eisenhower First Try",
              "Eisenhower Method",
              "Eisenhower Applied",
              "Pirate Encounter",
              "Cornell Method",
              "Blurting Method",
              "<strong>Map</strong>"]

sections_7 = ["Introduction",
              "Eisenhower First Try",
              "Eisenhower Method",
              "Eisenhower Applied",
              "Pirate Encounter",
              "Cornell Method",
              "Blurting Method",
              "Quest First Try",
              "<strong>Map</strong>"]

sections_8 = ["Introduction",
              "Eisenhower First Try",
              "Eisenhower Method",
              "Eisenhower Applied",
              "Pirate Encounter",
              "Cornell Method",
              "Blurting Method",
              "Pomodoro First Try",
              "Pomodoro Method",
              "<strong>Map</strong>"]

sections_9 = ["Introduction",
              "Eisenhower First Try",
              "Eisenhower Method",
              "Eisenhower Applied",
              "Pirate Encounter",
              "Cornell Method",
              "Blurting Method",
              "Pomodoro First Try",
              "Pomodoro Method",
              "Pomodoro Applied",
              "<strong>Map</strong>"]


# Functions to render the map pages
def render_map_1():
    # Creating a progress bar in the sidebar using time to let the bar grow slowly
    progress_10 = st.sidebar.progress(0)
    for percent_complete_10 in range(1, 10):
        time.sleep(0.01)
        progress_10.progress(percent_complete_10)

    # Displaying sections in the sidebar using a loop
    for section in sections_1:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_01.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size: {font_size_map_title};">
                OH NO, WHAT HAPPENED HERE?!
            </p> 
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                Looks like you and your little brother stranded on a deserted island. Unfortunately, your boat has 
                broken down and you need new equipment to repair it. As you explore the individual quests, you will be 
                rewarded with new equipment which you can find in your backpack.<br> Also, you can always check your 
                current game progress in the sidebar on the left.<br> Have a quick look into your backpack before we 
                start!
            </p> 
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_empty"
            st.rerun()


def render_map_2():
    # Creating a progress bar in the sidebar
    progress_20 = st.sidebar.progress(0)
    for percent_complete_20 in range(1, 20):
        time.sleep(0.01)
        progress_20.progress(percent_complete_20)

    # Displaying sections in the sidebar using a loop
    for section in sections_2:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_02.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
                Look! There is a way through the jungle!
            </p>
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                When finishing quests you not only get new equipment but can also find your way back to your boat. 
                Stay strong sailor!
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_1"
            st.rerun()


def render_map_3():
    # Creating a progress bar in the sidebar
    progress_30 = st.sidebar.progress(0)
    for percent_complete_30 in range(1, 30):
        time.sleep(0.01)
        progress_30.progress(percent_complete_30)

    # Displaying sections in the sidebar using a loop
    for section in sections_3:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_03.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
                That's the way to go!
            </p>
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                Even more jungle has cleared. Keep going, you have quite the way in front of you!
            </p>""", unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_2"
            st.rerun()


def render_map_4():
    # Creating a progress bar in the sidebar
    progress_40 = st.sidebar.progress(0)
    for percent_complete_40 in range(1, 40):
        time.sleep(0.01)
        progress_40.progress(percent_complete_40)

    # Displaying sections in the sidebar using a loop
    for section in sections_4:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_04.png")
    with col2:
        st.markdown(f""" 
        <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
            You did a great job applying the Eisenhower method!
        </p>
        <p style="line-height:{line_height_map}; font-size: {font_size_map};">
            Look how much of the way has cleared!<br>Have you checked your backpack yet?
        </p>
        """, unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_3"
            st.rerun()


def render_map_5():
    # Creating a progress bar in the sidebar
    progress_50 = st.sidebar.progress(0)
    for percent_complete_50 in range(1, 50):
        time.sleep(0.01)
        progress_50.progress(percent_complete_50)

    # Displaying sections in the sidebar using a loop
    for section in sections_5:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_05.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
                Now you know everything about the Cornell method!
            </p>
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                Looks like you made it halfway through the jungle!
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_4"
            st.rerun()


def render_map_6():
    # Creating a progress bar in the sidebar
    progress_60 = st.sidebar.progress(0)
    for percent_complete_60 in range(1, 60):
        time.sleep(0.01)
        progress_60.progress(percent_complete_60)

    # Displaying sections in the sidebar using a loop
    for section in sections_6:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_06.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
                Now you know everything about the Blurting method!
            </p>
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                Did you know, the best way to use it, is to combine it with the Cornell method?<br>Also have you noticed 
                your progress on the island?
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_5"
            st.rerun()


def render_map_7():
    # Creating a progress bar in the sidebar
    progress_70 = st.sidebar.progress(0)
    for percent_complete_70 in range(1, 70):
        time.sleep(0.01)
        progress_70.progress(percent_complete_70)

    # Displaying sections in the sidebar using a loop
    for section in sections_7:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_07.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
                Well done!
            </p>
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                I knew you would do well in this quest. Would you like to get to know a method that will make you a pro 
                in time management?<br>But first let's check out your new equipment!
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_6"
            st.rerun()


def render_map_8():
    # Creating a progress bar in the sidebar
    progress_80 = st.sidebar.progress(0)
    for percent_complete_80 in range(1, 80):
        time.sleep(0.01)
        progress_80.progress(percent_complete_80)

    # Displaying sections in the sidebar using a loop
    for section in sections_8:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_08.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
                Bravissimo!
            </p>
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                When hearing all these italian foods I have to show off some of my Italian.<br> Wow, have a look on the 
                island! I think I can already see some light coming through the jungle.<br><br>Don't stop now, you 
                almost made it!
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_7"
            st.rerun()


def render_map_9():
    # Creating a progress bar in the sidebar
    progress_90 = st.sidebar.progress(0)
    for percent_complete_90 in range(1, 90):
        time.sleep(0.01)
        progress_90.progress(percent_complete_90)

    # Displaying sections in the sidebar using a loop using a loop
    for section in sections_9:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left}; line-height: {line_height_sidebar}; 
                        font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Creating a layout with two columns for image of the map and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/island_09.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_map}; font-size:{font_size_map_title};">
                You did it!
            </p>
            <p style="line-height:{line_height_map}; font-size: {font_size_map};">
                Amazing job applying the Pomodoro method.<br>Look, the jungle has cleared all the way and you and your 
                brother can return to your boat.<br>Wow, and I think your backpack is getting quite heavy. Let's check 
                it out!
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/shelly_with_backpack.png", width=300)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Open Backpack"):
            st.session_state.place = "backpack_8"
            st.rerun()
