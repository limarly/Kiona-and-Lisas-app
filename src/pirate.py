import streamlit as st
import base64


# Setting up some constants for styling
line_height_sidebar = "100%"
font_size_sidebar = "1.1vw"
font_size_sidebar_current = "1.3vw"
line_height = "130%"
font_size_text = "1.5vw"
font_size_title = "2vw"

# Variables for column sizing
x = 1
y = 4

# List of tab titles to display
tab_titles = ["Pirate 1 | >>",
              "Pirate 2 | >>",
              "Pirate 3 |"
              ]

# List of sections until current page
sections = ["Introduction",
            "Eisenhower First Try",
            "Eisenhower Method",
            "Eisenhower Applied",
            "<strong>Pirate Encounter</strong>"
            ]

# Pirate speech content in a list to split it in three parts
pirate_speech = ["Arr, gather 'round, ye lads!<br>Sit tight and listen close, for I've a tale to tell that'll curl "
                 "yer toes and set the wind in yer sails. Once upon a time, not so long ago, I sailed the vast and "
                 "treacherous seas, seeking fortune and adventure at every turn. But, fate had other plans for this "
                 "old sea dog. A fierce storm, the likes of which I'd never seen, swept me ship off course and dashed "
                 "it upon the jagged rocks of this cursed isle. For years I've been marooned here, a castaway left to "
                 "fend for meself. But fear not, for I've learned a thing or two about survival in these harsh and "
                 "unforgiving lands. Ye see, survival ain't just about strength and skill; it's about adaptin' to yer "
                 "surroundings, makin' do with what ye have, and never losin' hope. Take heed, young ones, "
                 "for I'll share with ye the secrets of me survival.",
                 "First and foremost, ye must master the art of findin' water. Without ye will not survive the day. "
                 "Next ye must learn to find shelter from the elements. Build yerself a sturdy shelter, a haven from "
                 "the wind and rain, and ye'll weather any storm that comes yer way. And don´t forget ye also need "
                 "food. The sea be teemin' with life, me hearties, so cast yer lines and nets and reap the bounty "
                 "that lies beneath the waves. And don't be afraid to forage the land for fruits and berries, "
                 "for nature provides for those who know where to look. But survival ain't just about yer daily "
                 "bread; it's about stayin' sharp in both mind and body. Keep yer wits about ye at all times, "
                 "for danger lurks in every shadow. Train yer body to endure the rigors of this harsh land, "
                 "for only the strong survive in the end.",
                 "And finally, me lads, never lose sight of yer true goal. Ye may be stranded on this island for now, "
                 "but never give up hope of escapin' its clutches and returnin' to the open sea. Keep in mind that "
                 "time is essential for survival, use it wisely. Repair yer boat, gather yer supplies, and when the "
                 "time is right, set sail for freedom once more. So heed me words well, me hearties, and ye'll find "
                 "that even in the darkest of times, there be light to guide ye home. For as long as there be breath "
                 "in yer lungs and fire in yer hearts, ye'll never be truly lost at sea.<br>Now, enough of me "
                 "ramblin's! Let's raise a toast to adventure, to survival, and to the boundless spirit of the open "
                 "sea! Yo ho ho!"
                 ]


# Function to autoplay the sail away audio
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


# Funktion to render the pirate encounter page
def render_pirate():
    # Creating a progress bar in the sidebar
    st.sidebar.progress(45)

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

    # Creating three tabs for the pirate story
    tab1, tab2, tab3 = st.tabs(tab_titles)

    # Tab 1: Displaying the first part of the story
    with tab1:
        col1, col2, col3, col4 = st.columns((x, y, y, x))
        with col2:
            # using an image of the pirate
            st.image("pictures/pirate.png")

        with col3:
            st.markdown("\n\n\n")  # empty lines for layout reasons
            # audiofile of what the pirate has to say
            autoplay_audio("audio/Part_1.mp3")
            # written text of the tale of the pirate
            st.markdown(
                f"""
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    "{pirate_speech[0]}"
                </p>
                """, unsafe_allow_html=True)
    # Tab 2: Displaying the second part of the story
    with tab2:
        col1, col2, col3, col4 = st.columns((x, y, y, x))
        with col2:
            # using an image of the pirate
            st.image("pictures/pirate.png")

        with col3:
            st.markdown("\n\n\n")  # empty lines for layout reasons
            # audiofile of what the pirate has to say
            st.audio("audio/Part_2.mp3")
            # written text of the tale of the pirate
            st.markdown(
                f"""
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    "{pirate_speech[1]}"
                </p>
                """, unsafe_allow_html=True)

    # Tab 3: Displaying the third part of the story
    with tab3:
        col1, col2, col3, col4 = st.columns((x, y, y, x))
        with col2:
            # using an image of the pirate
            st.image("pictures/pirate.png")

        with col3:
            st.markdown("\n\n\n")  # empty lines for layout reasons
            # audiofile of what the pirate has to say
            st.audio("audio/Part_3.mp3")
            # written text of the tale of the pirate
            st.markdown(
                f"""
                <p style="line-height:{line_height}; font-size: {font_size_text};">
                    "{pirate_speech[2]}"
                </p>
                """, unsafe_allow_html=True)

        # Layout with two columns (same used on other pages) to guarantee consistency in the design of the pages
        col_a, col_b = st.columns((8, 1))
        with col_b:
            # https://docs.streamlit.io/library/api-reference/control-flow/st.rerun
            # Rerunning the app when the button is clicked to continues the game
            if st.button("Continue"):
                st.session_state.place = "cornell_method"
                st.rerun()
