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
        "https://github.com/aki3note/-Picture-Card/blob/main/%E7%94%BB%E5%83%8F/%E5%9B%B3%E5%B7%A5-%E3%81%9B%E3%81%A4%E3%82%81%E3%81%841.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%98%E3%82%85%E3%82%93%E3%81%B3.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%A4%E3%81%8F%E3%82%8B.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%81%9F%E3%81%A5%E3%81%91.png?raw=true",
        "https://github.com/aki3note/-Picture-Card/blob/main/%E5%9B%B3%E5%B7%A5-%E3%81%8B%E3%82%93%E3%81%97%E3%82%87%E3%81%86.png?raw=true"
    ]
    texts = ["せつめい", "じゅんび", "つくる", "かたづけ", "かんしょう"]

    # CSSカスタマイズ
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
        }
        .card-img {
            width: 45%;
            max-width: 500px;
            margin-left: 0px;
            padding-left: 0px;
        }
        .card-text {
    font-size: 120px;
    font-weight: bold;
    text-align: left; /* ← center から left に変更 */
    display: flex;
    align-items: center;
    justify-content: flex-start; /* ← 左寄せに */
    height: 100%;
    margin-left: -80px; /* ← 追加で左へずらす */
}

        .fixed-button {
            position: fixed;
            top: 50%;
            right: 20px;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: none;
            background-color: #cccccc;
            color: black;
            font-size: 24px;
            font-weight: bold;
            text-align: center;
            line-height: 50px;
            cursor: pointer;
            z-index: 9999;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # メイン表示：画像とテキスト
    st.markdown(
        f"""
        <div class="content-row">
            <img class="card-img" src="{img_paths[st.session_state.img_index]}" />
            <div class="card-text">{texts[st.session_state.img_index]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Streamlitボタン → JSでスタイル当てて右中央に配置＆丸く＆地味色
    if st.button("→", key="next"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)

    st.markdown(
        """
        <script>
        const btn = window.parent.document.querySelector('button[kind="secondary"]');
        if (btn) {
            btn.classList.add("fixed-button");
        }
        </script>
        """,
        unsafe_allow_html=True
    )

main()
