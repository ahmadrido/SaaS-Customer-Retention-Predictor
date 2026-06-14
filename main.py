import streamlit as st
import pandas as pd
import joblib 

st.set_page_config(
    page_title="Predicting Our SaaS Customers",
    page_icon=":chart_with_upwards_trend:",
)

model = joblib.load("model_pengguna_saas.joblib")

st.title("SaaS Customer Retention Predictor")
st.markdown("Prediksi apakah pengguna aplikasi Anda akan bertahan, berhenti, atau upgrade bulan depan.")
st.write("---")


col1, col2 = st.columns(2)

with col1:
    login_per_bulan = st.slider("Login Per Bulan", min_value=1, max_value=30, value=15)
    durasi_sesi_per_menit = st.slider("Durasi Sesi (Menit)", min_value=5, max_value=180, value=45)

with col2:
    fitur_ai_dipakai = st.slider("Fitur AI yang Digunakan", min_value=0, max_value=50, value=8)
    jumlah_komplain = st.slider("Jumlah Komplain Bulan Ini", min_value=0, max_value=10, value=1)

st.write("---")

if st.button("Analisis Status Pengguna", type="primary"):
    data_baru = pd.DataFrame([[login_per_bulan, durasi_sesi_per_menit, fitur_ai_dipakai, jumlah_komplain]], columns=["Login_Per_Bulan", "Durasi_Sesi_Menit", "Fitur_AI_Dipakai", "Jumlah_Komplain"])
    
    prediksi = model.predict(data_baru)[0]
    prob_array = model.predict_proba(data_baru)[0]
    persentase = float(prob_array.max()) * 100

    st.subheader("Hasil Analisis Sistem AI:")
    
    if prediksi == "Upgrade":
        st.success(f"Pengguna ini berpotensi besar untuk **{prediksi}** (Tingkat Keyakinan: {persentase:.2f}%)")
    elif prediksi == "Bertahan":
        st.info(f"Pengguna ini cenderung **{prediksi}** menggunakan layanan (Tingkat Keyakinan: {persentase:.2f}%)")
    else:
        st.error(f"Peringatan: Pengguna ini berisiko **{prediksi}** berlangganan! (Tingkat Keyakinan: {persentase:.2f}%)")