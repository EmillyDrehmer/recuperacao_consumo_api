import streamlit as st
from consumidor_api import obter_previsao

st.set_page_config(
    page_title="Dashboard Meteorológico",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Meteorológico")
st.write("Painel de monitoramento — Jaraguá do Sul/SC")

if st.button("🔄 Consultar novamente"):
    st.rerun()

try:
    with st.spinner("Atualizando painel..."):
        dados = obter_previsao()

    st.success("Painel atualizado.")

    st.subheader("Indicadores principais")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🌡️ Temperatura",
        f"{dados['Temperatura']:.1f} °C"
    )

    col2.metric(
        "💧 Umidade relativa",
        f"{dados['Umidade']:.0f} %"
    )

    col3.metric(
        "🌡️ Sensação térmica",
        f"{dados['Sensação_Térmica']:.1f} °C"
    )

    st.divider()

    st.subheader("Condições ambientais")

    esquerda, direita = st.columns(2)

    with esquerda:
        st.markdown("**Precipitação**")

        st.metric(
            "Volume registrado",
            f"{dados['Precipitação']:.1f} mm"
        )

    with direita:
        st.markdown("**Velocidade do vento**")

        st.metric(
            "Velocidade registrada",
            f"{dados['Velocidade_Vento']:.1f} km/h"
        )

    st.divider()



except Exception as erro:
    st.error(f"Erro ao atualizar o dashboard: {erro}")
