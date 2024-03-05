import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
line_height_pomodoro_main = "194%"
font_size_pomodoro = "1.7vw"
text_align_pomodoro = "right"
line_height_pomodoro = "150%"

# Variables for column sizing
x = 2
y = 3

# List of sections until current page
sections = ["Introduction",
            "Eisenhower First Try",
            "Eisenhower Method",
            "Eisenhower Applied",
            "Pirate Encounter",
            "Cornell Method",
            "Blurting Method",
            "<strong>Quest First Try</strong>"
            ]


# Function to render the first Pomodoro Quest
def render_pomodoro_q1():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(60)

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
        st.title("Hurry up!")
        st.markdown(
            f""" 
            <p style="line-height:130%; font-size: 1.5vw;">
                As you just heard from the pirate: time management is a crucial part of surviving this island. So let's 
                have a look at your tasks again. Looks like the pirate has already sorted them for you in the order that 
                he would recommend. The only thing left for you to do is to think about how much time you need for the 
                individual tasks. Fill out the time slots in hours and minutes by either selecting one of the suggested 
                times or by writing them down in the slots. <br>For example it takes me about 23 minutes to clean my 
                shell. So I would put in 00:23 for this task.
            </p>
            """, unsafe_allow_html=True
        )
        st.info("Continue once you are finished with the button on the bottom right.", icon="❕")

    st.divider()

    # Creating the columns for the tasks
    col1a, col1b = st.columns((x, y))
    col2a, col2b = st.columns((x, y))
    col3a, col3b = st.columns((x, y))
    col4a, col4b = st.columns((x, y))
    col5a, col5b = st.columns((x, y))
    col6a, col6b = st.columns((x, y))
    col7a, col7b = st.columns((x, y))
    col8a, col8b = st.columns((x, y))
    col9a, col9b = st.columns((x, y))
    col10a, col10b = st.columns((x, y))

    with col1a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Search for drinking water
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col1b:
        st.time_input('Label1', value=None, label_visibility="collapsed")

    with col2a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Build a Shelter
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col2b:
        st.time_input('Label2', value=None, label_visibility="collapsed")

    with col3a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Search for food
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col3b:
        st.time_input('Label3', value=None, label_visibility="collapsed")

    with col4a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Collect Wood
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col4b:
        st.time_input('Label4', value=None, label_visibility="collapsed")

    with col5a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Build a fire
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col5b:
        st.time_input('Label5', value=None, label_visibility="collapsed")

    with col6a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Search for a container (for water or food)
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col6b:
        st.time_input('Label6', value=None, label_visibility="collapsed")

    with col7a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Build a weapon
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col7b:
        st.time_input('Label7', value=None, label_visibility="collapsed")

    with col8a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Explore the surroundings
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col8b:
        st.time_input('Label8', value=None, label_visibility="collapsed")

    with col9a:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Collect Shells
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col9b:
        st.time_input('Label9', value=None, label_visibility="collapsed")

    with col10a:
        # Displaying a task
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Watch the Sunset
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the task above
    with col10b:
        st.time_input('Label10', value=None, label_visibility="collapsed")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "backpack_5"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "map_7"
            st.rerun()
