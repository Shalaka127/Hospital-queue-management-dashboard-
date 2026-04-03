import streamlit as st

def render_footer():
    footer_html = """
    <hr style="margin-top: 50px; border: 0.5px solid #E0E0E0;">
    <div style="text-align: center; padding: 20px 0; color: #666; font-size: 0.9rem;">
        <p style="margin: 0;">© 2024 All Rights Reserved</p>
        <p style="margin: 5px 0;">
            Made by <b>Shalaka Gangurde</b> (22108B0027) and <b>Sarthak Mokal</b> (22108B0017)
        </p>
        <p style="margin: 5px 0; font-style: italic; color: #314842; font-weight: bold;">
            Vidyalankar Institute of Technology
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)
