import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
line_height_blurting = "130%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_blurting = "1.5vw"
font_size_blurting_title = "2vw"

# Variables for column sizing
x = 1
y = 3
z = 4

# List of sections until current page
sections = ["Introduction",
            "Eisenhower First Try",
            "Eisenhower Method",
            "Eisenhower Applied",
            "Pirate Encounter",
            "Cornell Method",
            "<strong>Blurting Method</strong>"]

# List of tab titles to display
tab_titles = ["Blurting Method",
              "Blurting",
              "What you forgot",
              "Practice Questions",
              "Did you know?"]


# Function to render the Blurting Method page
def render_blurting_method():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(50)

    # Displaying sections in the sidebar using a loop
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)
        else:
            st.sidebar.markdown(f"""
                        <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar};">
                            {section}
                        </p>
                        """, unsafe_allow_html=True)

    # Page Title
    st.title("Blurting Method")

    # Creating tabs for the different sections
    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_titles)

    # Tab 1: Introduction to Blurting Method with image and markdown
    with tab1:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    This is the Blurting Method
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    I know you´ve listened closely to the Pirate and wrote down all the important information he gave 
                    you. Now to remember all that information by heart, you have to study it. For this the Blurting 
                    Method can be very helpful.<br><br>Have you ever heard of it? If not here's how it works:
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 2: Explaining Blurting with images and markdown
    with tab2:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    Blurting
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    If you want you can take a look at your notes you took before and organize them, if you have a lot 
                    of notes. Skim quickly through the notes. And now its time to blurt! Cover up your notes and start 
                    jotting down everything you can recall. Don´t worry about being perfect and getting everything 
                    right - just get the ideas flowing, like the waves around you.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 3: Explaining bottom left "What did you forget" with image and markdown
    with tab3:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    What did you forget?
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    You can now take a moment to review. Check your notes with your blurted ideas to see if you missed 
                    something.<br><br>Add this extra info in a different to color.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 4: Explaining "Practice Questions" bottom right with image and markdown
    with tab4:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/blurting.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    Practice Questions
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                    To help you remember everything even better, you can additionally add questions to test your 
                    knowledge and exam technique.
                </p>
                """, unsafe_allow_html=True
            )

    # Get the name of the player
    player_name = st.session_state.player_name
    if player_name is not None:
        player_name = player_name.upper()

    # Tab 5. Did you know - with image and markdown
    with tab5:
        col1, col2, col3, col4 = st.columns((x, z, z, x))
        with col2:
            st.image("pictures/red_curtain.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_blurting}; font-size:{font_size_blurting_title};">
                    Did you know?
                </p> 
                <p style="line-height:{line_height_blurting}; font-size: {font_size_blurting};">
                The blurting method is often used in improvisational comedy to generate quick and spontaneous humor.
                <br><br>In improvisation, blurting refers to the act of saying the first thing that comes to mind 
                without filtering it. This can lead to unexpected and hilarious outcomes as performers react in the 
                moment.<br><br>What do you think? Can you just blurt down notes and information from your memory like an 
                improvisation performer?<br>Curtains up and make way for {player_name}!
                </p>
                """, unsafe_allow_html=True
            )

        # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
        col_a, col_c, col_b = st.columns((1, 7, 1.3))
        with col_a:
            # Rerunning the app when the button is click to go back to previous page
            if st.button("<< | Go Back"):
                st.session_state.place = "backpack_4"
                st.rerun()
        with col_b:
            # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
            # Rerunning the app when the button is clicked to continues the game
            if st.button("Continue | >>"):
                st.session_state.place = "map_6"
                st.rerun()
