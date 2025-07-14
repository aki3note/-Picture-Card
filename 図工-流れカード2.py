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
            st.experimental_rerun()
        for i in range(1, 4):
            st.button(f"教科{i}（未設定）")
    elif st.session_state.page == "art":
        art_page()

def art_page():
    img_paths = [
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%9B%E3%81%A4%E3%82%81%E3%81%84.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%98%E3%82%85%E3%82%93%E3%81%B3.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%A4%E3%81%8F%E3%82%8B.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%81%9F%E3%81%A5%E3%81%91.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%82%93%E3%81%97%E3%82%87%E3%81%86.png?raw=true"
    ]
    texts = ["せつめい", "じゅんび", "つくる", "かたづけ", "かんしょう"]

    st.markdown(
        """
        <style>
        .content-row {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: space-around;
            min-height: 80vh;
        }
        .card-img {
            max-width: 400px;
            margin-left: 20px;
        }
        .card-text {
            font-size: 120px;
            font-weight: bold;
            text-align: center;
        }
        .corner-button {
            position: fixed;
            bottom: 40px;
            right: 40px;
            z-index: 9999;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="content-row">
            <img class="card-img" src="{img_paths[st.session_state.img_index]}" />
            <div class="card-text">{texts[st.session_state.img_index]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 画面右下に固定された「→」ボタン
    if st.button("→", key="next", use_container_width=False):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)

    st.markdown(
        """
        <script>
        const btn = window.parent.document.querySelector('button[kind="secondary"]');
        if (btn) {
            btn.classList.add("corner-button");
        }
        </script>
        """,
        unsafe_allow_html=True
    )

main()

