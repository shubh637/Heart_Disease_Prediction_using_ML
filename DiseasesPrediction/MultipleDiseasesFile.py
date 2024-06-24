import base64
import pickle
from sklearn.preprocessing import StandardScaler
import requests
import streamlit as st
from streamlit_option_menu import option_menu
import json
from streamlit_lottie import st_lottie

#streamlit run "D:\2024-06-20\DiseasesPrediction\MultipleDiseasesFile.py"
#loading the saved models

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="⚕️")

diabetics_model=pickle.load(open("./diabetic_model.sav","rb"))
heart_model=pickle.load(open("./heart_model.sav","rb"))
framingham_model=pickle.load(open("./framingham.sav","rb"))

#load lottie file using filepath
def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)

#loading lottie using the url
def load_lottieurl(url:str):
    r=requests.get(url)
    if r.status_code!=200:
        
        return None
    return r.json()
#backgrounf image path
@st.cache_data
def get_image_as_base64(file):
      with open(file,"rb") as f:
        data=f.read()
      return base64.b64encode(data).decode()  

lottie_coding=load_lottiefile("./doctor_animation.json")
heart_jason=load_lottieurl("https://lottie.host/fddbac1d-28e8-4ef0-aa62-6fae1f52dbb4/CZjsA0RgFg.json")
lottie_url=load_lottieurl("https://lottie.host/94a8638e-7c86-4f17-afb8-e9a8da81de6a/cr9RF5PmSt.json")
st.title("Health for better life")
# css

img = get_image_as_base64("./pexels-eberhardgross-2088205.jpg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{

background: linear-gradient(300deg,#7AD7F0, #B7E9F7, #ef8172);
background-size: 180% 180%;
animation: gradient-animation 18s ease infinite;

}}
[data-testid="stHeader"]{{
background:rgb(2,0,36);
color:white;
}}
[data-testid="stHeader"] > div {{
right: 2rem;
}}
[data-testid="stSidebar"] {{
background:rgb(2,0,36);
background-size: cover;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[id="health-for-better-life"],[id="diabetes-prediction-using-ml"]{{
    background:rgb(2,0,36);
    color:white;
}}


@keyframes gradient-animation {{
  0% {{
    background-position: 0% 50%;
  }}
  50% {{
    background-position: 100% 50%;
  }}
  100% {{
    background-position: 0% 50%;
  }}
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


    

#sidebar for navigation
with st.sidebar:
    selected=option_menu("Multiple Disease Prediction System using ML",
                         ["Diabetes Prediction",
                          "Heart Disease Prediction",
                          "Framingham Prediction"],
                          icons=["activity","heart","person"],
                          default_index=0)
# Set moving background

# Display a GIF image
# st.image('./hand_holds_lightbulb_swathed_in_leaves_surrounded_by_symbols_of_renewable_energy_sustainable_development_solar_wind_hydro_water_by_ipopba_gettyimages-1158790704_cso_2400x1600-100850057-orig.jpg', caption='Health', use_column_width=True)

# # Display a video
# st.video('animation.mp4', format='video/mp4')

#Diabetics Prediction Page
if (selected=="Diabetes Prediction"):
    #page title
    st_lottie(
    lottie_url,
    speed=1,
    loop=True,
    quality="high",
    height=500,
    width=1350,
    key=None,
    )

    st.title("Diabetes Prediction using ML")
    #getting the inputs form user
    st.write("Please provide the following information:")
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.number_input("Number of Pregnancies",min_value=0)
    with col2:
        Glucose=st.number_input("Glucose Level",min_value=0)         
    with col3:
        BloodPressure=st.number_input("Blood Pressure Value",min_value=0)
    with col1:
        SkinThickness=st.number_input("Skin Thickness Value",min_value=0)
    with col2:
        Insulin=st.number_input("Insulin Level",min_value=0)
    with col3:
       BMI=st.number_input("BMI Value",min_value=0.0,format="%.1f")
    with col1:
        DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Fubction value",min_value=0.0,format="%.3f")
    with col2:
        Age=st.number_input("Age of the person",min_value=0)

    #code for prediction 
    diab_diagnosis=""

    #creating a button
    if st.button("Diabetes Test Results"):
        diab_prediction=diabetics_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        print(diab_prediction[0])
        if (diab_prediction[0]==1):
            st.error("The person is likely to have diabetes.")
        else:
            st.success("The person is not likely to have diabetes.")


if (selected=="Heart Disease Prediction"):
    st_lottie(
    heart_jason,
    speed=1,
    loop=True,
    quality="high",
    height=500,
    width=1350,
    key=None,
    )

    st.title("Heart Disease Prediction using ML")

    # Collect user input
    st.write("Please provide the following information:")
      # Input fields for user data
    col1,col2,col3=st.columns(3) 
    with col1: 
       age = st.number_input("Age", min_value=0, max_value=150, step=1)
    with col2:   
       sex = st.selectbox("Sex", ["Female", "Male"])
    with col3:   
       cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    with col1:   
       trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, step=1)
    with col2:   
       chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=0, max_value=600, step=1)
    with col3:   
       fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    with col1:   
       restecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "Abnormality", "Hypertrophy"])
    with col2:   
       thalach = st.number_input("Maximum Heart Rate Achieved (bpm)", min_value=0, max_value=300, step=1)
    with col3:   
       exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    with col1:   
       oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
    with col2:   
       slope = st.selectbox("Slope of the Peak Exercise ST Segment", ["Upsloping", "Flat", "Downsloping"])
    with col3:   
       ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4, step=1)
    with col1:   
       thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

    # Convert categorical inputs to numeric
    sex = 1 if sex == "Male" else 0
    cp_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
    cp = cp_mapping[cp]
    fbs = 1 if fbs == "Yes" else 0
    restecg_mapping = {"Normal": 0, "Abnormality": 1, "Hypertrophy": 2}
    restecg = restecg_mapping[restecg]
    exang = 1 if exang == "Yes" else 0
    slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    slope = slope_mapping[slope]
    thal_mapping = {"Normal": 0, "Fixed Defect": 1, "Reversible Defect": 2}
    thal = thal_mapping[thal]

    # Predict button
    if st.button("Heart Test Results"):
        input_df = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_model.predict([input_df])
        if prediction[0] == 1:
            st.error("The person is likely to have heart disease.")
        else:
            st.success("The person is not likely to have heart disease.")


