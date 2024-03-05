import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
line_height = "130%"
font_size_text = "1.5vw"

# Variables for column sizing
x = 0.1
y = 2

# List of tasks for the first quest
tasks = ["Search for a container (for food or water)",
         "Build a fire",
         "Build Shelter",
         "Collect Shells",
         "Collect Wood",
         "Watch the Sunset",
         "Search for drinking water",
         "Search for Food",
         "Build a Weapon",
         "Explore the surroundings"
         ]


# Function to render the first quest of the Eisenhower Method
def render_eisenhower_q1():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(10)

    # Displaying sections in the sidebar
    st.sidebar.markdown(
        f"""
        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
            Introduction
        </p>
        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">
            <strong>First Quest</strong>
        </p>
        """, unsafe_allow_html=True
    )

    # Layout with two columns for image of shelly and a description of the quest
    col_1, col_2 = st.columns((1, 4))
    with col_1:
        st.image("pictures/shelly.png")
    with col_2:
        st.title("Arranging tasks!")
        st.markdown(
            f""" 
            <p style="line-height:{line_height}; font-size: {font_size_text};"> 
               You and your little brother are stranded on the deserted island. So, there are a lot of things you have 
               to do in order to survive. But how should you start?<br>Create an order of the tasks that you can see on 
               the left by choosing one of the boxes and selecting the task you would like to place there. You can 
               rearrange your tasks indefinitely until you are happy with your order. Go on, there is no right or wrong!
            </p>
            """, unsafe_allow_html=True)

    st.divider()

    # layout with 4 columns; col_space just for layout reasons
    col_3, col_space, col_4 = st.columns((2, 0.1, 4))
    with col_3:
        # Expander displays the tasks and info box
        with st.expander(label="Here you can see all your tasks", expanded=True):
            st.markdown(
                f""" 
                <p style="line-height:150%; font-size: {font_size_sidebar};">
                    · Build a Fire<br>· Collect Shells<br>· Build a shelter<br>· Search for Food<br>· Build a Weapon<br>
                    · Collect Wood<br>· Watch the Sunset<br>· Search for drinking water<br>· Explore the surroundings
                    <br>· Search for a container (for food or water)
                </p>""", unsafe_allow_html=True
            )

            st.info("Keep in mind to not select the same task more than once.\nContinue once you are finished with "
                    "the button on the bottom right.", icon="❕")

    with col_4:

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
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    1.
                </p>
                """, unsafe_allow_html=True
            )
        with col2a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    2.
                </p>
                """, unsafe_allow_html=True
            )
        with col3a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    3.
                </p>
                """, unsafe_allow_html=True
            )
        with col4a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    4.
                </p>
                """, unsafe_allow_html=True
            )
        with col5a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    5.
                </p>
                """, unsafe_allow_html=True
            )
        with col6a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    6.
                </p>
                """, unsafe_allow_html=True
            )
        with col7a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    7.
                </p>
                """, unsafe_allow_html=True
            )
        with col8a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    8.
                </p>
                """, unsafe_allow_html=True
            )
        with col9a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    9.
                </p>
                """, unsafe_allow_html=True
            )
        with col10a:
            st.markdown(
                f""" 
                <p style="text-align:right; font-size:1.7vw; line-height: 194%;">  
                    10.
                </p>
                """, unsafe_allow_html=True
            )


        # Creating 10 select boxes for the tasks
        with col1b:
            st.selectbox("1", tasks, index=None,
                     placeholder="Select what you would do first...", label_visibility="collapsed")
        with col2b:
            st.selectbox("2", tasks, index=None,
                     placeholder="Select what you would do second...", label_visibility="collapsed")
        with col3b:
            st.selectbox("3", tasks, index=None,
                     placeholder="Select what you would do third...", label_visibility="collapsed")
        with col4b:
            st.selectbox("4", tasks, index=None,
                     placeholder="Select what you would do fourth...", label_visibility="collapsed")
        with col5b:
            st.selectbox("5", tasks, index=None,
                     placeholder="Select what you would do fifth...", label_visibility="collapsed")
        with col6b:
            st.selectbox("6", tasks, index=None,
                     placeholder="Select what you would do sixth...", label_visibility="collapsed")
        with col7b:
            st.selectbox("7", tasks, index=None,
                     placeholder="Select what you would do seventh...", label_visibility="collapsed")
        with col8b:
            st.selectbox("8", tasks, index=None,
                     placeholder="Select what you would do eighth...", label_visibility="collapsed")
        with col9b:
            st.selectbox("9", tasks, index=None,
                     placeholder="Select what you would do ninth...", label_visibility="collapsed")
        with col10b:
            st.selectbox("10", tasks, index=None,
                     placeholder="Select what you would do last...", label_visibility="collapsed")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "backpack_empty"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "map_2"
            st.rerun()
