import streamlit as st

# TODO: Formatting & Comments

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

    # Series of columns to fit the layout
    col3, col4 = st.columns((x, y))
    with col3:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Search for drinking water<br>Build a Shelter<br>Search for food
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col4:
        st.time_input('Label1', value=None, label_visibility="collapsed")
        st.time_input('Label2', value=None, label_visibility="collapsed")
        st.time_input('Label3', value=None, label_visibility="collapsed")

    col5, col6 = st.columns((x, y))
    with col5:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Collect Wood<br>Build a fire<br>Search for a container (for water or food)
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col6:
        st.time_input('Label4', value=None, label_visibility="collapsed")
        st.time_input('Label5', value=None, label_visibility="collapsed")
        st.time_input('Label6', value=None, label_visibility="collapsed")

    col7, col8 = st.columns((x, y))
    with col7:
        # Displaying the tasks
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Build a weapon<br>Explore the surroundings<br>Collect Shells
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the three tasks above
    with col8:
        st.time_input('Label7', value=None, label_visibility="collapsed")
        st.time_input('Label8', value=None, label_visibility="collapsed")
        st.time_input('Label9', value=None, label_visibility="collapsed")

    col9, col10 = st.columns((x, y))
    with col9:
        # Displaying a task
        st.markdown(
            f""" 
            <p style="text-align:right; font-size:{font_size_pomodoro}; line-height: {line_height_pomodoro_main};">
                Watch the Sunset
            </p> 
            """, unsafe_allow_html=True)

    # Displaying the time inputs for the task above
    with col10:
        st.time_input('Label10', value=None, label_visibility="collapsed")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue"):
            st.session_state.place = "map_7"
            st.rerun()
