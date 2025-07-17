import streamlit as st
from PIL import Image, ImageSequence
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from io import BytesIO

# GIFをImageとして読み込み（ここは差し替えてもOK）
GIF_PATH = "sample.gif"  # ここを好きなパスやURLに変更してもOK

def extract_frames(gif_image):
    frames = []
    for frame in ImageSequence.Iterator(gif_image):
        frame = frame.convert("RGB")  # PDFはRGB推奨
        frames.append(frame)
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
        page = idx // (images_per_row * images_per_col)

        if idx % (images_per_row * images_per_col) == 0 and idx != 0:
            c.showPage()

        resized = frame.resize((int(img_width), int(img_height)))
        img_io = BytesIO()
        resized.save(img_io, format="PNG")
        c.drawImage(Image.open(BytesIO(img_io.getvalue())), x_positions[col], y_positions[row], width=img_width, height=img_height)

    c.save()
    pdf_buffer.seek(0)
    return pdf_buffer

# Streamlit App
st.title("🎞 GIFコマ割りPDFジェネレーター")

st.caption("サンプルGIFからPDFを生成します。")

try:
    gif = Image.open(GIF_PATH)
    frames = extract_frames(gif)
    st.success(f"GIFから {len(frames)} コマを抽出しました！")

    if st.button("📄 PDFを生成"):
        pdf = create_comic_pdf(frames)
        st.download_button("⬇️ PDFをダウンロード", data=pdf, file_name="comic_output.pdf", mime="application/pdf")
except Exception as e:
    st.error(f"GIFの読み込みに失敗しました: {e}")
