import streamlit as st

def main():
    st.set_page_config(page_title="絵カードアプリ", layout="centered")
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
    st.write("画像をクリックすると次のカードに進みます")

    img_paths = [
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%9B%E3%81%A4%E3%82%81%E3%81%84.png?raw=true",
        "https://placehold.jp/150x150.png?text=2枚目",
        "https://placehold.jp/150x150.png?text=3枚目",
        "https://placehold.jp/150x150.png?text=4枚目",
        "https://placehold.jp/150x150.png?text=5枚目"
    ]

    if "img_index" not in st.session_state:
        st.session_state.img_index = 0

    if st.button("次のカードを見る"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)

    st.image(img_paths[st.session_state.img_index], use_column_width=True)

    if st.button("← 教科選択に戻る"):
        st.session_state.page = "menu"
        st.experimental_rerun()

main()
