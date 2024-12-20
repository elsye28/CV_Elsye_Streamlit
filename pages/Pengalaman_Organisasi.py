import streamlit as st

st.title("🎭 Pengalaman Organisasi")
st.write("---")

def display_organization(title, period, description, achievements, icon="🎨"):
    st.write(f"### {icon} {title} ({period})")
    
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Deskripsi:**")
        st.markdown(description)
    with col2:
        st.markdown("**Pencapaian:**")
        st.markdown(achievements)

    st.write("---")

# Pengalaman Organisasi 1
display_organization(
    title="Ketua Pelestarian Seni dan Budaya Minangkabau (UKA ITB)",
    period="2016 - 2017",
    description="""
    - Mengelola tim seni dan budaya untuk melestarikan budaya Minangkabau di lingkungan ITB.
    - Merancang pertunjukan seni tahunan untuk mempromosikan seni tradisional Minangkabau.
    """,
    achievements="""
    - Berhasil menggelar pertunjukan seni tahunan dengan lebih dari 300 peserta.
    - Mendapat apresiasi dari civitas akademika atas kontribusi dalam pelestarian budaya.
    """,
    icon="🎨"
)

# Pengalaman Organisasi 2
display_organization(
    title="Konseptor Acara Pagelaran Seni dan Budaya UKM ITB",
    period="2015 - 2016",
    description="""
    - Bertanggung jawab atas perencanaan dan pelaksanaan acara seni tahunan.
    - Membentuk dan mengelola tim kreatif untuk mempersiapkan konsep acara.
    """,
    achievements="""
    - Berhasil memperkenalkan inovasi dalam format acara dengan tambahan segmen edukasi budaya.
    - Acara mendapatkan perhatian media lokal dan menarik lebih banyak audiens.
    """,
    icon="🎭"
)


# Pengalaman Organisasi 3
display_organization(
    title="Anggota Aktif Keluarga Mahasiswa Teknik Kimia ITB",
    period="2014 - 2018",
    description="""
    - Berkontribusi dalam pelaksanaan kegiatan sosial dan akademik.
    - Membantu mengoordinasikan acara seminar dan pelatihan untuk mahasiswa Teknik Kimia.
    """,
    achievements="""
    - Meningkatkan partisipasi mahasiswa dalam kegiatan sosial dan akademik.
    - Menjalin kemitraan dengan industri untuk mendukung seminar tahunan.
    """,
    icon="🔬"
)