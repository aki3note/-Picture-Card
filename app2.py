import streamlit as st
from PIL import Image, ImageSequence
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

st.set_page_config(page_title="GIFコマ割りPDF", layout="centered")

st.title("🎞 GIFコマ割りPDFジェネレーター")
st.caption("GIFをアップロードして、各コマをPDFに変換します（外部送信なし）")

uploaded_file = st.file_uploader("📁 GIFファイルを選択してください", type=["gif"])

def extract_frames(gif_image):
    frames = []
    for frame in ImageSequence.Iterator(gif_image):
        frames.append(frame.convert("RGB"))
    return frames

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

        if idx % (images_per_row * images_per_col) == 0 and idx != 0:
            c.showPage()

        resized = frame.resize((int(img_width), int(img_height)))
        img_io = BytesIO()
        resized.save(img_io, format="PNG")
        img_io.seek(0)
        c.drawImage(img_io, x_positions[col], y_positions[row], width=img_width, height=img_height)

    c.save()
    pdf_buffer.seek(0)
    return pdf_buffer

if uploaded_file is not None:
    try:
        gif = Image.open(uploaded_file)
        frames = extract_frames(gif)
        st.success(f"{len(frames)} フレームを抽出しました。")

        if st.button("📄 PDFを生成する"):
            pdf_bytes = create_comic_pdf(frames)
            st.download_button(
                label="⬇️ PDFをダウンロード",
                data=pdf_bytes,
                file_name="komawari_output.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.error(f"GIFの読み込みに失敗しました: {e}")
