import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Configure page
st.set_page_config(
    page_title='JunubLink AI Portal',
    page_icon=':earth_africa:',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# HEADER
st.title("JunubLink AI - Africa Youth Tech Education Innovation")
st.markdown("**Munuki Hub, Juba | JunubLink-AI@gmail.com | GDP + Scholarships + Scam Alert**")
st.divider()

# Create tabs
tab1, tab2, tab3 = st.tabs(["📈 GDP Dashboard", "🎓 Real Scholarships", "🚨 Scam Alert"])

# ============================================================================
# GDP DATA FUNCTION
# ============================================================================

@st.cache_data(ttl=3600)
def get_gdp_data():
    """Load GDP data from CSV or return demo fallback data."""
    csv_path = Path(__file__).parent / "data" / "gdp_data.csv"
    
    try:
        if csv_path.exists():
            df = pd.read_csv(csv_path)
            if not df.empty:
                return df
    except Exception as e:
        st.warning(f"Could not load CSV: {e}. Using demo data.")
    
    # Fallback demo data for East Africa
    return pd.DataFrame({
        'Country Code': ['SSD', 'KEN', 'UGA', 'ETH', 'SDN', 'RWA'] * 5,
        'Year': [2018]*6 + [2019]*6 + [2020]*6 + [2021]*6 + [2022]*6,
        'GDP (current US$)': [2.5e9, 9e10, 3.2e10, 8e10, 3e10, 1e10] * 5,
        'Country Name': ['South Sudan', 'Kenya', 'Uganda', 'Ethiopia', 'Sudan', 'Rwanda'] * 5
    })

# ============================================================================
# TAB 1: GDP DASHBOARD
# ============================================================================

with tab1:
    st.header("East Africa GDP – Live Data")
    
    try:
        df = get_gdp_data()
        
        if df.empty:
            st.error("No GDP data available.")
        else:
            # Get unique countries
            countries = sorted(df['Country Code'].unique().tolist())
            default_countries = [c for c in ['SSD', 'KEN', 'UGA', 'ETH', 'RWA'] if c in countries]
            
            # Country selector
            selected_countries = st.multiselect(
                "Select Countries",
                countries,
                default=default_countries if default_countries else countries[:3]
            )
            
            if selected_countries:
                # Filter data
                filtered_df = df[df['Country Code'].isin(selected_countries)].copy()
                
                # Plot using Plotly
                try:
                    fig = px.line(
                        filtered_df,
                        x='Year',
                        y='GDP (current US$)',
                        color='Country Code',
                        markers=True,
                        title="GDP Trends (Current US$)",
                        labels={'GDP (current US$)': 'GDP (US$)'}
                    )
                    fig.update_layout(height=500)
                    st.plotly_chart(fig, use_container_width=True)
                except Exception as e:
                    st.error(f"Could not create chart: {e}")
                
                # Data table
                st.subheader("Data Table")
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.info("Please select at least one country.")
    
    except Exception as e:
        st.error(f"Error loading GDP dashboard: {e}")

# ============================================================================
# TAB 2: SCHOLARSHIPS
# ============================================================================

with tab2:
    st.header("Verified Scholarships – FREE, No Payment")
    st.success("✅ Contact us: JunubLink-AI@gmail.com to add more scholarships")
    
    try:
        scholarships = pd.DataFrame([
            {
                "Name": "Mastercard Foundation",
                "Level": "Undergrad/Masters",
                "Website": "mastercardfdn.org/scholars",
                "Fee": "FREE"
            },
            {
                "Name": "Chevening (UK Government)",
                "Level": "Masters",
                "Website": "chevening.org",
                "Fee": "FREE"
            },
            {
                "Name": "DAAD (Germany)",
                "Level": "Masters/PhD",
                "Website": "daad.de",
                "Fee": "FREE"
            },
            {
                "Name": "World Bank Scholarships",
                "Level": "Masters",
                "Website": "worldbank.org/scholarships",
                "Fee": "FREE"
            },
            {
                "Name": "African Union",
                "Level": "Masters/PhD",
                "Website": "au.int/scholarship",
                "Fee": "FREE"
            },
        ])
        
        st.dataframe(scholarships, use_container_width=True)
        st.info("⚠️ Real scholarships NEVER ask for $50–$500 application fees!")
    
    except Exception as e:
        st.error(f"Error loading scholarships: {e}")

# ============================================================================
# TAB 3: SCAM ALERT
# ============================================================================

with tab3:
    st.header("Scholarship Scam Alert – Protecting Juba Youth")
    st.error("🚨 Fake scholarships on Facebook/WhatsApp are stealing money in South Sudan!")
    
    try:
        # Two-column comparison
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(
                """**❌ RED FLAGS – SCAM SIGNS:**
- Asks for application/processing fee ($50–$500)
- Uses Gmail/free email only (canada2025@gmail.com, uk_scholarship@gmail.com)
- Guarantees visa or acceptance
- "Pay today or lose your spot" pressure
- No official website or LinkedIn verification
- Broken English, poor grammar
"""
            )
        
        with c2:
            st.markdown(
                """**✅ GREEN LIGHTS – REAL SIGNS:**
- Completely FREE application
- Official .edu, .gov, or .org website
- No money requested at any stage
- Past winners listed on website
- Professional communication
- Verifiable on LinkedIn & official channels
- Transparent selection process
"""
            )
        
        st.divider()
        
        # Scam checker
        st.subheader("Quick Scam Check")
        check_url = st.text_input(
            "Paste a scholarship link or email to check:",
            placeholder="e.g., canada2025@gmail.com or https://example-scholarship.com"
        )
        
        if check_url:
            is_likely_scam = any(
                keyword in check_url.lower()
                for keyword in ['gmail.com', 'yahoo.com', 'hotmail.com', 'whatsapp', 'fee', 'pay now', 'deposit']
            )
            
            if is_likely_scam:
                st.error(
                    "🚨 **LIKELY SCAM** – Report this to:\n"
                    "- JunubLink-AI@gmail.com\n"
                    "- Facebook Scam Reporting\n"
                    "- Local authorities"
                )
            else:
                st.warning(
                    "⚠️ Verify on the official website. Ask us if unsure!\n"
                    "Email: JunubLink-AI@gmail.com"
                )
    
    except Exception as e:
        st.error(f"Error loading Scam Alert: {e}")

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown(
    "Built by Chris2026Ss | Munuki Hub, Juba | "
    "**JunubLink-AI@gmail.com** | "
    "[Live Dashboard](https://gdp-dashboard-h5k54ilfh5fwpk4ucnk69q.streamlit.app)"
)
