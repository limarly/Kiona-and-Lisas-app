import streamlit as st


# Setting up some constants for styling
line_height_sidebar = "100%"
line_height = "130%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
font_size_text = "1.5vw"
font_size_title = "2vw"

# Variables for column sizing
x = 1
y = 3
z = 4
v = 0.5

# List of sections until current page
sections = [
    "Introduction",
    "Eisenhower First Try",
    "Eisenhower Method",
    "Eisenhower Applied",
    "Pirate Encounter",
    "Cornell Method",
    "Blurting Method",
    "Pomodoro First Try",
    "<strong>Pomodoro Method</strong>"
]

# List of tab titles to display
tab_titles = ["Tomatoes",
              "Pomodoro Method",
              "Tasks in Pomodori",
              "Did you know?"]


# Function to render the Pomodoro Method page
def render_pomodoro_method():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(70)

    # Displaying sections in the sidebar using a loop
    for section in sections:
        if "<strong>" in section:
            st.sidebar.markdown(
                f"""
                <p style="line-height: {line_height_sidebar}; font-size: {font_size_sidebar_current};">
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

    # Page title
    st.title("Pomodoro Technique")

    # Creating tabs for the different sections
    tab1, tab2, tab3, tab4 = st.tabs(tab_titles)

    # Tab 1: Introduction to Pomodoro Method with image and markdown
    with tab1:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            st.image("pictures/tomato.png")
        with col3:
            st.markdown(
                f""" 
                <p style="line-height:{line_height}; font-size:{font_size_title};">
                    Pasta Bolognese, Pasta Arrabiata, Pasta Pomodoro...Wait what? We are not talking about food?
                </p>
                <p style="line-height:{line_height}; font-size: {font_size_text};"> 
                    In fact the Pomodoro Technique has not much to do with the pasta dish or tomatoes. Even though 
                    pomodoro means tomato in Italian.<br><br>It actually is a helpful method to stay concentrated and 
                    think about time-management. Continue clicking through the tabs above to learn more about foo..I 
                    mean the technique. Wow, all this talk about tomatoes made me hungry...
                </p>
                """, unsafe_allow_html=True)

    # Tab 2: Explanation of main concept of pomodoro method using an image and markdown
    with tab2:
        col1, col2, col3, col4 = st.columns((v, y, z, v))
        with col2:
            st.image("pictures/pomodoro.png")
        with col3:
            st.markdown(
                f"""
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    The Pomodoro Method is a technique for time management developed by the student Frances Cirillo in 
                    the late 1980s. It is a simple but effective way to improve focus and productivity by breaking down 
                    work or tasks into intervals.<br><br>This is how the Pomodoro Method works:<br>
                </p>
                <p style="line-height:150%; font-size: {font_size_text};">
                    1. Choose a task you would like to work on<br>
                    2. Set a timer for 25 minutes (one Pomodoro)<br>
                    3. Work until the timer goes off<br>
                    4. Take a short break of five minutes<br>
                    5. Repeat the process  until you have completed four Pomodori<br>
                    6. After four Pomodori, take a longer break of 15-30 minutes
                </p>
                """, unsafe_allow_html=True)

    # Tab 3: Explain additional rules of the pomodoro method and show how to apply to daily life using images
    # and markdown
    with tab3:
        col1, col2, col3, col4 = st.columns((v, y, z, v))
        with col2:
            st.image("pictures/day_in_pomodori.png")
            st.markdown(
                f"""
                <p style="text-align: center; line-height:{line_height}; font-size: 2vw;">
                    This is how you could structure<br>a day into Pomodori
                """, unsafe_allow_html=True)

        with col3:
            st.markdown(
                f"""
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    <strong>There are three additional rules for the technique:</strong><br>
                    Break down complex tasks into smaller once. If a task has more than four Pomodori break it down to 
                    even smaller tasks. Like when you think about surviving on the island. It is much easier to think 
                    about that challenge if you break it down into the tasks of finding water, food and shelter than to 
                    just think about surviving all in once.<br><br>
                    Combine small and easy tasks. If a task doesn't need a full pomodoro flow combine it with another 
                    easy task to make it a full pomodoro.<br><br>
                    Once a pomodoro has started you should not interrupt the flow. Try to keep distractions to a minimum 
                    and if you did get distracted take a five minute break instead and start another pomodoro 
                    afterwards. For your next time try to keep track of your distractions so you think about how you can 
                    minimise them in the future.
                """, unsafe_allow_html=True)

    # Tab 4: Did you know of Method shows a recipie of Pasta Al Pomodoro
    with tab4:
        col1, col2, col3, col4 = st.columns((x, y, z, x))
        with col2:
            # https://www.gutekueche.at/spaghetti-al-pomodoro-rezept-32917
            st.image("pictures/spaghetti_al_pomodoro.png")
            st.markdown(
                f"""
               <p style="line-height:{line_height}; font-size: {font_size_text};">
                   <strong>Ingredients for 2 Portions</strong><br>
               """, unsafe_allow_html=True)
            col_left, col_right = st.columns((1, 2))
            with col_left:
                st.markdown(
                    f"""
                    <p style="line-height:{line_height}; font-size: {font_size_text};">
                        240g<br>0.5 <br>1 EL<br>0.25 TL<br>Pinch<br>0.5 TL<br>400g<br>2<br>2 EL<br>2 EL<br>1 Pinch
                        <br>2<br>
                    </p>
                    """, unsafe_allow_html=True)
            with col_right:
                st.markdown(
                    f"""
                    <p style="line-height:{line_height}; font-size: {font_size_text};">
                        Spaghetti<br>Basil<br>Tomato Paste<br>Sugar<br>Black Pepper<br>Salt<br>Diced Canned Tomatoes<br>
                        Garlic Cloves<br>Olive Oil<br>Grated Parmesan<br>Chilli Flakes<br>Thyme Twigs<br>
                    </p>
                    """, unsafe_allow_html=True)

        with col3:
            st.markdown(
                f"""
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    <strong>Spaghetti Al Pomodoro is a tasty italian recipie.<br>If you are looking for something to do 
                    in your 30 minute break between your pomodoro flows here is a great recipie for it:<br><br></strong>
                </p>
                """, unsafe_allow_html=True)

            col_left_1, col_right_1 = st.columns((0.1, 2))
            with col_left_1:
                st.markdown(
                    f"""
                    <p style="line-height:{line_height}; font-size: {font_size_text};">
                        1. <br><br><br>
                        2. <br><br><br>
                        3. <br><br><br>
                        4. <br><br><br><br>
                        5. <br><br><br>
                        6. 
                    </p>
                    """, unsafe_allow_html=True)

            with col_right_1:
                st.markdown(
                    f"""
                    <p style="line-height:{line_height}; font-size: {font_size_text};">
                        Peel and finely dice the garlic cloves. Heat oil in a pan and fry the diced garlic until 
                        translucent.<br><br>
                        Then add the tomato paste, fry briefly and deglaze with the canned tomatoes.<br><br>
                        Season with salt, pepper, chilli flakes and sugar and simmer gently over a low heat for around 5 
                        minutes.<br><br>
                        In the meantime, cook the spaghetti according to the package instructions until al dente. wash 
                        the basil, shake dry and chop finely.<br><br>
                        Season the tomato sauce again with salt and pepper, add the basil and thyme and briefly bring to 
                        a boil.<br><br>
                        Finally, drain the spaghetti, remove the twigs of thyme from the sauce and mix the spaghetti 
                        with the sauce - serve sprinkled with parmesan if you like.<br>
                    </p>
                    """, unsafe_allow_html=True)

    # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
    col_a, col_b = st.columns((8, 1))
    with col_b:
        # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
        # Rerunning the app when the button is clicked to continues the game
        if st.button("Continue"):
            st.session_state.place = "map_8"
            st.rerun()
