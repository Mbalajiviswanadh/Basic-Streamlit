from PIL import Image
# import requests
import streamlit as st
# import streamlit_lottie as st_lottie

# use emoji codes from here : https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Basic Website" ,page_icon=":four_leaf_clover:",layout="wide")

# def load_lottieUrl(url):
#     r=requests.get(url)
#     if r.status_code !=200:
#         return None
#     return r.json()

# ------------------------load assets
# lottie_coding_ani="#"

image =Image.open("images/wallpaper.jfif")


# ------ Header section ------------
with st.container():
    st.subheader("Hi..:wave:")
    st.title("This is a Basic Website using StreamLit")
    st.write("I made a small Basic Website using StreamLit using Python to practice the syntax in streamlit for creating my upcoming projects :seedling:.")
    st.write("[Connect me](https://www.instagram.com/mb_viswanadh/)")


# section 2

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Hello.., I am vissy
            - i made this website to pracite the streamlit
            - i will be use this streamlit to deply my AI&Ml projects.
            - you can follow me and connect me here: 
                - [linkedin](https://www.linkedin.com/in/balaji-viswanadh-madhavareddy-875473220/)
                - [github](https://github.com/Mbalajiviswanadh)
                - [instagram](https://www.instagram.com/mb_viswanadh/)
            """
        )
        st.markdown("[my Fav Song..](https://youtu.be/ZoEFkdoPosw?si=Z7iQoTNfPao_M8ko)")
        
    with right_column:
        # st_lottie(load_lottieUrl,height=300,key="coding")
        st.header("This is Right Column")
        st.write("##")
        st.write(
            """ 
            seems like i kinda like this haha.
            """
        )        

with st.container():
    st.write("---")
    st.header("works")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # image
        st.image(image)
    with text_column:
            
        st.subheader("helo")
        st.subheader("THis is the text coloumn")
        st.write(
                """
                Lorem Ipsum is simply dummy text of the printing and typesetting industry.
                """
        )
        st.markdown("[my Fav Song..](https://youtu.be/ZoEFkdoPosw?si=Z7iQoTNfPao_M8ko)")