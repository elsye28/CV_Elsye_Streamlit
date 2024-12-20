import streamlit as st

st.title("💼 Pengalaman Kerja")
st.write("---")

def display_experience(title, period, description, projects, achievements, icon="🏭"):
    st.write(f"### {icon} {title} ({period})")
    st.markdown(f"**Deskripsi:** {description}")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Proyek Utama:**")
        st.markdown(projects)
    with col2:
        st.markdown("**Pencapaian:**")
        st.markdown(achievements)
    
    st.write("---")


# Pengalaman Kerja 1
display_experience(
    title="PT. INTENS - Tenaga Ahli",
    period="Sep 2022 - Okt 2024",
    description="Merancang dan mengimplementasikan sistem pengolahan limbah di berbagai lokasi.",
    projects="""
    - Analisis kelayakan pengolahan sampah di TPA Mekarsari Kota Dumai.
    - Perancangan sistem dan proses pengolahan sampah di TPA Mekarsari dan TPS3R Desa Bulila, Kab. Gorontalo.
    - Monitoring dan evaluasi instalasi sistem pengolahan sampah.
    """,
    achievements="""
    - Meningkatkan efisiensi sistem pengolahan limbah di dua lokasi utama.
    - Membantu optimalisasi instalasi pengolahan sampah.
    """,
    icon="🏭"
)

# Pengalaman Kerja 2
display_experience(
    title="PT. Masaro Berkah Enjineering - Tenaga Ahli",
    period="Jan 2024 - Agu 2024",
    description="Mengembangkan instalasi pengolahan sampah berbasis circular economy.",
    projects="""
    - Pembuatan proposal, RAB, desain, dan laporan untuk instalasi pengolahan sampah di TPS3R Desa Borobudur dan Kabupaten Klaten.
    """,
    achievements="""
    - Menyelesaikan instalasi dengan efisiensi tinggi dan tepat waktu.
    """,
    icon="♻️"
)

# Pengalaman Kerja 3
display_experience(
    title="ERIA - Tenaga Ahli",
    period="Jun 2022 - Jan 2024",
    description="Kajian demand dan supply hidrogen untuk sektor industri di ASEAN hingga 2050.",
    projects="""
    - Menyusun rekomendasi kebijakan transisi ke hidrogen rendah karbon di negara berkembang.
    """,
    achievements="""
    - Menyusun rekomendasi strategis untuk sektor industri.
    - Berhasil menyelesaikan laporan akhir sesuai target waktu.
    """,
    icon="🔬"
)

# Pengalaman Kerja 4
display_experience(
    title="Badan Riset dan Inovasi Nasional (BRIN) - Asisten Periset",
    period="Sep 2022 - Sep 2023",
    description="Penelitian LCA PVC di Indonesia, China, dan database global menggunakan OpenLCA.",
    projects="""
    - Sintesis PVC Oxo-Biodegradable.
    - Pirolisis limbah PVC untuk pengelolaan yang lebih berkelanjutan.
    """,
    achievements="""
    - Publikasi jurnal internasional terkait penelitian.
    - Menyusun laporan lengkap untuk presentasi hasil penelitian.
    """,
    icon="🔍"
)

# Pengalaman Kerja 5
display_experience(
    title="LTPM ITB - Peneliti",
    period="Mei 2022 - Nov 2023",
    description="Penelitian mikroplastik pada produk teh celup dan AMDK.",
    projects="""
    - Uji kualitas keamanan air minum dalam kemasan (AMDK).
    - Penelitian mikroplastik pada produk teh celup.
    """,
    achievements="""
    - Mengembangkan metodologi baru untuk mendeteksi mikroplastik secara efisien.
    - Meningkatkan kualitas penelitian mikroplastik di ITB.
    """,
    icon="🧪"
)

# Pengalaman Kerja 6
display_experience(
    title="PT. Rinder Energia - Tenaga Ahli",
    period="Jan 2023 - Sep 2023",
    description="Analisis data cadangan gas dan kebutuhan industri petrokimia berbasis gas bumi.",
    projects="""
    - Pemilihan lokasi kilang petrokimia berbasis surplus gas regional.
    - Menyusun proyeksi kebutuhan gas bumi Indonesia 2023-2060.
    """,
    achievements="""
    - Menyusun laporan komprehensif yang diterima oleh klien.
    """,
    icon="🔧"
)

# Pengalaman Kerja 7
display_experience(
    title="Yayasan Polimer Lestari - Tenaga Ahli",
    period="Jul 2022 - Des 2022",
    description="Penyusunan dokumen kebijakan strategis di sektor polimer lestari.",
    projects="""
    - Penyusunan dokumen RPIP dan RPIK untuk Provinsi Kepulauan Riau dan Kab. Natuna.
    - Penyusunan naskah akademik dan rancangan Peraturan Daerah (Ranperda).
    """,
    achievements="""
    - Dokumen berhasil digunakan sebagai referensi kebijakan di daerah terkait.
    """,
    icon="🌱"
)

# Pengalaman Kerja 8
display_experience(
    title="LPPM ITB - Asisten Pelaksana Pengabdian",
    period="Feb 2019 - Des 2022",
    description="Implementasi pengelolaan sampah Masaro di berbagai lokasi.",
    projects="""
    - Edukasi masyarakat terkait pengolahan sampah dan pertanian berkelanjutan.
    """,
    achievements="""
    - Sukses meningkatkan kesadaran masyarakat tentang pengelolaan sampah organik.
    """,
    icon="🌎"
)

# Pengalaman Kerja 9
display_experience(
    title="PT. LAPI ITB - Tenaga Ahli",
    period="Jun 2020 - Jan 2022",
    description="Optimalisasi peralatan industri menggunakan RENKEI Control untuk pengurangan konsumsi energi.",
    projects="""
    - LCA produk PVC dari industri di Indonesia.
    """,
    achievements="""
    - Laporan diterima dengan baik oleh klien, mendukung efisiensi energi di sektor PVC.
    """,
    icon="🔄"
)

# Pengalaman Kerja 10
display_experience(
    title="PT. Pertamina RU VI - Magang",
    period="Jul 2017 - Agu 2017",
    description="Evaluasi aktivitas katalis untuk konversi heavy naphtha menjadi naphtha bernilai oktan tinggi.",
    projects="""
    - Pengujian efisiensi katalis pada skala laboratorium.
    """,
    achievements="""
    - Laporan hasil magang diterima oleh tim teknis Pertamina RU VI.
    """,
    icon="⛽"
)

# Pengalaman Kerja 11
display_experience(
    title="Ganesha Course - Pengajar",
    period="Apr 2017 - Agu 2021",
    description="Mengajar mata pelajaran matematika, kimia, dan fisika untuk siswa SMA.",
    projects="""
    - Membimbing siswa dalam memahami konsep-konsep kompleks dan mempersiapkan ujian.
    """,
    achievements="""
    - Membantu siswa mencapai nilai akademik yang lebih tinggi di sekolah dan ujian masuk universitas.
    """,
    icon="📚"
)