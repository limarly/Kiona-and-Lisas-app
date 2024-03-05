import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
line_height_pomodoro_main = "130%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_pomodoro = "1.5vw"
text_align_pomodoro = "right"
line_height_pomodoro = "150%"

# Variables for column sizing
x = 3
y = 0.5
z = 0.6

#  List of sections until current page
sections = ["Introduction",
            "Eisenhower First Try",
            "Eisenhower Method",
            "Eisenhower Applied",
            "Pirate Encounter",
            "Cornell Method",
            "Blurting Method",
            "Pomodoro First Try",
            "Pomodoro Method",
            "<strong>Pomodoro Applied</strong>"
            ]

# Session state keys for adding and removing tomatoes
button1_add_key = "button1_add"
button2_add_key = "button2_add"
button3_add_key = "button3_add"
button4_add_key = "button4_add"
button5_add_key = "button5_add"
button6_add_key = "button6_add"
button7_add_key = "button7_add"
button8_add_key = "button8_add"
button9_add_key = "button9_add"
button10_add_key = "button10_add"

button1_rem_key = "button1_rem"
button2_rem_key = "button2_rem"
button3_rem_key = "button3_rem"
button4_rem_key = "button4_rem"
button5_rem_key = "button5_rem"
button6_rem_key = "button6_rem"
button7_rem_key = "button7_rem"
button8_rem_key = "button8_rem"
button9_rem_key = "button9_rem"
button10_rem_key = "button10_rem"


