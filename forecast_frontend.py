import streamlit as st


def enter_place():
    pass


st.set_page_config(layout="wide")
st.title("Weather Forecast App for next Days")

with st.container():

    location = st.text_input(label="Place", key="place", placeholder="Enter Place",
                             on_change=enter_place)

    days = st.slider("Forecast Days", min_value=1, max_value=5,
                     help="Select number of forecast days")

    option = st.selectbox("Select Data to View", ("Temperature", "Sky"))

    st.subheader(f"{option} for the next {days} days in {location} ")
