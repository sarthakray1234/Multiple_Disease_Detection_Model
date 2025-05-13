import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Diease Prediction", page_icon="⚕️")

# Apply Custom CSS Styling
# Enhanced Styling
custom_css = """
<style>
/* Background with Gradient */
body {
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
    font-family: 'Roboto', sans-serif;
}

/* Sidebar Customization */
[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
    border-right: 3px solid #2563eb;
}

/* Sidebar Option Menu */
[data-testid="stSidebar"] .css-1v3fvcr {
    color: white;
    font-weight: bold;
    font-size: 1.2rem;
}

/* Button Styling */
button {
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 15px;
    border: none;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
    transition: transform 0.2s ease-in-out;
}

button:hover {
    background: linear-gradient(90deg, #1d4ed8, #2563eb);
    transform: scale(1.1);
}

/* Input Box Styling */
input {
    background-color: #334155;
    color: white;
    border: 1px solid #4b5563;
    border-radius: 8px;
    padding: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
}

/* Header Styling */
h1, h2, h3, h4, h5, h6 {
    color: #93c5fd;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
}

/* Footer and Main Menu */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

# Apply Custom CSS
st.markdown(custom_css, unsafe_allow_html=True)


# Apply Custom CSS to App
st.markdown(custom_css, unsafe_allow_html=True)


# hidding streamlit ad-ons

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# loading the saved models

diabetes_model = pickle.load(open('Models\diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('Models\heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('Models\parkinsons_model.sav', 'rb'))

lungs_disease_model = pickle.load(open('Models\lungs_disease_model.sav', 'rb'))

thyroid_model = pickle.load(open('Models\Thyroid_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Lungs Cancer Prediction',
                            'Hypo-Thyroid Prediction'],

                           icons=['activity', 'heart', 'person',
                                  'brightness-high', 'droplet-half'],

                           default_index=0)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        try:
           heart_prediction = heart_disease_model.predict([[
            float(age), float(sex), float(cp), float(trestbps), 
            float(chol), float(fbs), float(restecg), float(thalach), 
            float(exang), float(oldpeak), float(slope), float(ca), float(thal)
            ]])

           if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
           else:
            heart_diagnosis = 'The person does not have any heart disease'

        except ValueError:
            heart_diagnosis = "Please enter valid numeric inputs."

    st.success(heart_diagnosis)
    




# Parkinson's Prediction Page
# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)', format="%.2f")
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)', format="%.2f")
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)', format="%.2f")
    with col4:
        Jitter_percent = st.number_input('MDVP:Jitter(%)', format="%.4f")
    with col5:
        Jitter_Abs = st.number_input('MDVP:Jitter(Abs)', format="%.6f")
    with col1:
        RAP = st.number_input('MDVP:RAP', format="%.6f")
    with col2:
        PPQ = st.number_input('MDVP:PPQ', format="%.6f")
    with col3:
        DDP = st.number_input('Jitter:DDP', format="%.6f")
    with col4:
        Shimmer = st.number_input('MDVP:Shimmer', format="%.4f")
    with col5:
        Shimmer_dB = st.number_input('MDVP:Shimmer(dB)', format="%.4f")
    with col1:
        APQ3 = st.number_input('Shimmer:APQ3', format="%.4f")
    with col2:
        APQ5 = st.number_input('Shimmer:APQ5', format="%.4f")
    with col3:
        APQ = st.number_input('MDVP:APQ', format="%.4f")
    with col4:
        DDA = st.number_input('Shimmer:DDA', format="%.4f")
    with col5:
        NHR = st.number_input('NHR', format="%.4f")
    with col1:
        HNR = st.number_input('HNR', format="%.4f")
    with col2:
        RPDE = st.number_input('RPDE', format="%.4f")
    with col3:
        DFA = st.number_input('DFA', format="%.4f")
    with col4:
        spread1 = st.number_input('spread1', format="%.4f")
    with col5:
        spread2 = st.number_input('spread2', format="%.4f")
    with col1:
        D2 = st.number_input('D2', format="%.4f")
    with col2:
        PPE = st.number_input('PPE', format="%.4f")


    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[
                float(fo), float(fhi), float(flo), float(Jitter_percent), float(Jitter_Abs), 
                float(RAP), float(PPQ), float(DDP), float(Shimmer), float(Shimmer_dB), 
                float(APQ3), float(APQ5), float(APQ), float(DDA), float(NHR), 
                float(HNR), float(RPDE), float(DFA), float(spread1), float(spread2), 
                float(D2), float(PPE)
            ]])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

        except ValueError:
            parkinsons_diagnosis = "Please enter valid numeric inputs."

        st.success(parkinsons_diagnosis)


# Lungs Cancer Prediction Page
if (selected == "Lungs Cancer Prediction"):

    # page title
    st.title("Lungs Cancer Disease Prediction using ML")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        GENDER = st.text_input('Gender (0 for Female, 1 for Male)')
    with col2:
        AGE = st.text_input('Age')
    with col3:
        SMOKING = st.text_input('Smoking (1 for No, 2 for Yes)')
    with col4:
        YELLOW_FINGERS = st.text_input('Yellow Fingers (1 for No, 2 for Yes)')
    with col1:
        ANXIETY = st.text_input('Anxiety (1 for No, 2 for Yes)')
    with col2:
        PEER_PRESSURE = st.text_input('Peer Pressure (1 for No, 2 for Yes)')
    with col3:
        CHRONIC_DISEASE = st.text_input('Chronic Disease (1 for No, 2 for Yes)')
    with col4:
        FATIGUE = st.text_input('Fatigue (1 for No, 2 for Yes)')
    with col1:
        ALLERGY = st.text_input('Allergy (1 for No, 2 for Yes)')
    with col2:
        WHEEZING = st.text_input('Wheezing (1 for No, 2 for Yes)')
    with col3:
        ALCOHOL_CONSUMING = st.text_input('Alcohol Consuming (1 for No, 2 for Yes)')
    with col4:
        COUGHING = st.text_input('Coughing (1 for No, 2 for Yes)')
    with col1:
        SHORTNESS_OF_BREATH = st.text_input('Shortness Of Breath (1 for No, 2 for Yes)')
    with col2:
        SWALLOWING_DIFFICULTY = st.text_input('Swallowing Difficulty (1 for No, 2 for Yes)')
    with col3:
        CHEST_PAIN = st.text_input('Chest Pain (1 for No, 2 for Yes)')

    # code for Prediction
    lungs_diagnosis = ''

    # creating a button for Prediction
    if st.button("Lung's Test Result"):
        try:
            # Convert all inputs to float
            input_features = [
                float(GENDER), float(AGE), float(SMOKING), float(YELLOW_FINGERS),
                float(ANXIETY), float(PEER_PRESSURE), float(CHRONIC_DISEASE),
                float(FATIGUE), float(ALLERGY), float(WHEEZING),
                float(ALCOHOL_CONSUMING), float(COUGHING),
                float(SHORTNESS_OF_BREATH), float(SWALLOWING_DIFFICULTY), float(CHEST_PAIN)
            ]
            
            # Make prediction
            lungs_prediction = lungs_disease_model.predict([input_features])

            if lungs_prediction[0] == 1:
                lungs_diagnosis = "The person has lungs cancer disease"
            else:
                lungs_diagnosis = "The person does not have lungs cancer disease"

        except ValueError:
            lungs_diagnosis = "Please enter valid numeric inputs."

        # Display the result
        st.success(lungs_diagnosis)

# Hypo-Thyroid Prediction Page
if (selected == "Hypo-Thyroid Prediction"):

    # page title
    st.title("Hypo-Thyroid Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (0 for Female, 1 for Male)')
    with col3:
        on_thyroxine = st.text_input('On Thyroxine (0 for No, 1 for Yes)')
    with col1:
        tsh = st.text_input('TSH Level')
    with col2:
        t3_measured = st.text_input('T3 Measured (0 for No, 1 for Yes)')
    with col3:
        t3 = st.text_input('T3 Level')
    with col1:
        tt4 = st.text_input('TT4 Level')

    # code for Prediction
    thyroid_diagnosis = ''

    # creating a button for Prediction
    if st.button("Thyroid's Test Result"):
        try:
            # Convert inputs to numeric values
            input_features = [
                float(age), float(sex), float(on_thyroxine), float(tsh), 
                float(t3_measured), float(t3), float(tt4)
            ]
            
            # Make prediction
            thyroid_prediction = thyroid_model.predict([input_features])

            if thyroid_prediction[0] == 1:
                thyroid_diagnosis = "The person has Hypo-Thyroid disease"
            else:
                thyroid_diagnosis = "The person does not have Hypo-Thyroid disease"

        except ValueError:
            thyroid_diagnosis = "Please ensure all inputs are valid numeric values."

        # Display result
        st.success(thyroid_diagnosis)
