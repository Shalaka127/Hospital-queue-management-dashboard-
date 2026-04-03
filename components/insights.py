import streamlit as st
import math

def insight_box(title, content, border_color):
    return f'''
    <div style="background-color: #FFFFFF; padding: 20px; border-radius: 12px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.05); border-top: 4px solid {border_color}; height: 100%;">
        <p style="margin:0; font-size: 1.15rem; font-weight: bold; color: #314842; margin-bottom: 8px;">{title}</p>
        <p style="margin:0; font-size: 1.05rem; color: #444; line-height:1.5;">{content}</p>
    </div>
    '''

def render_insights(lam, mu, c, rho):
    c_required = math.ceil(lam / mu)
    st.markdown("<h2 style='color:#314842; font-weight:bold; font-size: 1.8rem;'>Decision Support & Insights</h2>", unsafe_allow_html=True)
    
    rec_col, int_col = st.columns(2)
    
    with rec_col:
        if c < c_required:
            rec_html = insight_box("Actionable Recommendation", f"<b>System is overloaded.</b> Increase doctors to at least <b>{c_required}</b> to stabilize.", "red")
        elif 0.7 <= rho <= 1.0:
            rec_html = insight_box("Actionable Recommendation", "<b>System is operating efficiently.</b> Minor queues may occur.", "#FFC300")
        else:
            rec_html = insight_box("Actionable Recommendation", "<b>System is underutilized.</b> Consider reducing resources.", "green")
        st.markdown(rec_html, unsafe_allow_html=True)
    
    with int_col:
        if rho > 1:
            int_html = insight_box("System Interpretation", "<b>Demand exceeds capacity.</b> Queue will continuously grow.", "red")
        elif 0.8 <= rho <= 0.9:
            int_html = insight_box("System Interpretation", "<b>Doctors are highly utilized.</b> System is efficient but may experience occasional delays.", "#FFC300")
        elif rho < 0.7:
            int_html = insight_box("System Interpretation", "<b>Doctors are idle most of the time.</b> Resources may be wasted.", "green")
        else:
            int_html = insight_box("System Interpretation", "<b>System is moderately utilized.</b> Load is balanced.", "#FFC300")
        st.markdown(int_html, unsafe_allow_html=True)
