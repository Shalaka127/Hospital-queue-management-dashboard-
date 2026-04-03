import streamlit as st

def render_sidebar():
    st.sidebar.markdown("<h2 style='color:white; font-weight:bold; margin-top:0px;'>Input Controls</h2>", unsafe_allow_html=True)
    
    st.sidebar.markdown("**Scenario Selection**")
    scenario = st.sidebar.selectbox("Select Scenario", [
        "Underloaded System", 
        "Stable System", 
        "Overloaded System", 
        "Custom (manual input)"
    ], label_visibility="collapsed")
    
    if scenario == "Underloaded System":
        st.session_state['lam_val'] = 10
        st.session_state['mu_val'] = 8
        st.session_state['c_val'] = 4
    elif scenario == "Stable System":
        st.session_state['lam_val'] = 20
        st.session_state['mu_val'] = 6
        st.session_state['c_val'] = 4
    elif scenario == "Overloaded System":
        st.session_state['lam_val'] = 35
        st.session_state['mu_val'] = 5
        st.session_state['c_val'] = 2
    else:
        if 'lam_val' not in st.session_state:
            st.session_state['lam_val'] = 20
            st.session_state['mu_val'] = 6
            st.session_state['c_val'] = 3
    
    disabled = scenario != "Custom (manual input)"
    
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    st.sidebar.markdown("**System Parameters**")
    lam = st.sidebar.slider("Patients arriving per hour (λ)", min_value=5, max_value=40, step=1, help="Arrival Rate", disabled=disabled, key='lam_val')
    mu = st.sidebar.slider("Patients treated per doctor per hour (μ)", min_value=4, max_value=10, step=1, help="Service Rate", disabled=disabled, key='mu_val')
    c = st.sidebar.slider("Number of Doctors (c)", min_value=1, max_value=6, step=1, disabled=disabled, key='c_val')
    sim_time = st.sidebar.slider("Simulation Time (hours)", min_value=4, max_value=16, value=10, step=1)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Priority Settings**")
    priority_enabled = st.sidebar.toggle("Enable Priority Queue (Emergency first)", value=False)
    if priority_enabled:
        emergency_pct = st.sidebar.slider("Emergency patient percentage (%)", min_value=10, max_value=30, value=20, step=1)
    else:
        emergency_pct = 0

    # System Status Calculation
    rho = lam / (c * mu)
    if rho < 0.7:
        status = "Underloaded"
        status_color = "green"
        msg = "System underutilized. Resources may be wasted."
    elif 0.7 <= rho <= 1.0:
        status = "Stable"
        status_color = "#FFC300"
        msg = "System is stable. Normal queue lengths expected."
    else:
        status = "Overloaded"
        status_color = "red"
        msg = "System is overloaded. Waiting time will increase boundlessly."

    st.sidebar.markdown("---")
    st.sidebar.subheader("System Status")
    st.sidebar.markdown(f"**Utilization (ρ):** {rho:.2f}")
    st.sidebar.markdown(f"**Status:** <span style='color:{status_color}; font-weight:bold;'>{status}</span>", unsafe_allow_html=True)
    st.sidebar.info(msg)

    return lam, mu, c, sim_time, priority_enabled, emergency_pct, rho, status
