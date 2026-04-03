import streamlit as st
import sys
import os

# Ensure the root directory is on the path for Streamlit Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 1. Page Config
st.set_page_config(page_title="Hospital Queue Simulation", layout="wide")

# 2. Imports after set_page_config
from src.utils.helpers import load_css
from src.simulation.engine import simulate_queue
from src.analytics.metrics import calculate_metrics
from components.header import render_header
from components.sidebar import render_sidebar
from components.kpi_cards import render_kpi_cards
from components.graphs import render_graphs
from components.insights import render_insights
from components.footer import render_footer

# 3. Load Assets
load_css("assets/styles/custom.css")

# 4. Render Header
render_header()

# 5. Render Sidebar & Get Inputs
lam, mu, c, sim_time, priority_enabled, emergency_pct, rho, status = render_sidebar()

# 6. Run Simulation Logic
with st.spinner("Generating simulation discrete events..."):
    sim_data = simulate_queue(lam, mu, c, sim_time, priority_enabled, emergency_pct)
    metrics = calculate_metrics(sim_data, sim_time, c)

# 7. Render Dashboard Output
render_kpi_cards(rho, status, metrics)
st.markdown("---")
render_graphs(metrics, priority_enabled)
st.markdown("---")
render_insights(lam, mu, c, rho)
render_footer()

st.markdown("<br>", unsafe_allow_html=True)
