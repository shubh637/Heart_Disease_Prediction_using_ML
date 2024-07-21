import base64
from  datetime import datetime
from io import BytesIO
import pickle
# from tkinter import Image
from sklearn.preprocessing import StandardScaler
import requests
import pandas as pd
from PIL import Image as PILImage
import streamlit as st
from streamlit_option_menu import option_menu
import json
import sqlite3
import bcrypt
import secrets
import time as delay
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import wikipedia 
import streamlit.components.v1 as components



# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="⚕️")   
from webpart import *
import sqlite3
# Initialize session state variables


# Function to create user table if it doesn't exist
def create_user_table():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    
    # Create users table if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password_hash TEXT, history TEXT)''')
    
    conn.commit()
    conn.close()

def create_test_history_table():
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS test_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT,
                 disease TEXT,
                 timestamp TEXT,
                 result TEXT,
                 symptoms TEXT)''')
    conn.commit()
    conn.close()
# Function to add a user to the database with hashed password
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()

# Function to validate user credentials
def validate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    if user and bcrypt.checkpw(password.encode('utf-8'), user[1].encode('utf-8')):
        return user[0]  # Return user ID or any other identifier
    return None

# Function to check if user is logged in based on session state
def is_logged_in():
    return st.session_state.username is not None and st.session_state.token is not None
def save_test_history(username, disease, timestamp, result, dataframe):
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    
    # Ensure the table exists before inserting data
    c.execute('''CREATE TABLE IF NOT EXISTS test_history
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 username TEXT,
                 disease TEXT,
                 timestamp TEXT,
                 result TEXT,
                 symptoms TEXT)''')
    
    # Convert dataframe to a JSON string and store it in the 'symptoms' column
    symptoms_json = dataframe.to_json(orient='records')
    
    c.execute("INSERT INTO test_history (username, disease, timestamp, result, symptoms) VALUES (?, ?, ?, ?, ?)",
              (username, disease, timestamp, result, symptoms_json))
    conn.commit()
    conn.close()
def clear_history():
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute("DELETE FROM test_history WHERE username = ?", (st.session_state.username,))
    conn.commit()
    conn.close()    
def display_history():
    components.html(history_value,height=400)
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute("SELECT username, disease, timestamp, result,symptoms FROM test_history WHERE username = ?", (st.session_state.username,))
    history = c.fetchall()
    conn.close()
    if history:
        
        st.title("Test History")
        for test in reversed(history):
            st.write(f"**Username:** {test[0]}")
            st.write(f"**Date:** {test[2]}")  # assuming timestamp is the third column (index 2)
            st.write(f"**Disease:** {test[1]}")  # assuming disease is the second column (index 1)
            st.write(f"**Result:** {test[3]}")  # assuming result is the fourth column (index 3)
            symptoms_df = pd.read_json(test[4])  # Convert JSON back to DataFrame
            st.write(f"**Symptoms:**")
            st.dataframe(symptoms_df)
            
            st.write("---")
      # Add a button to clear history
        if st.button("Clear History"):
            clear_history()
            st.success("History cleared successfully.")
            st.rerun()  # Reloads the app to reflect changes after clearing history
    else:
        st.write("No test history found.")
    
    conn.close()
    
# Create user table if it doesn't exist
create_user_table()

diabetics_model=pickle.load(open("./models/diabeticdisease_model.sav","rb"))
heart_model=pickle.load(open("./models/heart_model.sav","rb"))
framingham_model=pickle.load(open("./models/framingham.sav","rb"))
any_model = pickle.load(open("./models/any_model.sav","rb"))
doctor_df = pd.read_csv('./data and predictions/doctors.csv') 


# Login page
def login_page():
    components.html(login_image,height=460)
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        if not username or not password:
            st.error("Username and password cannot be empty")
            return

        user_id = validate_user(username, password)

        if user_id is not None:
            token = secrets.token_hex(16)
            st.success(f"Logged in as {username}")
            st.session_state.logged_in = True
            st.session_state.user_id = user_id
            st.session_state.username = username
            st.session_state.token = token
            st.session_state.page = 'start'
            st.rerun()

            
            
        else:
            st.error("Invalid username or password")

# Signup page
def signup_page():
    components.html(sign_image,height=460)
    st.title("Sign Up")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if new_password != confirm_password:
        st.error("Passwords do not match")
        return

    if st.button("Sign Up"):
        if not new_username or not new_password:
            st.error("Username and password cannot be empty")
        else:
            # Check if username already exists
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE username = ?", (new_username,))
            existing_user = c.fetchone()

            if existing_user:
                st.error("Username already exists. Please choose another.")
            else:
                # Add user to database
                add_user(new_username, new_password)
                st.success("User successfully registered. Please log in.")
                st.session_state.page = 'select'

if 'page' not in st.session_state:
    st.session_state.page = 'select'
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("Disease Prediction System")

def start():
    #sidebar for navigation
    with st.sidebar:
        selected=option_menu("Multiple Disease Prediction System using ML",
                             ["Home","Disease Predictor","Diabetes Prediction",
                              "Heart Disease Prediction",
                              "Cardiovascular Disease Prediction","History",
                              "LogOut"],
                              icons=["house","capsule","activity","heart","person","book","box-arrow-right"],
                              default_index=0)
        st.session_state.selected = selected
    if  st.session_state.selected=="Home":
        components.html(hover+bootstrap,height=3000) 

    if st.session_state.selected=="Disease Predictor":
        any_disease()
    elif st.session_state.selected == "Diabetes Prediction":
        diabetes_prediction_page()
    elif st.session_state.selected == "Heart Disease Prediction":
        heart_disease_prediction_page()
    elif st.session_state.selected == "Cardiovascular Disease Prediction":
        framingham_prediction_page()   
    elif st.session_state.selected=="History":
        display_history()    
    elif st.session_state.selected=="LogOut":
        st.session_state.username = None
        st.session_state.token = None
        st.session_state.page = 'select'
        st.rerun() 


# Function to get doctor information based on disease
def get_doctor_info(disease):
    try:
        doctors = doctor_df[doctor_df['Disease'] == disease]
        if not doctors.empty:
            return doctors.to_dict('records')[0]  # Return the first matching doctor as a dictionary
        else:
            return {"error": "No doctors found for this disease"}
    except Exception as e:
        return {"error": str(e)}
def save_appointment_to_csv(data, csv_file):
    # Convert the data dictionary to a DataFrame with one row
    new_data = pd.DataFrame([data])
    
    try:
        # Read the existing CSV file
        df = pd.read_csv(csv_file)
        # Append the new data to the existing DataFrame
        df = pd.concat([df, new_data], ignore_index=True)
    except FileNotFoundError:
        # If the file does not exist, create a new DataFrame from the new data
        df = new_data
    
    # Save the updated DataFrame to the CSV file
    df.to_csv(csv_file, index=False)
def any_disease():
    
    # Define symptoms and diseases
    l1 = ['back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
      'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
      'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
      'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',
      'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
      'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs',
      'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails',
      'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips',
      'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints',
      'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness',
      'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine',
      'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',
      'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
      'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria',
      'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances',
      'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding',
      'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum',
      'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads',
      'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails',
      'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

    disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction',
           'Peptic ulcer diseae', 'AIDS', 'Diabetes', 'Gastroenteritis', 'Bronchial Asthma',
           'Hypertension', 'Migraine', 'Cervical spondylosis', 'Paralysis (brain hemorrhage)',
           'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A',
           'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis',
           'Tuberculosis', 'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)',
           'Heart attack', 'Varicose veins', 'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
           'Osteoarthristis', 'Arthritis', '(vertigo) Paroymsal  Positional Vertigo', 'Acne',
           'Urinary tract infection', 'Psoriasis', 'Impetigo']
    components.html(first_page_image,height=600)
    st.title("Disease Prediction")

    # User input for symptoms
    selected_symptoms = []
    st.subheader("Select Symptoms:")
    
    # Add 5 initial symptoms with selectbox
    for i in range(5):
        symptom = st.selectbox(f"Symptom {i+1}", l1)
        selected_symptoms.append(symptom)
    
    # Option to add more symptoms dynamically
    add_more = st.checkbox("Add More Symptoms")
    if add_more:
        additional_symptoms = st.text_input("Enter additional symptoms (comma-separated)", "")
        if additional_symptoms:
            additional_symptoms = [sym.strip() for sym in additional_symptoms.split(",")]
            selected_symptoms.extend(additional_symptoms)

   # Predict disease on button click
   
    formbtn = st.button("Predict Disease")

    if "formbtn_state" not in st.session_state:
         st.session_state.formbtn_state = False

    if formbtn or st.session_state.formbtn_state:
        st.session_state.formbtn_state = True
        # Initialize l2 to represent symptom presence
        l2 = [0] * len(l1)
        for k in range(len(l1)):
            if l1[k] in selected_symptoms:
                l2[k] = 1

        # Make prediction
        inputtest = [l2]
        predicted = any_model.predict(inputtest)[0]

        # Find predicted disease
        h = 'Not Found'
        for a in range(len(disease)):
            if predicted == a:
                h = disease[a]
                break

        # Display result
        st.subheader("Prediction Result:")
        if 'username' not in st.session_state or not st.session_state.username:
            st.error("Please Log In")
            st.session_state.page="Login"
        else: 
            symptoms_df=pd.DataFrame({"Symptoms":selected_symptoms})
            save_test_history(st.session_state.username,h, datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"positive",symptoms_df)
            st.success(f"Predicted Disease: {h}") 
            try:
                wiki_page = wikipedia.page(h)
                st.subheader(f"More Information about {h}:")
                st.write(wiki_page.summary[:600],"...")  

                st.write(f"Read more on [Wikipedia]({wiki_page.url})")
            
            except wikipedia.DisambiguationError as e:
                st.warning(f"More than one '{h}' found. Please be more specific.")
            except wikipedia.PageError as e:
                st.warning(f"No information found for '{h}' on Wikipedia.") 
        # Fetch doctor information
        form_function(h)
        

def form_function(disease):
        default_photo_url = "https://via.placeholder.com/50"  # URL of the default image
        csv_file="./data and predictions/paitent_appointments.csv"
        doctor_info = get_doctor_info(disease)

        if doctor_info and "error" not in doctor_info:
            
        
        # Display appointment form
            st.title("Appointment Form")
            with st.form(key='appointment_form'):
                st.subheader("Doctor Information:")
                col1,col2=st.columns(2)
           
                photo_url = doctor_info.get("Photo", default_photo_url)
                with col2:
                    if not photo_url:
                        photo_url = default_photo_url
        
                    st.image(photo_url, caption=f"Dr. {doctor_info['Doctor Name']}", width=300)  # Adjust width for smaller image
                with col1:
                    for key, value in doctor_info.items():
                        if key != "Photo_url":  # Skip the photo key while displaying other information
                            st.write(f"**{key}:** {value}")
                st.subheader("Make an Appointment:")
                name = st.text_input("Your Name", key="name")
                contact = st.text_input("Your Contact", key="contact")
                email = st.text_input("Your Email", key="email")
                date = st.date_input("Preferred Appointment Date", key="date")
                time = st.time_input("Preferred Appointment Time", key="time")
                col1,col2=st.columns(2)
                with col1:    
                    submit_button = st.form_submit_button(label='Submit')
                with col2:    
                    close_button = st.form_submit_button(label='Close')
                if close_button:
                    st.success(f"Closing the Form")
                    delay.sleep(2)
                    st.session_state.formbtn_state = False                           
                    st.rerun()
                if submit_button:
                        if name and contact and email:    
                            
                            appointment_data = {
                                "Disease": disease,
                                "Doctor Name": doctor_info["Doctor Name"],
                                "Specialization": doctor_info["Specialization"],
                                "Contact": doctor_info["Contact"],
                                "Address": doctor_info["Address"],
                                "Email": doctor_info["Email"],
                                "Patient Name": name,
                                "Patient Contact": contact,
                                "Patient Email": email,
                                "Appointment Date": date.strftime("%Y-%m-%d"),
                                "Appointment Time": time.strftime("%H:%M:%S")
                            }
                            save_appointment_to_csv(appointment_data, csv_file)
                            st.success(f"Appointment requested for {name} with Dr. {doctor_info['Doctor Name']} on {date} at {time}.")
                            delay.sleep(3)
                            st.session_state.formbtn_state = False                           
                            st.rerun()
                            
                           
                        else:
                            st.error("Please fill in all fields.")   

        else: 
            st.error(doctor_info["error"])

def diabetes_prediction_page():
    components.html(second_page_image,height=600)
    st.title("Diabetes Prediction using ML")
    st.write("Please provide the following information:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0)         
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value", min_value=0)
    with col1:
        SkinThickness = st.number_input("Skin Thickness Value", min_value=0)
    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0)
    with col3:
        BMI = st.number_input("BMI Value", min_value=0.0, format="%.1f")
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value", min_value=0.0, format="%.3f")
    with col2:
        Age = st.number_input("Age of the person", min_value=0)

    if st.button("Diabetes Test Results"):
        diab_prediction = diabetics_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        st.session_state.diab_prediction = diab_prediction[0]
        result="Positive" if  diab_prediction[0]==1 else "Nagative"
        if 'username' not in st.session_state or not st.session_state.username:
            st.error("Please Log In")
            st.session_state.page="Login"
        else: 
            diabetic_df=pd.DataFrame({"Number of Pregnancies":[Pregnancies],"Glucose Level":[Glucose], "Blood Pressure Value":[BloodPressure], "Skin Thickness Value":[SkinThickness], "Insulin Level":[Insulin], "BMI Value":[BMI], "Diabetes Pedigree Function value":[DiabetesPedigreeFunction], "Age of the person":[Age]})   
            save_test_history(st.session_state.username, "Diabetes", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result, diabetic_df)
            st.session_state.page = 'diabetes_result'
            st.rerun()

def heart_disease_prediction_page():
    components.html(third_page_image,height=600)
    st.title("Heart Disease Prediction using ML")
    st.write("Please provide the following information:")
    
    col1, col2, col3 = st.columns(3)
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

    if st.button("Heart Test Results"):
        input_df = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        prediction = heart_model.predict([input_df])
        st.session_state.heart_prediction = prediction[0]
        result="Positive" if  prediction[0]==1 else "Nagative"
        if 'username' not in st.session_state or not st.session_state.username:
            st.error("Please Log In")
            st.session_state.page="Login"
        else:
            heart_df=pd.DataFrame({"Age":[age],"Sex":[sex], "Chest Pain Type":[cp], "Resting Blood Pressure (mm Hg)":[trestbps], "Serum Cholesterol (mg/dl)":[chol], "Fasting Blood Sugar > 120 mg/dl":[fbs], "Resting Electrocardiographic Results":[restecg], "Maximum Heart Rate Achieved (bpm)":[thalach],"Exercise Induced Angina":[exang],"ST Depression Induced by Exercise":[oldpeak],"Slope of the Peak Exercise ST Segment":[slope],"Number of Major Vessels Colored by Fluoroscopy":[ca],"Thalassemia":[thal]})    
            save_test_history(st.session_state.username, "Heart Disease", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result,heart_df)
            st.session_state.page = 'heart_result'
            st.rerun()

def framingham_prediction_page():
    components.html(forth_page_image,height=600)
    st.title("Cardiovascular Disease Prediction using ML")
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

    gender = 1 if gender == "Male" else 0
    education_mapping = {"Less than High School":1,"High School Diploma or Equivalent":2, "College":3, "Bachelor's Degree or Higher":4}
    education = education_mapping[education]
    currentSmoker = 1 if currentSmoker == "Yes" else 0
    BPMeds = 1 if BPMeds == "Yes" else 0
    prevalentStroke = 1 if prevalentStroke == "Yes" else 0
    prevalentHyp = 1 if prevalentHyp == "Yes" else 0
    diabetes = 1 if diabetes == "Yes" else 0

    if st.button("Cardiovascular Disease Test Results"):
        input_df = [gender, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate, Glucose]
        prediction = framingham_model.predict([input_df])
        st.session_state.framingham_prediction = prediction[0]
        result="Positive" if  prediction[0]==1 else "Nagative"
        if 'username' not in st.session_state or not st.session_state.username:
            st.error("Please Log In")
            st.session_state.page="Login"
        else:
            cardio_df=pd.DataFrame({"Gender":[gender],"Age":[age], "Education Level":[education], "Current Smoker":[currentSmoker], "Cigarettes per Day":[cigsPerDay], "Blood Pressure Medication":[BPMeds], "Prevalent Stroke":[prevalentStroke], "Prevalent Hypertension":[prevalentHyp],"Diabetes":[diabetes],"Total Cholesterol (mg/dL)":[totChol],"Systolic Blood Pressure (mm Hg)":[sysBP],"Diastolic Blood Pressure (mm Hg)":[diaBP],"BMI":[BMI],"Heart Rate (bpm)":[heartRate],"Glucose":[Glucose]})  
            save_test_history(st.session_state.username, "Cardio Vescular Disease", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), result,cardio_df)
            st.session_state.page = 'framingham_result'
            st.rerun()

                    
def diabetes_result_page():
    if st.session_state.diab_prediction == 1:
        st.error("The person is likely to have diabetes.")
        components.html(result_image1,height=500)
        components.html(hover+result_if_page1,height=650)
        formbtn = st.button("Make Appointment")

        if "formbtn_state" not in st.session_state:
            st.session_state.formbtn_state = False

        if formbtn or st.session_state.formbtn_state:
            st.session_state.formbtn_state = True
            form_function("Diabetes")
            st.session_state.formbtn_state = False  
    else:
        st.success("The person is not likely to have diabetes.")
        components.html(no_disease_image, height=400)
        components.html(hover+result_else_page1,height=650)

    if st.button("Back to Home"):
        st.session_state.page = 'start'
        st.rerun()


def heart_result_page():
    if st.session_state.heart_prediction == 1:
        st.error("The person is likely to have heart disease.")
        components.html(result_page_image2,height=470)
        components.html(hover+heart_result_if,height=650)
        formbtn = st.button("Make Appointment")

        if "formbtn_state" not in st.session_state:
            st.session_state.formbtn_state = False

        if formbtn or st.session_state.formbtn_state:
            st.session_state.formbtn_state = True
            form_function("Heart disease")
            st.session_state.formbtn_state = False 
    else:
        st.success("The person is not likely to have heart disease.")
        components.html(no_disease_image,height=400)
        components.html(hover+heart_page_else,height=600)

    if st.button("Back to Home"):
        st.session_state.page = 'start'
        st.rerun()


def framingham_result_page():
    if st.session_state.framingham_prediction == 1:
        st.error("The person is likely to have Cardiovascular Disease.")
        components.html(cardio_page_image,height=470)
        components.html(hover+cardio_page_if,height=670)
        
        if "formbtn_state" not in st.session_state:
            st.session_state.formbtn_state = False

        if formbtn or st.session_state.formbtn_state:
            st.session_state.formbtn_state = True
            form_function("Heart disease")
            st.session_state.formbtn_state = False 
    else:
        st.success("The person is not likely to have Cardiovascular Disease.")
        
        components.html(hover+no_disease_image,height=470)
        components.html(hover+cardio_page_else,height=670)
    if st.button("Back to Home"):
        st.session_state.page = 'start'
        st.rerun()



# Determine which page to show based on session state
if st.session_state.page == 'select':
    with st.sidebar:
        selected=option_menu("Multiple Disease Prediction System using ML",
                             ["Login","Sign Up"],
                              icons=["box-arrow-in-left","person-add"],
                              default_index=0)
        st.session_state.selected = selected
    if st.session_state.selected == "Login":
        login_page()
    elif  st.session_state.selected == "Sign Up":
        signup_page()
elif st.session_state.page =='start':
    if is_logged_in():
        start()
        
    else:
        st.warning("Please login to access this page.")       

elif st.session_state.page == 'diabetes_result':
    
    diabetes_result_page()
elif st.session_state.page == 'heart_result':
   
    heart_result_page()
elif st.session_state.page == 'framingham_result':
    framingham_result_page()
 
# Display the CSS styles and HTML content using st.markdown
