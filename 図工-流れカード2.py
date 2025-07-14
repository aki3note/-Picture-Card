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

    cols = st.columns([2, 3])
    with cols[0]:
        # 画像を左に詰めて表示（余白20px）
        st.markdown(
            f"""
            <div style='margin-left: 20px;'>
                <img src="{img_paths[st.session_state.img_index]}" style="width:100%; max-width:400px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

    with cols[1]:
        st.markdown(
            f"""
            <div style='
                font-size: 96px;
                font-weight: bold;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
            '>
                {texts[st.session_state.img_index]}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 右下に「→」ボタンだけ配置
    col_spacer, col_next = st.columns([10, 1])
    with col_next:
        if st.button("→", use_container_width=True):
            st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)

main()

