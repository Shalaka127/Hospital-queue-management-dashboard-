import streamlit as st
from src.utils.helpers import get_image_as_base64

def render_header():
    img_b64 = get_image_as_base64("assets/images/illustration.png")
    img_html = ""
    if img_b64:
        img_html = f'<img src="data:image/png;base64,{img_b64}" style="width: 100%; max-width: 500px; height: auto;" />'

    header_html = f'''
    <div style="display: flex; align-items: center; justify-content: space-between; padding: 5px 0px 15px 0px;">
        <div style="flex: 1; padding-right: 10px;">
            <h1 style="color:#314842; font-size: 3.1rem; font-weight:bold; line-height: 1.1; margin: 0; padding: 0;">Hospital Queue Optimization Dashboard</h1>
            <p style="color:#666; font-size:1.3rem; margin: 10px 0 0 0;">Using M/M/c Model with Priority Queue</p>
        </div>
        <div style="flex: 0 0 45%; display: flex; justify-content: flex-end; padding-right: 20px;">
            {img_html}
        </div>
    </div>
    '''
    st.markdown(header_html, unsafe_allow_html=True)
