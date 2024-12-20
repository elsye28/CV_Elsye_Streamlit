import streamlit as st

st.title("🌟 Keahlian (Skills)")
st.write("---")

# Keahlian Teknis
st.subheader("🔧 Keahlian Teknis")
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    - **Pemrograman dan Analisis Data:**
      - Python
      - SQL
      - OpenLCA
    - **Statistik dan Analisis:**
      - Minitab
      - Excel
    - **Desain Industri:**
      - Aspen HYSYS
      - SketchUp
      - SolidWorks
    """)

with col2:
    st.markdown("**Level Kompetensi:**")
    
    skills = {
        "Python (Intermediate)": 0.65,
        "SQL (Intermediate)": 0.6,
        "OpenLCA (Intermediate)": 0.7,
        "Minitab (Advanced)": 0.85,
        "Aspen HYSYS (Advanced)": 0.8,
        "SketchUp (Advanced)": 0.9,
        "SolidWorks (Intermediate)": 0.6
    }

    for skill, level in skills.items():
        st.markdown(f"{skill}")
        st.progress(level)
st.write("---")

# Soft Skills dan Bahasa
st.subheader("🌍 Soft Skills dan Bahasa")
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
    - **Soft Skills:**
      - Pemecahan Masalah
      - Komunikasi Tim dan Leadership
      - Manajemen Waktu
    """)

with col2:
    st.markdown("""
    - **Bahasa:**
      - Bahasa Indonesia (Native)
      - Bahasa Inggris (Fluent)
    """)

# Skill Highlight
st.write("---")
st.subheader("🌟 Tingkat Keahlian Soft Skills")
soft_skills = {
    "Komunikasi Tim": 0.95,
    "Pemecahan Masalah": 0.9,
    "Manajemen Waktu": 0.85
}

for skill, level in soft_skills.items():
    st.markdown(f"**{skill}**")
    st.progress(level)