import streamlit as st
import pickle
import os


# Load the trained model


class SessionState:
    def __init__(self):
        self.currentPage = "Home"
        
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

def predict_crop_category(model, N, P, K):
    input_data = [[N, P, K]]  # Ensure input_data is in the correct format
    predicted_crop_cat = model.predict(input_data)
    return predicted_crop_cat


# Function to display photo based on predicted category

def display_photo(predicted_category):
    if predicted_category == 1:
        st.markdown("<h3 style='text-align: center;'>You should consider growing \"Fruits\" this season !</h3>",
                    unsafe_allow_html=True)
        st.image("Fruits_merged.jpg")
        st.markdown("<h3 style='text-align: center;'>Go to the next page to know what kind of 'Fruit Crops' to grow</h3>",
            unsafe_allow_html=True)
        

    elif predicted_category == 2:
        st.markdown("<h3 style='text-align: center;'>You should consider growing \"Cereals\" this season !</h3>",
                    unsafe_allow_html=True)
        st.image("cereals.png")
        st.markdown("<h3 style='text-align: center;'>Check out the next page to know what kind of 'Cereals' to grow</h2>",
                    unsafe_allow_html=True)
        

       
    elif predicted_category == 3:
        st.markdown("<h3 style='text-align: center;'>You should consider growing \"Lentils\" this season !</h3>",
                    unsafe_allow_html=True)
        st.image("lentils.jpg")
        st.markdown("<h3 style='text-align: center;'>Check out the next page to know what kind of 'Lentils' to grow</h2>",
                    unsafe_allow_html=True)
        
     
    elif predicted_category == 4:
        st.markdown("<h3 style='text-align: center;'>You should consider growing \"Fibre Crops\" this season !</h3>",
                    unsafe_allow_html=True)
        st.image("fibre_merged.jpg")
        st.markdown("<h3 style='text-align: center;'>Check out the next page to know what kind of 'Fibre Crops' to grow</h2>",
                    unsafe_allow_html=True)
        

      
    else:
        st.write('Unknown Crop')
        
        
set_bg_hack_url()
session_state = SessionState()
st.title('Welcome New Farmer')
st.subheader('Please enter your primary soil profile')

N = st.slider('Enter soil N content (0-140)', min_value=0, max_value=140, step=1)
P = st.slider('Enter soil P content (5-95)', min_value=5, max_value=95, step=1)
K = st.slider('Enter soil K content (15-85)', min_value=15, max_value=85, step=1)

if st.button('What kind of crops are best for your soil'):
    model = pickle.load(open('trained model/pre_pipe.sav', 'rb'))
    predicted_category = predict_crop_category(model, N, P, K)  
    display_photo(predicted_category)

if st.button("Next Page"):
    st.switch_page('pages/4_🌾_Crops_to_grow.py')
    
    
    



        
