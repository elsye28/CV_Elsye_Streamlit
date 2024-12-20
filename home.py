import streamlit as st
from PIL import Image, ExifTags

st.set_page_config(page_title="CV Elsye Veradika", page_icon="👩‍🔬", layout="wide")

def fix_orientation(image_path):
    """Memperbaiki orientasi foto berdasarkan metadata EXIF."""
    image = Image.open(image_path)
    try:
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == "Orientation":
                break
        exif = image._getexif()
        if exif is not None:
            orientation_value = exif.get(orientation)
            if orientation_value == 3:
                image = image.rotate(180, expand=True)
            elif orientation_value == 6:
                image = image.rotate(270, expand=True)
            elif orientation_value == 8:
                image = image.rotate(90, expand=True)
    except Exception:
        pass
    return image

image_path = "images/foto.JPG"

photo = fix_orientation(image_path)

st.title("👩‍🔬 Curriculum Vitae - Elsye Veradika")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(photo, caption="Foto Profil", width=200)

with col2:
    st.write("## 📜 Biodata")
    st.markdown("""
    - **Nama:** Elsye Veradika Yemensia  
    - **Bidang:** Teknik Kimia  
    - **Email:** [elsye.v.y@gmail.com](mailto:elsye.v.y@gmail.com)  
    - **Nomor Telepon:** +62 82129768177  
    - **LinkedIn:** [linkedin.com/in/elsye-veradika](https://linkedin.com/in/elsye-veradika)  
    """)

# Pemisah
st.write("---")

# Tentang Saya
st.subheader("Tentang Saya")
st.write("""
Saya merupakan lulusan teknik kimia dengan pengalaman dalam penelitian, pengembangan teknologi, dan berbagai proyek di bidang lingkungan, energi, dan industri.
Saya terlibat dalam berbagai proyek terkait dengan kajian energi di Indonesia, pengolahan limbah berbasis teknologi berkelanjutan, pengembangan polimer, analisis siklus hidup (LCA), dan penyusunan kebijakan pembangunan industri daerah.
Didukung dengan keahlian teknis, kemampuan beradaptasi, dan kemampuan kerjasama dan kolaborasi yang baik, saya juga aktif dalam publikasi ilmiah serta pengembangan paten teknologi.
""")