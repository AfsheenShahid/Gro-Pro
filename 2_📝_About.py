import streamlit as st


def set_bg_hack_url_2():
    '''
    A function to set background image with transparency.
    '''
    st.markdown(
        """
        <style>
        .stApp {
            background: rgba(0, 0, 0, 0.2); /* Adjust the last value (0.0 - 1.0) to set transparency */
            background-image: url(https://images.unsplash.com/photo-1598015435328-8e948456581e?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8Y29ybiUyMGZpZWxkfGVufDB8fDB8fHww);
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


set_bg_hack_url_2()

st.title('About GRO-PRO')
    
st.markdown("### OUR VISION")
st.markdown("""
    <p style='color: black; font-size: 20px; font-weight: bold;'>With GRO-PRO, the aim is to provide intelligent machine learning based predictive models for precision agriculture to help farmers make informed decisions about the farming strategy as well as choose the most suitable crops to grow based on soil parameters. This solution reduces the use of artificial fertilizers, which is budget friendly for the farmers in addition to being a environment friendly approach.</p>
    """, unsafe_allow_html=True)
    
st.markdown("### OUR CUSTOMERS")
st.markdown("""
    <p style='color: black; font-size: 20px; font-weight: bold;'>New generation of farmers who want to upgrade the crop selection process in their generational fields and also want to make informed decisions based on their soil profile and physical field conditions.</p>
    """, unsafe_allow_html=True)
    