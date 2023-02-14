import requests as rq

API_KEY = "5d7ae4c8b77ccfe35e8f6639cfcc89b0"


def get_data(location_local, forecast_days_local=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={location_local}&appid={API_KEY}"
    response = rq.get(url)
    data = response.json()

    # filtering data based on days
    filtered_data = data['list'][:8 * forecast_days_local]
    return filtered_data


if __name__ == "__main__":
    result = get_data(location_local="Mumbai", forecast_days_local=3)
    print(result)
