import streamlit as st
import pickle



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
# Load the model only once at the beginning
cereal_model = pickle.load(open('trained model/first_pipe.sav', 'rb'))
fruit_model = pickle.load(open('trained model/fruit_pipe.sav', 'rb'))
lentils_model = pickle.load(open('trained model/lentils_pipe.sav', 'rb'))
fibre_model = pickle.load(open('trained model/fibre_pipe.sav', 'rb'))
    
def input_features_page():
    

    # Initialize selected_crop_type if not already initialized
    if 'selected_crop_type' not in st.session_state:
        st.session_state.selected_crop_type = None
        
    recommended_crops = []

    
    
    st.title("Please provide additional features for your field and area!")
    # User input for feature values using input boxes
    N = st.slider('Enter soil N content (0-140)', min_value=0, max_value=140, step=1)
    P = st.slider('Enter soil P content (5-95)', min_value=5, max_value=95, step=1)
    K = st.slider('Enter soil K content (15-85)', min_value=15, max_value=85, step=1)
    temperature = st.slider("Enter Temperature Value", min_value=0, max_value=50, step=1, value=0)
    humidity = st.slider("Enter Humidity Value", min_value=0, max_value=100, step=1, value=0)
    ph = st.slider("Enter pH Value", min_value=0.0, max_value=14.0, step=0.1, value=7.0)
    rainfall = st.slider("Enter Rainfall Value", min_value=0, max_value=200, step=1, value=0)

    # Convert user inputs to numeric values
    N, P, K, temperature, humidity, ph, rainfall = (
        float(N),
        float(P),
        float(K),
        float(temperature),
        float(humidity),
        float(ph),
        float(rainfall),
    )

    # Button to trigger recommendation
    if st.button("Recommend Crop"):
    # Make crop recommendation
        crop_mapping = get_crop_mapping(st.session_state.selected_crop_type)
        recommended_crops = recommend_crop(
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall,
            crop_mapping,
    )
    recommended_crop_images = {
        'Rice': 'Rice.jpg',
        'Maize': 'Corn.jpg',
        'Banana':'banana.jpg',
        'Muskmelon': 'musk.jpg',
        'Watermelon': 'watermelon.jpg',
        'Chickpea': 'chickpea.jpg',
        'Mungbean': 'mung.jpg',
        'Blackgram': 'blackgram.jpg',
        'Cotton': 'cotton.jpg',
        'Jute': 'jute_2.jpg'
        # Add other crop images here based on your crop_mapping
    }
    
    
    
        # Loop through recommended crops and display them
    for crop in recommended_crops:
        st.markdown(f'<div class="text-container"> <h3>In this season {crop} will be best for your field</h3> </div>', unsafe_allow_html=True)
        image_path = recommended_crop_images.get(crop)
        if image_path:
            st.image(image_path)

    recommended_crops = [crop for crop in recommended_crops if crop in recommended_crop_images]

    
recommended_crop_cat_images = {
        'Cereals': 'cereals.png',
        'Fruits': 'Fruits_merged.jpg',
        'Lentils':'lentils.jpg',
        'Fibres': 'fibre_merged.jpg'
    }

def recommend_crop(N, P, K, temperature, humidity, ph, rainfall, crop_mapping):
    # Use the appropriate model based on the selected crop type
    model = get_model(st.session_state.selected_crop_type)

    # Use the model to make predictions
    input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
    predicted_crop = model.predict(input_data)

    # Map numerical predictions to crop names
    predicted_crop_names = [crop_mapping.get(float(p), 'Unknown Crop') for p in predicted_crop]

    return predicted_crop_names


# Function to get the appropriate model based on crop type
def get_model(selected_crop_type):
    if selected_crop_type == "Cereals":
        return cereal_model
    elif selected_crop_type == "Fruits":
        return fruit_model
    elif selected_crop_type == "Lentils":
        return lentils_model
    elif selected_crop_type == "Fibres":
        return fibre_model
    else:
        raise ValueError(f"Invalid crop type selected: {selected_crop_type}")

        

# Page to input feature values and get predictions


# Function to get the appropriate crop mapping based on crop type
def get_crop_mapping(selected_crop_type):
    if selected_crop_type == "Cereals":
        return {1.: 'Rice', 2.: 'Maize'}
    elif selected_crop_type == "Fruits":
        return {1.: 'Banana', 2.: 'Muskmelon', 3.: 'Watermelon'}
    elif selected_crop_type == "Lentils":
        return {1.: 'Chickpea', 2.: 'Mungbean', 3.: 'Blackgram'}
    elif selected_crop_type == "Fibres":
        return {1.: 'Cotton', 2.: 'Jute'}
    else:
        raise ValueError(f"Invalid crop type selected: {selected_crop_type}")

    st.title('Crops to Grow')    
    
st.title('What should you grow this season')

st.image('background.jpg')
st.header("Please select a crop category!")
if "selected_crop_type" not in st.session_state:
    st.session_state.selected_crop_type = None
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
selected_crop_type = st.selectbox("Select Crop Category", ["None", "Cereals", "Fruits", "Lentils", "Fibres"])
st.session_state.selected_crop_type = selected_crop_type
st.subheader(f"Selected Crop Type: {st.session_state.selected_crop_type}")
image_path_cat = recommended_crop_cat_images.get(selected_crop_type)
if image_path_cat:
    st.image(image_path_cat)

if st.button("Next"):
    st.session_state.selected_crop_type = selected_crop_type
    st.session_state.button_clicked = True
    st.experimental_rerun()
if st.session_state.button_clicked and st.session_state.selected_crop_type:
    input_features_page()



# Function to make crop recommendations
