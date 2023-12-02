import streamlit as st

EMISSION_FACTORS ={
    "India":{
        "Transportation": 0.14, 
        "Electricity": 0.82,
        "Diet": 1.25,
        "Waste": 0.1
    }
}

st.set_page_config(layout="wide",page_title="Ecoscore Tracker")

st.title("Ecoscore Tracker")


st.subheader("🌏Your Country")
country = st.selectbox("Select",["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗Daily commute distance (in km)")
    distance = st.number_input("Distance", 0.0, 100.0, key="distance_input")


    st.subheader("💡Monthly electricity consumpution (in kwh)")
    electricity = st.number_input("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑 Waste generated per week (in kg)")
    waste = st.number_input("Waste", 0.0, 100.0, key="waste_input")


    st.subheader("🥘Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals-input")

    if distance > 0:
        distance = distance * 365

    if electricity > 0:
        electricity = electricity * 12

    if meals > 0:
        meals = meals * 365

    if waste > 0:
        waste = waste * 52 


        
transportation_emissions = EMISSION_FACTORS[country]['Transportation'] * distance
electricity_emissions = EMISSION_FACTORS[country]['Electricity'] * electricity
Diet_emissions = EMISSION_FACTORS[country]['Diet'] * meals
waste_emissions = EMISSION_FACTORS[country]['Waste'] * waste

transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(Diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)


total_emissions = round(
    transportation_emissions+ electricity_emissions + diet_emissions + waste_emissions, 2
      )
if st.button("Calculate CO2 Emissions"):

    st.header("Results")

    col3, col4 =st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Categories")
        st.info(f"🚗Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🥘Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑 Waste: {waste_emissions} tonnes CO2 per year")
    with  col4:
        st.subheader("Total Carbon Footprint")   
        st.info(f"Your total Carbon footprint is: {total_emissions} tonnes per year")
        st.warning ("In 2022, CO2 emissions per capita for India was 1.9 tons of CO2 per capita. Between 1972 and 2021, CO2 emissions per capita of India grew substantially from 0.39 to 1.9 tons of CO2 per capita rising at an increasing annual rate that reached a maximum of 9.41% in 2022.")
