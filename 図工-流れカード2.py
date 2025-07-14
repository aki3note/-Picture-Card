import streamlit as st

def main():
    st.set_page_config(page_title="絵カードアプリ", layout="wide")  # iPad横画面対応
    st.title("絵カードアプリ")

    page = st.session_state.get("page", "menu")

    if page == "menu":
        st.header("教科を選んでください")
        if st.button("図工"):
            st.session_state.page = "art"
            st.experimental_rerun()
        for i in range(1, 4):
            st.button(f"教科{i}（未設定）")

    elif page == "art":
        art_page()

def art_page():
    st.header("図工の絵カード")
    st.write("画像をタッチすると次のカードに進みます")

    img_paths = [
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%9B%E3%81%A4%E3%82%81%E3%81%84.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%98%E3%82%85%E3%82%93%E3%81%B3.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%A4%E3%81%8F%E3%82%8B.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%81%9F%E3%81%A5%E3%81%91.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%82%93%E3%81%97%E3%82%87%E3%81%86.png?raw=true"
    ]

    texts = ["せつめい", "じゅんび", "つくる", "かたづけ", "かんしょう"]

    if "img_index" not in st.session_state:
        st.session_state.img_index = 0

    # 横並び（左：画像、右：説明）
    cols = st.columns([2, 3])
    with cols[0]:
        if st.button("", key="img_click"):
            st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)
        st.image(img_paths[st.session_state.img_index], use_column_width=True)

    with cols[1]:
        st.markdown(
            f"""
            <div style='font-size: 48px; font-weight: bold; padding: 40px; text-align: center;'>
                {texts[st.session_state.img_index]}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    if st.button("← 教科選択に戻る"):
        st.session_state.page = "menu"
        st.experimental_rerun()

main()
