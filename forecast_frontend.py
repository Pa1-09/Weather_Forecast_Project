import streamlit as st
import plotly.express as pex

def enter_place():
    pass


def plot_graph(days_local):
    dates=["2020-1-1", "2021-1-1", "2022-1-1", "2023-1-1"]
    temps = [15, -15, 26, 33]
    temps= [data*days_local for data in temps]
    return dates, temps

st.set_page_config(layout="wide")
st.title("Weather Forecast App for next Days")

with st.container():

    location = st.text_input(label="Place", key="place", placeholder="Enter Place",
                             on_change=enter_place)

    days = st.slider("Forecast Days", min_value=1, max_value=5,
                     help="Select number of forecast days")

    option = st.selectbox("Select Data to View", ("Temperature", "Sky"))

    st.subheader(f"{option} for the next {days} days in {location} ")

    # returning date and time
    d, t = plot_graph(days)
    # jotting out line chart using plotly
    figure = pex.line(x=d, y=t, labels={"x": "DATE", "y":"TEMPERATURE (C)"})
    # plotting char in streamlit
    st.plotly_chart(figure, use_container_width=True)