# Function to render the second Pomodoro Quest
def render_pomodoro_q2():
    # Displaying sections in the sidebar using a loop
    st.sidebar.progress(80)

    # Use a loop to format and display the strings
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">{section}</p>
                """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">{section}</p>
                """, unsafe_allow_html=True)

    # Layout with two columns with a picture of shelly, an explanation of the quest and an info box
    col_1, col_2 = st.columns((1, 4))
    with col_1:
        st.image("pictures/shelly.png")
    with col_2:
        st.title("Let's talk tomatoes!")
        st.markdown(
            f""" 
            <p style="line-height:{line_height_pomodoro_main}; font-size: {font_size_pomodoro};">
                Now you learned everything about the Pomodoro Method. Shall we have another look at the time management 
                of your tasks? Let's try to break down your tasks in Pomodori.<br>For example I would choose one 
                Pomodoro for the time I need for cleaning my shell. 
            </p>
            """, unsafe_allow_html=True)
        st.info("Continue once you are finished with the button on the bottom right.", icon="❕")

    st.divider()

    # Markdown to define the meaning of the tomato
    st.markdown(
        f""" 
        <p style="text-align: center; line-height:{line_height_pomodoro_main}; font-size: {font_size_pomodoro}; ">
            🍅  =  1  Pomodoro  =  25 minutes of focused work session  +  5 minutes break
        </p> 
        """, unsafe_allow_html=True)

    st.divider()

    # Creating columns for the game
    col1a, col1b, col1c, col1d = st.columns((x, y, z, x))
    col2a, col2b, col2c, col2d = st.columns((x, y, z, x))
    col3a, col3b, col3c, col3d = st.columns((x, y, z, x))
    col4a, col4b, col4c, col4d = st.columns((x, y, z, x))
    col5a, col5b, col5c, col5d = st.columns((x, y, z, x))
    col6a, col6b, col6c, col6d = st.columns((x, y, z, x))
    col7a, col7b, col7c, col7d = st.columns((x, y, z, x))
    col8a, col8b, col8c, col8d = st.columns((x, y, z, x))
    col9a, col9b, col9c, col9d = st.columns((x, y, z, x))
    col10a, col10b, col10c, col10d = st.columns((x, y, z, x))

    # Displaying the tasks
    with col1a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Search for drinking water
            </p> 
            """, unsafe_allow_html=True)
    with col2a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Build a Shelter
            </p> 
            """, unsafe_allow_html=True)
    with col3a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Search for food
            </p> 
            """, unsafe_allow_html=True)
    with col4a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Collect Wood 
            </p> 
            """, unsafe_allow_html=True)
    with col5a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Build a fire
            </p> 
            """, unsafe_allow_html=True)
    with col6a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Search for a container (for water or food)
            </p> 
            """, unsafe_allow_html=True)

    with col7a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Build a weapon
            </p> 
            """,  unsafe_allow_html=True)
    with col8a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Explore the 
            surroundings
            </p> 
            """, unsafe_allow_html=True)

    with col9a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro};">
                Collect Shells
            </p> 
            """, unsafe_allow_html=True)
    with col10a:
        st.markdown(
            f"""
            <p style="text-align:{text_align_pomodoro}; font-size:{font_size_pomodoro}; 
            line-height: {line_height_pomodoro}; ">
                Watch the Sunset
            </p> 
            """, unsafe_allow_html=True)

    # Buttons to add tomatoes
    with col1b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes1' not in st.session_state:
            st.session_state.tomatoes1 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button1_add_key):
            st.session_state.tomatoes1.append("🍅")

    with col2b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes2' not in st.session_state:
            st.session_state.tomatoes2 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button2_add_key):
            st.session_state.tomatoes2.append("🍅")

    with col3b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes3' not in st.session_state:
            st.session_state.tomatoes3 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button3_add_key):
            st.session_state.tomatoes3.append("🍅")

    with col4b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes4' not in st.session_state:
            st.session_state.tomatoes4 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button4_add_key):
            st.session_state.tomatoes4.append("🍅")

    with col5b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes5' not in st.session_state:
            st.session_state.tomatoes5 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button5_add_key):
            st.session_state.tomatoes5.append("🍅")

    with col6b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes6' not in st.session_state:
            st.session_state.tomatoes6 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button6_add_key):
            st.session_state.tomatoes6.append("🍅")

    with col7b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes7' not in st.session_state:
            st.session_state.tomatoes7 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button7_add_key):
            st.session_state.tomatoes7.append("🍅")

    with col8b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes8' not in st.session_state:
            st.session_state.tomatoes8 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button8_add_key):
            st.session_state.tomatoes8.append("🍅")

    with col9b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes9' not in st.session_state:
            st.session_state.tomatoes9 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button9_add_key):
            st.session_state.tomatoes9.append("🍅")

    with col10b:
        # Initialize the tomatoes list in the session state
        if 'tomatoes10' not in st.session_state:
            st.session_state.tomatoes10 = []

        # Add button to add a tomato
        if st.button("+ Add 🍅", button10_add_key):
            st.session_state.tomatoes10.append("🍅")

    # Buttons to remove tomatoes
    with col1c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button1_rem_key):
            if st.session_state.tomatoes1:
                st.session_state.tomatoes1.pop()

    with col2c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button2_rem_key):
            if st.session_state.tomatoes2:
                st.session_state.tomatoes2.pop()

    with col3c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button3_rem_key):
            if st.session_state.tomatoes3:
                st.session_state.tomatoes3.pop()

    with col4c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button4_rem_key):
            if st.session_state.tomatoes4:
                st.session_state.tomatoes4.pop()

    with col5c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button5_rem_key):
            if st.session_state.tomatoes5:
                st.session_state.tomatoes5.pop()

    with col6c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button6_rem_key):
            if st.session_state.tomatoes6:
                st.session_state.tomatoes6.pop()

    with col7c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button7_rem_key):
            if st.session_state.tomatoes7:
                st.session_state.tomatoes7.pop()

    with col8c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button8_rem_key):
            if st.session_state.tomatoes8:
                st.session_state.tomatoes8.pop()

    with col9c:
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button9_rem_key):
            if st.session_state.tomatoes9:
                st.session_state.tomatoes9.pop()

    with col10c:
        # Add button to remove a tomato
        # Add button to remove a tomato
        if st.button("- Remove 🍅", button10_rem_key):
            if st.session_state.tomatoes10:
                st.session_state.tomatoes10.pop()

    # Displaying the tomato emojis
    with col1d:
        st.text(" ".join(st.session_state.tomatoes1))
    with col2d:
        st.text(" ".join(st.session_state.tomatoes2))
    with col3d:
        st.text(" ".join(st.session_state.tomatoes3))
    with col4d:
        st.text(" ".join(st.session_state.tomatoes4))
    with col5d:
        st.text(" ".join(st.session_state.tomatoes5))
    with col6d:
        st.text(" ".join(st.session_state.tomatoes6))
    with col7d:
        st.text(" ".join(st.session_state.tomatoes7))
    with col8d:
        st.text(" ".join(st.session_state.tomatoes8))
    with col9d:
        st.text(" ".join(st.session_state.tomatoes9))
    with col10d:
        st.text(" ".join(st.session_state.tomatoes10))

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        # button to return to the map
        if st.button("Continue"):
            st.session_state.place = "map_9"
            st.rerun()
