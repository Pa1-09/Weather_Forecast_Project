import streamlit as st
import plotly.express as pex
from forecast_backend import get_data

st.set_page_config(layout="wide")
st.title(f"Weather Forecast App for Upcoming Days")

with st.container():
    location = st.text_input(label="Place", key="place", placeholder="Enter Place")

    days = st.slider("Forecast Days", min_value=1, max_value=5,
                     help="Select number of forecast days")

    option = st.selectbox("Select Data to View", ("Temperature", "Sky"))

    st.subheader(f"{option} for the next {days} days in {location} ")

    print("Enter something in place input area")

    try:
        # handling location incase if empty
        if location:
            # getting temperature and sky_data
            filtered_data = get_data(location_local=location, forecast_days_local=days)

            # filter further based on option
            if option == "Temperature":
                temperatures = [data['main']['temp'] / 10 for data in filtered_data]

                dates = [dict["dt_txt"] for dict in filtered_data]
                figure1 = pex.line(x=dates, y=temperatures, labels={"x": "DATES", "y": "TEMPERATURE (C)"})
                st.plotly_chart(figure1)
            elif option == "Sky":
                image_mapping = {
                    "Clouds": "images/cloud.png",
                    "Clear": "images/clear.png",
                    "Rain": "images/rain.png",
                    "Snow": "images/snow.png"
                }
                sky_conditions = [data['weather'][0]['main'] for data in filtered_data]
                images = [image_mapping[data] for data in sky_conditions]
                st.image(images, width=120)

            else:
                print("Sorry...!")
    except KeyError:
        st.info("Location not exists")
