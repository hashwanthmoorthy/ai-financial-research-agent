import streamlit as st
from crew import run_research

st.set_page_config(page_title="AI Financial Research Agent", page_icon="📈", layout="wide")

st.title("📈 AI Multi-Agent Financial Research System")
st.markdown("Powered by **CrewAI** + **Gemini 2.5 Flash** | Built with 4 collaborative AI agents")

st.divider()

ticker = st.text_input("Enter a Stock Ticker", placeholder="e.g. AAPL, TSLA, GOOGL").upper()

if st.button("🚀 Run Research"):
    if not ticker:
        st.warning("Please enter a stock ticker first!")
    else:
        with st.spinner(f"Agents are researching {ticker}... this may take a minute ⏳"):
            try:
                result = run_research(ticker)
                st.success("Research Complete!")
                st.divider()
                st.markdown("## 📝 Final Investment Report")
                st.markdown(str(result))
            except Exception as e:
                st.error(f"Something went wrong: {e}")

st.divider()
st.caption("⚠️ This is not financial advice. For educational purposes only.")