import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
line_height_cornell = "130%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_cornell = "1.5vw"
font_size_cornell_title = "2vw"

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
            "<strong>Cornell Method</strong>"]

tab_titles = ["Strange Encounter",
              "Cornell Method",
              "Main Notes",
              "Keywords & Questions",
              "Summary",
              "Did you know?"]


# Function to render the Cornell Method page
def render_cornell_method():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(40)

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
    st.title("Cornell Method")

    # Creating tabs for the different sections
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tab_titles)

    # Tab 1: Shelly's transition to Cornell Method
    with tab1:
        col1, col2 = st.columns((3, 5), gap='large')
        with col1:
            # Adding some space
            st.markdown(
                f""" 
                <p style="line-height:130%; font-size: 1.3vw; ">
                    <br><br>
                </p>
                """, unsafe_allow_html=True)
            st.image("pictures/shelly_without.png")

        with col2:
            # Markdown with transition to Method
            st.markdown(
                f""" 
                <p style="line-height:{line_height_cornell}; font-size: {font_size_cornell_title};">
                    Wow, what a strange encounter!
                </p>
                <p style="line-height:{line_height_cornell}; font-size: {font_size_cornell};">
                    He was rambling quite a lot, right? But he also said some very helpful things. Did you remember any 
                    of them?<br><br>In this next part I will show you another method. This one is quiet helpful for 
                    writing down notes and keeping them structured. I´m already starting to forget what the pirate 
                    said... was it food or water first?<br><br>Let´s quickly start with this method, so you will know 
                    how to structure your notes and not be so forgetful as me.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 2: Introduces Cornell Method with image and markdown
    with tab2:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f"""
                <p style="line-height:{line_height_cornell}; font-size:{font_size_cornell_title};">
                    This is the Cornell Method
                </p> 
                <p style="line-height:{line_height_cornell}; font-size: {font_size_cornell};">
                    As I said, its great for organizing and understanding information better and keeping it structured.
                    <br><br>First divide your paper into three sections. On the left side you have a narrow column for 
                    Keywords and Questions, the right side is for taking notes and a bottom part for a summary. At the 
                    top you can add a title and date so it is easier for you to associate your notes.
                </p>
                """, unsafe_allow_html=True
            )

    # Explaining Main & keynotes of Method with image and markdown
    with tab3:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_cornell}; font-size:{font_size_cornell_title};">
                    Main Notes & Key Notes
                </p> 
                <p style="line-height:{line_height_cornell}; font-size: {font_size_cornell}; ">
                As you are reading or listening to new information, write down the key points, details and explanations 
                in the large right column.<br><br>Try to use your own words and keep them as short as possible, so you 
                understand the information better.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 4: Explaining left side Keywords and Questions of Method with image and markdown
    with tab4:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_cornell}; font-size:{font_size_cornell_title};">
                    Keywords & Questions
                </p> 
                <p style="line-height:{line_height_cornell}; font-size: {font_size_cornell};">
                    On the left side you can focus on writing down the most important key points that summarize your key 
                    notes, as well as questions about what you are learning.<br><br>This will help you to stay even more 
                    focused and find the most important keywords at a glance.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 5: Explaining bottom summary of method with image and markdown
    with tab5:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/cornell.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_cornell}; font-size:{font_size_cornell_title};">
                    Summary
                </p> 
                <p style="line-height:{line_height_cornell}; font-size: {font_size_cornell}; ">
                    After you finished taking all your notes, write a short summary at the bottom of the page. This will 
                    help you review everything at once.<br><br>When you finished writing everything down, you can use 
                    the paper to see what you remember and review it. For that you can cover up the right side, where 
                    your notes are, and try to answer the questions or explain the main ideas only using the left 
                    column.<br><br>If you use this method before a test or exam, you can review the summaries at the 
                    bottom to remember all your key points.
                </p>
                """, unsafe_allow_html=True
            )

    # Tab 6: Did you know with image and markdown about Cornell University
    with tab6:
        col1, col2, col3, col4 = st.columns((x, z, z, x))
        with col2:
            # https://news.cornell.edu/stories/2023/10/cornell-awarded-excellence-diversity-and-inclusion
            st.image("pictures/cornell_uni.png")

        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height_cornell}; font-size:{font_size_cornell_title};">
                Did you know?
                </p> 
                <p style="line-height:{line_height_cornell}; font-size: {font_size_cornell};">
                    This method was developed at the Cornell University by a professor for their students, so they could 
                    take better notes and encourage active studying.<br><br>So, if you are already learning this method 
                    right now, it will be super easy for you at university. Or maybe already at school? Very impressive!
                </p>
                """, unsafe_allow_html=True
            )

        # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
        col_a, col_b = st.columns((8, 1))
        with col_b:
            # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
            # Rerunning the app when the button is clicked to continues the game
            if st.button("Continue"):
                st.session_state.place = "map_5"
                st.rerun()