if selected == "Framingham Prediction":
    st_lottie(
    lottie_coding,
    speed=1,
    loop=True,
    quality="high",
    height=500,
    width=1350,
    key=None,
    )
    st.title("Framingham Disease Prediction using ML")
    st.write("Please provide the following information:")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
    with col2:
        age = st.number_input("Age", min_value=20, max_value=100, step=1)
    with col3:
        education = st.selectbox("Education Level", ["Less than High School","High School Diploma or Equivalent", "College", "Bachelor's Degree or Higher"])
    with col1:
        currentSmoker = st.selectbox("Current Smoker", ["No", "Yes"])
    with col2:
        cigsPerDay = st.number_input("Cigarettes per Day", min_value=0, max_value=70, step=1)
    with col3:
        BPMeds = st.selectbox("Blood Pressure Medication", ["No", "Yes"])
    with col1:
        prevalentStroke = st.selectbox("Prevalent Stroke", ["No", "Yes"])
    with col2:
        prevalentHyp = st.selectbox("Prevalent Hypertension", ["No", "Yes"])
    with col3:
        diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    with col1:
        totChol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=600, step=1)
    with col2:
        sysBP = st.number_input("Systolic Blood Pressure (mm Hg)", min_value=80, max_value=300, step=1)
    with col3:
        diaBP = st.number_input("Diastolic Blood Pressure (mm Hg)", min_value=40, max_value=200, step=1)
    with col1:
        BMI = st.number_input("BMI", min_value=10.0, max_value=70.0, step=0.1)
    with col2:
        heartRate = st.number_input("Heart Rate (bpm)", min_value=30, max_value=200, step=1)
    with col3:
        Glucose = st.number_input("Glucose", min_value=30, max_value=200, step=1)
    # Convert categorical inputs to numeric
    gender = 1 if gender == "Male" else 0
    education_mapping = {"Less than High School":1,"High School Diploma or Equivalent":2, "College":3, "Bachelor's Degree or Higher":4}
    education = education_mapping[education]
    currentSmoker = 1 if currentSmoker == "Yes" else 0
    BPMeds = 1 if BPMeds == "Yes" else 0
    prevalentStroke = 1 if prevalentStroke == "Yes" else 0
    prevalentHyp = 1 if prevalentHyp == "Yes" else 0
    diabetes = 1 if diabetes == "Yes" else 0

    if st.button("Framingham Test Results"):
        input_df = [gender,age,education,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,Glucose]
        prediction = framingham_model.predict([input_df])
        if prediction[0] == 1:
            st.error("The person is likely to have framhaming disease.")
        else:
            st.success("The person is not likely to have framhaming disease.")

    







