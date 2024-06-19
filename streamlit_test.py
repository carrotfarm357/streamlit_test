import streamlit as st
from PIL import Image

# 사이드바 만들기
st.sidebar.header("로그인")
user_id = st.sidebar.text_input("ID", value='', max_chars=20)
user_pw = st.sidebar.text_input("PW", value="", type='password')

if user_id == 'abcd' and user_pw == '1234':
    st.sidebar.header("image list")
    sel_options = ["", 'le', 'ai', 'fu', 'rui', 'hui']
    user_opt = st.sidebar.selectbox("like", sel_options, index = 0)
    st.sidebar.write("select>> ", user_opt)

    # 메인 화면
    st.subheader("main")
    image_files=["welcome.jpg","le.jpg","ai.jpg","fu.jpg","rui.jpg","hui.jpg"]
    sel_index = sel_options.index(user_opt)
    img_file = image_files[sel_index]
    img_local = Image.open(f"(img_file))
    st.image(img_local, caption=user_opt)
