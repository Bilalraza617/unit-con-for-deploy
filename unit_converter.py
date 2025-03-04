import streamlit as st

st.title("Unit Converter")

units = {
    "Length": {
        "Meter": 1,
        "Centimeter": 100,
        "Kilometer": 0.001,
        "Inch": 39.3701,
        "Foot": 3.28084,
        "Mile": 0.000621371
    },
    "Weight": {
        "Kilogram": 1,
        "Gram": 1000,
        "Milligram": 1e+6,
        "Pound": 2.20462,
        "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": 1,
        "Fahrenheit": 33.8,
        "Kelvin": 274.15
    }
}

unit_type = st.selectbox("Select Unit Type", list(units.keys()))

from_unit = st.selectbox("From", list(units[unit_type].keys()))

to_unit = st.selectbox("To", list(units[unit_type].keys()))

value = st.number_input("Enter value", value=1.0)

if unit_type == "Temperature":
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            converted_value = (value * 9/5) + 32
        elif to_unit == "Kelvin":
            converted_value = value + 273.15
        else:
            converted_value = value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            converted_value = (value - 32) * 5/9
        elif to_unit == "Kelvin":
            converted_value = (value - 32) * 5/9 + 273.15
        else:
            converted_value = value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            converted_value = value - 273.15
        elif to_unit == "Fahrenheit":
            converted_value = (value - 273.15) * 9/5 + 32
        else:
            converted_value = value
else:
    converted_value = value * (units[unit_type][to_unit] / units[unit_type][from_unit])


st.write(f"{value} {from_unit} is equal to {converted_value:.2f} {to_unit}")