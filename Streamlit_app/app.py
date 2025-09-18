import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

# ============================
# Load model + encoders
# ============================
model = joblib.load('Streamlit_app/best_model.pkl')  # saved model
encoders = joblib.load('Streamlit_app/label_enc.pkl')  # dictionary with LabelEncoders

# For easier reading:
le_constructor = encoders['constructorRef']
le_driver = encoders['surname']
le_circuit = encoders['circuitRef']
le_number = encoders['number']
le_forename = encoders['forename']

st.title("🏎️ Prediction: Driver in Top 10")
st.markdown("Fill in the race information to predict if the driver will finish in the **Top 10**.")

# ============================
# Numerical inputs
# ============================
driver_avg_finish_before = st.number_input("Driver's average previous finishes", value=10.0)
grid = st.number_input("Grid position", value=5, min_value=1)
constructor_avg_finish_before = st.number_input("Team's average previous finishes", value=8.0)
driver_races_before = st.number_input("Number of previous races for the driver", value=20)
constructor_races_before = st.number_input("Number of previous races for the team", value=50)
pilot_age = st.number_input("Driver's age", value=25)
driver_track_avg = st.number_input("Driver's average on this track", value=10.0)
constructor_track_avg = st.number_input("Team's average on this track", value=10.0)
round = st.number_input("Season round", value=1)

# ============================
# Categorical inputs (LabelEncoder)
# ============================
driver_last = st.selectbox("Select driver last name", le_driver.classes_)
surname_enc = le_driver.transform([driver_last])[0]

driver_first = st.selectbox("Select driver first name", le_forename.classes_)
forename_enc = le_forename.transform([driver_first])[0]

constructor = st.selectbox("Select team", le_constructor.classes_)
constructorRef_enc = le_constructor.transform([constructor])[0]

circuit = st.selectbox("Select circuit", le_circuit.classes_)
circuitRef_enc = le_circuit.transform([circuit])[0]

car_number = st.selectbox("Car number", le_number.classes_)
number_enc = le_number.transform([car_number])[0]

# ============================
# Boolean inputs (0/1)
# ============================
constructor_home_race = st.checkbox("Is this a home race for the team?") * 1
driver_home_race = st.checkbox("Is this a home race for the driver?") * 1

# ============================
# Build input vector
# ============================
input_data = np.array([[
number_enc,
constructor_races_before,
driver_avg_finish_before,
driver_races_before,
constructor_avg_finish_before,
constructor_track_avg,
driver_track_avg,
grid,
constructorRef_enc,
surname_enc,
round,
circuitRef_enc,
pilot_age,
driver_home_race,
constructor_home_race,
forename_enc
]])

# ============================
# Prediction
# ============================
if st.button("Predict"):
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]  # probability of class 1

    if pred == 1:
        st.success("✅ The model predicts the driver **will finish in the Top 10**.")
    else:
        st.error("❌ The model predicts the driver **will NOT finish in the Top 10**.")

    st.metric("Probability of Top 10", f"{prob*100:.2f}%")

    # ============================
    # Gauge Chart (Plotly)
    # ============================
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Chance of Top 10"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, 50], 'color': "red"},
                {'range': [50, 80], 'color': "yellow"},
                {'range': [80, 100], 'color': "lightgreen"}
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)