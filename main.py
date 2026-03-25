import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tablero de Accesos", layout="centered")

# Captura el email de quien entra (se activa en el paso final)
user_email = st.user.email if st.user else None

st.title("🎛️ Panel de Accesos Directos")
st.divider()

if user_email:
    df = pd.read_csv("permisos.csv")
    permiso_usuario = df[df['email'] == user_email]

    if not permiso_usuario.empty:
        st.success(f"Bienvenido: {user_email}")
        col1, col2 = st.columns(2)
        
        # Botón VENTAS (Cambiá el link entre comillas por el real)
        if permiso_usuario['ventas'].values[0] == True:
            with col1:
                st.link_button("📊 ACCESO VENTAS", "https://docs.google.com")
                
        # Botón REPORTING (Cambiá el link entre comillas por el real)
        if permiso_usuario['reporting'].values[0] == True:
            with col2:
                st.link_button("📈 ACCESO REPORTING", "https://docs.google.com")
    else:
        st.error(f"⛔ Acceso Denegado para {user_email}.")
else:
    st.warning("Iniciá sesión con Google para ver tus botones.")
