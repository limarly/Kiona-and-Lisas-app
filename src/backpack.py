import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
line_height_backpack = "130%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_backpack = "1.5vw"
font_size_backpack_title = "2vw"
padding_left_backpack = "30px"

# Variables for column sizing
x = 5
y = 3

# Lists of sections for different backpack pages
sections_e = ["Introduction",
              "<strong>Backpack</strong>"]

sections1 = ["Introduction",
             "First Quest",
             "<strong>Backpack</strong>"]

sections2 = ["Introduction",
             "Eisenhower First Try",
             "Eisenhower Method",
             "<strong>Backpack</strong>"]

sections3 = ["Introduction",
             "Eisenhower First Try",
             "Eisenhower Method",
             "Eisenhower Applied",
             "<strong>Backpack</strong>"]

sections4 = ["Introduction",
             "Eisenhower First Try",
             "Eisenhower Method",
             "Eisenhower Applied",
             "Pirate Encounter",
             "Cornell Method",
             "<strong>Backpack</strong>"]

sections5 = ["Introduction",
             "Eisenhower First Try",
             "Eisenhower Method",
             "Eisenhower Applied",
             "Pirate Encounter",
             "Cornell Method",
             "Blurting Method",
             "<strong>Backpack</strong>"]

sections6 = ["Introduction",
             "Eisenhower First Try",
             "Eisenhower Method",
             "Eisenhower Applied",
             "Pirate Encounter",
             "Cornell Method",
             "Blurting Method",
             "Quest First Try",
             "<strong>Backpack</strong>"]

sections7 = ["Introduction",
             "Eisenhower First Try",
             "Eisenhower Method",
             "Eisenhower Applied",
             "Pirate Encounter",
             "Cornell Method",
             "Blurting Method",
             "Pomodoro First try",
             "Pomodoro Method",
             "<strong>Backpack</strong>"
             ]

sections8 = ["Introduction",
             "Eisenhower First Try",
             "Eisenhower Method",
             "Eisenhower Applied",
             "Pirate Encounter",
             "Cornell Method",
             "Blurting Method",
             "Pomodoro First try",
             "Pomodoro Method",
             "Pomodoro Applied",
             "<strong>Backpack</strong>"
             ]


# Function to render the empty backpack
def render_backpack_empty():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(10)

    # Displaying sections in the sidebar using a loop
    for section in sections_e:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_empty.png")
    with col2:
        st.markdown(f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                This is your backpack.
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};"> 
                Unfortunately, it is still empty. Once you finish a quest, you will find your collected equipment here. 
                Let´s see if you can gather enough equipment to repair your boat.<br><br>Let's get started and begin 
                with the first quest!
            </p>
            """, unsafe_allow_html=True)
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_1"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Start First Quest | >>"):
            st.session_state.place = "eisenhower_q1"
            st.rerun()


def render_backpack_1():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(20)

    # Displaying sections in the sidebar using a loop
    for section in sections1:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_1.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                Great!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};">
                You collected the first item in your backpack. You can use the wood later to patch up the holes in your 
                boat.<br><br>Good job!
            </p>""",
            unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_2"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "eisenhower_method"
            st.rerun()


def render_backpack_2():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(30)

    # Displaying sections in the sidebar using a loop
    for section in sections2:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_2.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                Fantastic!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};">
                You collected the second item in your backpack. You can use the nails for the wood you received with 
                your last quest.<br><br>Keep up the good work!
            </p>
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_3"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "eisenhower_q2"
            st.rerun()


def render_backpack_3():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(40)

    # Displaying sections in the sidebar using a loop
    for section in sections3:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_3.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                Amazing!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};"
                You collected the third item in your backpack. What good are nails, without a hammer am I right?<br><br>
                Let's keep going to see what else you can get!<br><br>Oh no wait, can you hear that? I think someone is 
                approaching you. Hopefully this person can help you!
            </p>
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_4"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "pirate"
            st.rerun()


def render_backpack_4():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(50)

    # Displaying sections in the sidebar using a loop
    for section in sections4:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_4.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                Awesome!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};">
                You collected the fourth item in your backpack. Its a saw that you can use to cut the wood to size. I 
                guess you have everything to start with the woodwork?<br><br>Way to go!
            </p>
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_5"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "blurting_method"
            st.rerun()


def render_backpack_5():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(60)

    # Displaying sections in the sidebar using a loop
    for section in sections5:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_5.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
            Extraordinary!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};">
                You collected the fifth item in your backpack. It's white, it's soft, it's... fabric! You can use it to 
                fix your sails.<br><br>Wow! You are really becoming a pro.
            </p>
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_6"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "pomodoro_q1"
            st.rerun()


def render_backpack_6():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(70)

    # Displaying sections in the sidebar using a loop
    for section in sections6:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_6.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                Excellent!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};">
                You collected the sixth item in your backpack. This needle and thread will be helpful to sew the fabric 
                for your new sails. Just be careful to not prick your fingers! <br><br>You are nearly there!
            </p>
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_7"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "pomodoro_method"
            st.rerun()


def render_backpack_7():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(80)

    # Displaying sections in the sidebar using a loop
    for section in sections7:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                    <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_7.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                Wonderful!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};">
                You collected the seventh item in your backpack. Its a rope that you can use to set and adjust the 
                sails. <br><br>Only one more quest to go. You can do it!
            </p>
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_8"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue | >>"):
            st.session_state.place = "pomodoro_q2"
            st.rerun()


def render_backpack_8():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(90)

    # Displaying sections in the sidebar using a loop
    for section in sections8:
        if "<strong>" in section:
            st.sidebar.markdown(
                f"""
                <p style="padding-left: {padding_left_backpack}; line-height: {line_height_sidebar}; 
                font-size: {font_size_sidebar_current};">
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

    # Creating a layout with two columns for image of the backpack and description of the situation
    col1, col2 = st.columns((x, y), gap='large')
    with col1:
        st.image("pictures/backpack_items_8.png")
    with col2:
        st.markdown(
            f""" 
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack_title};">
                Terrific!
            </p>
            <p style="line-height:{line_height_backpack}; font-size: {font_size_backpack};">
                You got a bucket of paint. You can use it to put the finishing touches to your boat and make it look 
                pretty.<br><br>You filled your backpack all the way.<br>Good work! Your boat is now finally completely 
                repaired and you can sail away!
            </p>
            """, unsafe_allow_html=True
        )
        st.image("pictures/shelly_without.png")

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_c, col_b = st.columns((1, 7, 1.3))
    with col_a:
        # Rerunning the app when the button is click to go back to previous page
        if st.button("<< | Go Back"):
            st.session_state.place = "map_9"
            st.rerun()
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Sail Away | >>"):
            st.session_state.place = "sail_away"
            st.rerun()
