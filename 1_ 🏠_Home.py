import streamlit as st



def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(https://img.freepik.com/free-photo/plant-green-small-hope-cultivated_1172-190.jpg?w=826&t=st=1707385027~exp=1707385627~hmac=cde7a95c46e7c49b2d53d6527fb675d6b7ce0fc4159907b6ffa5e71737744806) no-repeat center center fixed;
             background-size: cover;
             opacity: 0.9; /* Adjust the opacity value (0.0 - 1.0) */
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
set_bg_hack_url()
    #st.set_page_config(layout="wide")
    
    # Position the text on the left side of the page
    #st.markdown('<div style="position: absolute; left: 150px; top: 150px; color: white;">Welcome to GRO-PRO</div>', unsafe_allow_html=True)
    
    # Display the logo
st.image('logo_white.png',  use_column_width=False, width=300)
    


st.markdown('<div class="text-container"> <h1>Welcome to GRO-PRO</h1> </div>', unsafe_allow_html=True)
st.markdown('<div class="text-container"> <h3>Crop GROwth PROfessional recommendations for your farm</h3> </div>', unsafe_allow_html=True)