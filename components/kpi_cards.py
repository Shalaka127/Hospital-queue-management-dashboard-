import streamlit as st

def kpi_card(label, value, value_color="#314842", value_size="2.2rem"):
    return f'''
    <div style="background-color: #FFFFFF; padding: 15px 20px; border-radius: 12px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05); border-left: 5px solid #CCA33A; height: 100%;">
        <p style="margin:0; font-size: 1.0rem; color: #666;">{label}</p>
        <p style="margin:0; font-size: {value_size}; font-weight: bold; color: {value_color};">{value}</p>
    </div>
    '''

def render_kpi_cards(rho, status, metrics):
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(kpi_card("Utilization (ρ)", f"{rho:.2f}"), unsafe_allow_html=True)
    with col2:
        status_hex = "green" if status == "Underloaded" else ("#FFC300" if status == "Stable" else "red")
        st.markdown(kpi_card("System Status", status, value_color=status_hex, value_size="2.2rem"), unsafe_allow_html=True)
    with col3:
        st.markdown(kpi_card("Avg Waiting Time", f"{metrics['avg_wait_mins']:.1f} mins"), unsafe_allow_html=True)
    with col4:
        st.markdown(kpi_card("Avg Queue Length", f"{metrics['avg_q_len']:.1f} pts"), unsafe_allow_html=True)
