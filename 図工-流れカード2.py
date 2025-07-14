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

    # CSSでスタイルを調整
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
            width: 75%;
            max-width: 500px;
            margin-left: 0px;
            padding-left: 0px;
        }
        .card-text {
            font-size: 120px;
            font-weight: bold;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
        }
        .side-button {
            position: fixed;
            left: 20px;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            border-radius: 50%;
            border: none;
            background-color: #ff4b4b;
            color: white;
            font-size: 24px;
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

    # レイアウト構成（画像＋文字）
    st.markdown(
        f"""
        <div class="content-row">
            <img class="card-img" src="{img_paths[st.session_state.img_index]}" />
            <div class="card-text">{texts[st.session_state.img_index]}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 「→」ボタン（HTMLとして左中央に固定）
    st.markdown(
        """
        <button class="side-button" onclick="parent.postMessage({streamlitMessageType: 'streamlit:setComponentValue', value: 'next'}, '*')">→</button>
        <script>
        window.addEventListener("message", (event) => {
            if (event.data && event.data.type === "streamlit:setComponentValue" && event.data.value === "next") {
                window.parent.location.reload();
            }
        });
        </script>
        """,
        unsafe_allow_html=True
    )

    # Python側でボタンイベント検出（reloadでイベントは消えるのでstreamlitでやる場合は↓が確実）
    if st.button("進む（補助用）", key="hidden", help="JSが使えないとき用", disabled=True):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)

main()
