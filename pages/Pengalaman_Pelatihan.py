import streamlit as st

# Judul Halaman
st.title("📚 Pengalaman Pelatihan")
st.write("---")

# Fungsi untuk menampilkan setiap pelatihan
def display_training(title, period, description, icon="📘"):
    st.write(f"### {icon} {title} ({period})")
    st.markdown(f"**Deskripsi:** {description}")
    st.write("---")

# Pelatihan 1: Minitab Essential Training
display_training(
    title="Minitab Essential Training",
    period="27-28 Juli 2024",
    description="""
    Pelatihan mendalam tentang analisis statistik menggunakan Minitab, termasuk:
    - Analisis data eksploratif dan pengolahan data statistik.
    - Penerapan kontrol kualitas statistik untuk pengambilan keputusan berbasis data.
    """
)

# Pelatihan 2: Full Stack Data Science Sanber Campus X ITB (Batch 4)
display_training(
    title="Full Stack Data Science Sanber Campus X ITB (Batch 4)",
    period="September 2024 - Januari 2025",
    description="""
    Pelatihan intensif untuk menjadi praktisi data science, mencakup:
    - Pemrograman Python untuk analisis data.
    - Pemodelan Machine Learning.
    - Visualisasi data dengan Matplotlib.
    """
)