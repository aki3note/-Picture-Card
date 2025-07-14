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

    # HTML＋CSSで画像全体クリック可能なボタンを作る
    st.markdown(
        f"""
        <form action="" method="post">
            <button name="next_card" type="submit" style="
                border: none;
                background: none;
                padding: 0;
                width: 100%;
            ">
                <img src="{img_paths[st.session_state.img_index]}" style="max-width: 400px; display: block; margin: auto;" />
            </button>
        </form>
        """,
        unsafe_allow_html=True
    )

    # POSTで送信されたときだけインデックス進める
    if st.session_state.get("_submitted"):
        st.session_state.img_index = (st.session_state.img_index + 1) % len(img_paths)
        st.session_state._submitted = False  # リセット

    # フォーム送信検出用（非表示でPOST受信を確認）
    js = """
    <script>
    const form = window.parent.document.querySelector('form');
    form.onsubmit = function() {
        window.parent.postMessage("next", "*");
    }
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)

    # JSからのメッセージを受けてSessionStateを書き換える
    st.experimental_data_editor({"_submitted": True}, key="editor", disabled=True)

    if st.button("← 教科選択に戻る"):
        st.session_state.page = "menu"
        st.experimental_rerun()

main()

