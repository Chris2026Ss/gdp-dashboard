import streamlit as st
import pandas as pd
import math
from pathlib import Path

st.set_page_config(page_title='JunubLink AI Portal', page_icon=':earth_africa:', layout='wide')

# HEADER
st.title("JunubLink AI - Africa Youth Tech Education Innovation")
st.markdown("**Munuki Hub, Juba | JunubLink-AI@gmail.com | GDP + Scholarships + Scam Alert**")
st.divider()

tab1, tab2, tab3 = st.tabs(["📈 GDP Dashboard", "🎓 Real Scholarships", "🚨 Scam Alert"])

@st.cache_data
def get_gdp_data():
    csv_path = Path(__file__).parent / "data" / "gdp_data.csv"
    if csv_path.exists():
        return pd.read_csv(csv_path)
    # fallback demo data if no csv
    data = {
        'Country Code': ['SSD','KEN','UGA','ETH','SDN','RWA']*5,
        'Year': [2018,2018,2018,2018,2018,2018,2019,2019,2019,2019,2019,2019,2020,2020,2020,2020,2020,2020,2021,2021,2021,2021,2021,2021,2022,2022,2022,2022,2022,2022],
        'GDP (current US$)': [2.5e9, 9e10, 3.2e10, 8e10, 3e10, 1e10]*5
    }
    return pd.DataFrame(data)

with tab1:
    st.header("East Africa GDP – Live Data")
    df = get_gdp_data()
    countries = st.multiselect("Select Countries", df['Country Code'].unique().tolist() if 'Country Code' in df.columns else ["SSD","KEN","UGA","ETH","SDN","RWA"], default=["SSD","KEN","UGA","ETH","RWA"])
    try:
        import plotly.express as px
        filt = df[df['Country Code'].isin(countries)] if 'Country Code' in df.columns else df
        y_col = 'GDP (current US$)' if 'GDP (current US$)' in filt.columns else filt.columns[-1]
        x_col = 'Year' if 'Year' in filt.columns else filt.columns[1]
        fig = px.line(filt, x=x_col, y=y_col, color='Country Code' if 'Country Code' in filt.columns else None, markers=True)
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.line_chart(df)
    st.dataframe(df, use_container_width=True)

with tab2:
    st.header("Verified Scholarships – FREE, No Payment")
    st.success("Contact us: JunubLink-AI@gmail.com to add more")
    sch = pd.DataFrame([
        {"Name":"Mastercard Foundation","Level":"Undergrad/Masters","Link":"mastercardfdn.org/scholars","Fee":"FREE"},
        {"Name":"Chevening UK","Level":"Masters","Link":"chevening.org","Fee":"FREE"},
        {"Name":"DAAD Germany","Level":"Masters/PhD","Link":"daad.de","Fee":"FREE"},
        {"Name":"World Bank JJ/WBGSP","Level":"Masters","Link":"worldbank.org/scholarships","Fee":"FREE"},
        {"Name":"African Union","Level":"Masters","Link":"au.int/scholarship","Fee":"FREE"},
    ])
    st.dataframe(sch, use_container_width=True)
    st.info("Real scholarships NEVER ask for $50-$500 fee!")

with tab3:
    st.header("Scholarship Scam Alert – Protecting Juba Youth")
    st.error("Fake scholarships on Facebook/WhatsApp are stealing money in South Sudan!")
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("**❌ SCAM Signs:**\n- Asks for application fee\n- Gmail only: canada2025@gmail.com\n- Guaranteed visa\n- Pay today or lose spot")
    with c2:
        st.markdown("**✅ REAL Signs:**\n- FREE application\n- .edu/.gov/.org website\n- No money asked\n- Past winners listed")
    check = st.text_input("Paste scholarship link to check:")
    if check:
        if "gmail" in check.lower() or "whatsapp" in check.lower() or "fee" in check.lower():
            st.error("🚨 LIKELY SCAM – Report to JunubLink-AI@gmail.com")
        else:
            st.warning("Verify on official site. Ask us!")

st.divider()
st.markdown("Built by Chris2026Ss | Munuki Hub, Juba | **JunubLink-AI@gmail.com** | Live Dashboard: gdp-dashboard-h5k54ilfh5fwpk4ucnk69q.streamlit.app")
