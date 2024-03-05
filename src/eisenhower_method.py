import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
line_height = "130%"
font_size_text = "1.5vw"
font_size_title = "2vw"

# Variables for column sizing
x = 2
y = 1

# List of sections until current page
sections = ["Introduction",
            "Eisenhower First Try",
            "<strong>Eisenhower Method</strong>"
            ]

# List of titles for the tabs
tab_titles = ["Eisenhower Matrix",
              "(1) Do",
              "(2) Schedule",
              "(3) Delegate",
              "(4) Delete",
              "Did you know?"]


# Function to render the eisenhower method page
def render_eisenhower_method():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(20)

    # Displaying sections in the sidebar using a loop
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">{section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">{section}
                        </p>
                        """, unsafe_allow_html=True)

    # Page Title
    st.title("Eisenhower Matrix")

    # Creating tabs for the different sections
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tab_titles)

    # Tab 1: Eisenhower Matrix introduction
    with tab1:
        # Creating a layout with two columns for displaying a picture of the matrix and some explanation
        col1, col2 = st.columns((x, y))
        with col1:
            st.image("pictures/em_empty.png")
        with col2:
            st.markdown(
                f""" 
                <p style="line-height:{line_height}; font-size:{font_size_title};">
                    This is the Eisenhower matrix.
                </p>
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    It's great for organizing and prioritizing tasks. The tasks are divided into important and 
                    unimportant, as well as urgent and non-urgent. This results in a table with 4 fields.<br><br>
                    Continue clicking through the tabs above to learn more about each field
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 2: Field 1 - Do
    with tab2:
        col1, col2 = st.columns((x, y))
        # Creating a layout with two columns for displaying a picture of the matrix and some explanation
        with col1:
            st.image("pictures/em_do.png")
        with col2:
            st.markdown(
                f""" 
                <p style="line-height:{line_height}; font-size: {font_size_title};">
                    Field number 1:<br>Urgent and Important
                </p> 
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    These are tasks that you should complete immediately, otherwise there are consequences, such as you 
                    could die of thirst without clean drinking water. 
                </p> 
                """, unsafe_allow_html=True
            )

    # Tab 3: Field 2 - Schedule
    with tab3:
        col1, col2 = st.columns((x, y))
        # Creating a layout with two columns for displaying a picture of the matrix and some explanation
        with col1:
            st.image("pictures/em_schedule.png")
        with col2:
            st.markdown(
                f""" 
                <p style="line-height: {line_height}; font-size: {font_size_title};">
                    Field number 2:<br>Not Urgent but Important
                </p> 
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    These are tasks that you definitely have to complete, but not as the very first thing. You can 
                    postpone these tasks to a later date, but you still have to complete them because they are important 
                    in the long term, such as building a weapon.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 4: Field 3 - Delegate
    with tab4:
        col1, col2 = st.columns((x, y))
        # Creating a layout with two columns for displaying a picture of the matrix and some explanation
        with col1:
            st.image("pictures/em_delegate.png")
        with col2:
            st.markdown(
                f""" 
                <p style="line-height: {line_height}; font-size: {font_size_title};">
                    Field number 3:<br>Urgent but not Important
                </p> 
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    These are tasks that need to be done urgently, but are not so important that you absolutely have to 
                    do them. Perhaps you can pass the tasks on, in this case to your little brother. Finding wood, for 
                    example, is urgent for fires, shelters and weapons, but doesn't necessarily require your skills and 
                    can also be done by him.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 5: Field 4 - Delete
    with tab5:
        col1, col2 = st.columns((x, y))
        # Creating a layout with two columns for displaying a picture of the matrix and some explanation
        with col1:
            st.image("pictures/em_delete.png")
        with col2:
            st.markdown(
                f""" 
                <p style="line-height: {line_height}; font-size: {font_size_title};">
                    Field number 4:<br>Not Urgent and not Important
                </p> 
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    These tasks are often unnecessary tasks. Like watching the sunset, for example. This activity does 
                    not bring you any closer to your goal and should only be done when everything else has already been 
                    ticked off.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 6: Did you know
    with tab6:
        col1, col2 = st.columns((y, x), gap="large")
        # Creating a layout with two columns for displaying a picture of the matrix and some explanation
        with col1:
            # https://upload.wikimedia.org/wikipedia/commons/6/63/Dwight_D._Eisenhower%2C_official_photo_portrait%2C_May_29%2C_1959.jpg
            st.image("pictures/dwight_eisenhower.png")
        with col2:
            st.markdown(
                f"""<p style="line-height: {line_height}; font-size: {font_size_title};">
                    Did you know?
                </p> 
                <p style="line-height:{line_height}; font-size: {font_size_text};"> 
                    Back in 1954, US President Dwight D. Eisenhower mentioned in one of his speeches that he has a 
                    problem with time management, where he always encounters the same problems: "I have two kinds of 
                    problems, the urgent and the important. The urgent ones are not important, and the important ones 
                    are never urgent." Does it sound familiar to you?<br><br>Now, fast forward a bit to Stephen Covey, 
                    the genius behind a book called "The 7 Habits of Highly Effective People" took Eisenhower's words 
                    and turned it into what we now call the Eisenhower Matrix. Also, it goes by a few other names like 
                    the Eisenhower Principle or the Urgent-Important Matrix.<br><br>Cool, huh? So even a president was 
                    struggling with the same problem as you might be. 
                </p>
                """, unsafe_allow_html=True
            )

        # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
        col_a, col_b = st.columns((8, 1))
        with col_b:
            # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
            # Rerunning the app when the button is clicked to continues the game
            if st.button("Continue"):
                st.session_state.place = "map_3"
                st.rerun()
