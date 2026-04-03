import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def render_graphs(metrics, priority_enabled):
    st.markdown("<h2 style='color:#314842; font-weight:bold; font-size: 1.8rem;'>System Behavior Analysis</h2>", unsafe_allow_html=True)
    
    # Row 1
    col_graph1, col_graph2 = st.columns(2)
    with col_graph1:
        st.markdown("<h3 style='font-size: 1.25rem; color:#666; margin-bottom: 0px;'>Queue Length vs Time</h3>", unsafe_allow_html=True)
        q_df = metrics['queue_df']
        if not q_df.empty:
            fig1 = px.line(q_df, x='Time', y='Queue Length', 
                           labels={'Time': 'Simulation Time (hours)', 'Queue Length': 'Number of Patients in Queue'}, 
                           color_discrete_sequence=['#CCA33A'])
            fig1.update_layout(height=350, margin=dict(l=0, r=0, t=10, b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig1, use_container_width=True)
        else:
            st.info("No queue length data available.")

    with col_graph2:
        st.markdown("<h3 style='font-size: 1.25rem; color:#666; margin-bottom: 0px;'>Waiting Time Distribution</h3>", unsafe_allow_html=True)
        patients_df = metrics['patients_df']
        if not patients_df.empty:
            fig2 = px.histogram(patients_df, x='Waiting Time (mins)', nbins=20, 
                                color_discrete_sequence=['#3F5A54'],
                                labels={'Waiting Time (mins)': 'Waiting Time (minutes)'})
            fig2.update_layout(height=350, margin=dict(l=0, r=0, t=10, b=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig2, use_container_width=True)
        else:
            st.info("No patient data available.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Row 2
    col_graph3, col_graph4 = st.columns(2)
    with col_graph3:
        st.markdown("<h3 style='font-size: 1.25rem; color:#666; margin-bottom: 0px;'>Doctor Utilization</h3>", unsafe_allow_html=True)
        util_pct = metrics['doc_util'] * 100
        fig3 = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = util_pct,
            number = {'suffix': "%", 'valueformat': ".1f", 'font': {'color': '#314842'}},
            gauge = {
                'axis': {'range': [0, 100]},
                'bar': {'color': "#CCA33A"},
                'steps': [
                    {'range': [0, 70], 'color': "#EDF3F1"},
                    {'range': [70, 99.9], 'color': "#C2D5D0"},
                    {'range': [99.9, 100], 'color': "#3F5A54"}
                ]
            }
        ))
        fig3.update_layout(height=350, margin=dict(l=20, r=20, t=20, b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig3, use_container_width=True)
        st.caption("**Ideal utilization range: 70% – 85%**")

    with col_graph4:
        st.markdown("<h3 style='font-size: 1.25rem; color:#666; margin-bottom: 0px;'>Priority Comparison</h3>", unsafe_allow_html=True)
        if priority_enabled:
            comp_df = pd.DataFrame({
                'Patient Type': ['Emergency', 'Normal'],
                'Avg Waiting Time (mins)': [metrics['emer_wait_mins'], metrics['norm_wait_mins']]
            })
            fig4 = px.bar(comp_df, x='Patient Type', y='Avg Waiting Time (mins)', 
                          color='Patient Type',
                          color_discrete_map={'Emergency': '#CCA33A', 'Normal': '#3F5A54'})
            fig4.update_layout(height=350, margin=dict(l=0, r=0, t=10, b=0), showlegend=False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("Priority Queue is disabled. Enable it from the sidebar to view Emergency vs Normal patient comparison.")
