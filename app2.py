import streamlit as st
from PIL import Image, ImageSequence
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

st.set_page_config(page_title="GIFコマ割りPDF", layout="centered")
st.title("🎞 GIFコマ割りPDFジェネレーター")
st.caption("アニメーションGIFをアップロード → コマ割りPDF生成")

uploaded_file = st.file_uploader("📁 GIFファイルを選んでください", type=["gif"])

def extract_frames(gif_image):
    return [frame.copy().convert("RGB") for frame in ImageSequence.Iterator(gif_image)]

def create_comic_pdf(frames, images_per_row=3, images_per_col=3):
    pdf_buffer = BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=A4)
    width, height = A4
    margin = 30
    img_width = (width - 2 * margin) / images_per_row
    img_height = (height - 2 * margin) / images_per_col

    x_positions = [margin + i * img_width for i in range(images_per_row)]
    y_positions = [height - margin - (j + 1) * img_height for j in range(images_per_col)]

    for idx, frame in enumerate(frames):
        col = idx % images_per_row
        row = (idx // images_per_row) % images_per_col

        if idx != 0 and idx % (images_per_row * images_per_col) == 0:
            c.showPage()

        resized = frame.resize((int(img_width), int(img_height)))
        img_io = BytesIO()
        resized.save(img_io, format="PNG")
        img_io.seek(0)
        c.drawImage(img_io, x_positions[col], y_positions[row], width=img_width, height=img_height)

    c.save()
    pdf_buffer.seek(0)
    return pdf_buffer

if uploaded_file:
    try:
        gif = Image.open(uploaded_file)
        if getattr(gif, "is_animated", False) is False:
            st.warning("これはアニメーションGIFではありません")
        else:
            frames = extract_frames(gif)
            st.success(f"{len(frames)}フレームを抽出しました")

            if st.button("📄 PDFを生成"):
                pdf = create_comic_pdf(frames)
                st.download_button("⬇️ PDFをダウンロード", data=pdf, file_name="komawari.pdf", mime="application/pdf")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")
