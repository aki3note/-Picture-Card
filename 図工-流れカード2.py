import streamlit as st

def main():
    st.set_page_config(page_title="絵カードアプリ", layout="wide")

    if "img_index" not in st.session_state:
        st.session_state.img_index = 0
    if "page" not in st.session_state:
        st.session_state.page = "menu"

    if st.session_state.page == "menu":
        st.header("教科を選んでください")
        if st.button("図工"):
            st.session_state.page = "art"
            st.rerun()
        for i in range(1, 4):
            st.button(f"教科{i}（未設定）")
    elif st.session_state.page == "art":
        art_page()

def art_page():
    img_paths = [
        "https://github.com/aki3note/-Picture-Card/blob/main/%E7%94%BB%E5%83%8F/%E5%9B%B3%E5%B7%A5-%E3%81%9B%E3%81%A4%E3%82%81%E3%81%841.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%98%E3%82%85%E3%82%93%E3%81%B3.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%A4%E3%81%8F%E3%82%8B.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%81%9F%E3%81%A5%E3%81%91.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%82%93%E3%81%97%E3%82%87%E3%81%86.png?raw=true"
    ]
    texts = ["せつめい", "じゅんび", "つくる", "かたづけ", "かんしょう"]

    st.markdown(
        """
        <style>
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
        .content-row {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            min-height: 80vh;
            gap: 50px;
            position: relative;
        }
        .card-img {
            width: 35%;
            max-width: 500px;
        }
        .card-text {
            font-size: 130px;
            font-weight: bold;
            text-align: left;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            height: 100%;
            margin-left: -60px;
            min-width: 400px;
        }
        /* 透明の全画面ボタン */
        div[data-testid="stButton"] button.fullscreen-button {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            opacity: 0;
            cursor: pointer;
            z-index: 9999;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # メイン表示
    st.markdown(
        f"""
        <div class="content-row">
            <img class="card-img" src="{img_paths[st.session_state.img_index]}" />
            <div class="card-text">{texts[st.session_state.img_index]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Streamlitボタン（透明）を画面全体に重ねる
    if st.button(" ", key="tap_next"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)

main()
