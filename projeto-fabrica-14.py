import streamlit as st
import pandas as pd

# =========================
# CONFIGURAÇÃO DOS NOMES DE COLUNAS
# =========================
COL_ARTISTA = "Artist"
COL_MUSICA = "Track"
COL_SPOTIFY = "Stream"
COL_YOUTUBE = "Views"
COL_YT_URL = "Url_youtube"
COL_SPOTIFY_URL = "Url_spotify"

ARQUIVO_DADOS = "Dados_Artistas.parquet"

# =========================
# CONFIG STREAMLIT
# =========================
st.set_page_config(
    page_title="DJ Wilck - As mais tocadas",
    page_icon="🎧",
    layout="wide",
)

# =========================
# CARREGAR DADOS (PARQUET)
# =========================
@st.cache_data
def load_data():
    return pd.read_parquet(ARQUIVO_DADOS)

df = load_data()

# =========================
# SIDEBAR – FILTROS
# =========================
with st.sidebar:
    st.markdown("### 🎛 Filtros")

    artistas = sorted(df[COL_ARTISTA].unique())
    artista_selecionado = st.selectbox(
        "Selecione o Artista",
        options=artistas
    )

# =========================
# FILTRAR POR ARTISTA
# =========================
df_artista = df[df[COL_ARTISTA] == artista_selecionado]

# =========================
# SUBTÍTULO – ARTISTA SELECIONADO  (ITEM 6)
# =========================
st.markdown(f"## ⭐ Artista Selecionado: **{artista_selecionado}**")
st.write("---")

# =========================
# LISTAGEM DAS MÚSICAS (ITEM 7)
# =========================
st.markdown("### 🎵 Aqui estão as músicas mais tocadas:")

for index, row in df_artista.iterrows():
    with st.container():
        st.markdown(f"### 🎶 **{row[COL_MUSICA]}**")

        col1, col2 = st.columns(2)
        col1.metric("🎧 Spotify Streams", f"{row[COL_SPOTIFY]:,.0f}")
        col2.metric("📺 YouTube Views", f"{row[COL_YOUTUBE]:,.0f}")

        st.video(row[COL_YT_URL])

        # Botão Spotify
        st.link_button('Ouça no Spotify', url=row[COL_SPOTIFY_URL], type='primary')

        st.markdown("---")

