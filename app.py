import streamlit as st

def convert_to_inches(value):
    if "." in value:
        feet, inch = value.split(".")
        return int(feet) * 12 + int(inch)
    else:
        return int(value) * 12

st.title("Truck Volume Calculator (ट्रक आयतन कैलकुलेटर)")

h = st.text_input("Height (जैसे 12.5 = 12ft 5in)")
w = st.text_input("Width (जैसे 4.5 = 4ft 5in)")
b = st.text_input("Breadth (उदाहरण 25.5)")

if st.button("Calculate हिसाब लगाएँ"):
    try:
        h_in = convert_to_inches(h)
        w_in = convert_to_inches(w)
        b_in = convert_to_inches(b)

        cu_in = h_in * w_in * b_in
        cu_ft = cu_in / 1728

        st.success(f"आयतन (Volume) = {cu_ft:.2f} cubic feet")
    except:
        st.error("कृपया सही संख्या डालें (Please enter valid numbers)")
