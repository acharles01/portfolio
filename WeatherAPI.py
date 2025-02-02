import requests

def fetch_weather(city1):
    response1 = requests.get("http://api.openweathermap.org/data/2.5/weather", {"q": city1, "appid": "0e6174158bf1eda2f24c5969bc756369", "units": "metric"})

    if response1.status_code == 200:
        data1 = response1.json()
        name1 = data1["name"]
        temp1 = data1["main"]["temp"]
        weather1 = data1["weather"][0]["description"]
        print("City: ", name1)
        print("Temperature: ", temp1)
        print("Conditions: ", weather1)
    else:
        print("Error: ", response1.status_code)

if(__name__ == "__main__"):
    city = input("Enter the name of the city: ")
    fetch_weather(city)