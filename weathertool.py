import requests
import weather.com as api
from statistics import mean, median, mode

def get_weather_data(city):
    api_key = '17b1c78ebf62434c863133647241802'
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if "error" not in data:
            weather_dict = {
                "city": data["location"]["name"],
                "temperature": data["current"]["temp_c"],
                "description": data["current"]["condition"]["text"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_kph"]
            }
            return weather_dict
        else:
            return {"error": data["error"]["message"]}
    
    except Exception as e:
        return {"error": str(e)}
        
def get historical_weather_data(city, start_date, end_date):
    api_key ='17b1c78ebf62434c863133647241802'
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
        response = requests.get(url)
        data = response.json()
        
        if "hourly" in data:
            temperature =[hour["temp"] for hour in data["hourly"]]
            return temperatures
            else:
                return {"error" : "No hourly data available"}
                
                except Exception as e:
                    return{"error" : str(e)}
    
def calculate_statistics(data):
   mean_temp = mean(data)
   median_temp = median(data)
   mode_temp =mode(data)
   return {"mean" : mean_temp, "median" : median_temp, "mode" : mode_temp}
     
     city_name = ""
weather_info = get_weather_data(city_name)
if "error" not in weather_info:
    print("Current Weather:")
    for key, value in weather_info.items():
        print(f"{key}: {value}")

# Historical Data
    city_coordinates = {"lat": "lon":}  
    historical_data = get_historical_weather_data(city_coordinates, "2024-02-01", "2024-02-07")
    if "error" not in historical_data:
        stats = calculate_statistics(historical_data)
        print("\nHistorical Weather Statistics:")
        print(f"Mean Temperature: {stats['mean']}")
        print(f"Median Temperature: {stats['median']}")
        print(f"Mode Temperature: {stats['mode']}")
    else:
        print("\nError fetching historical weather data:", historical_data["error"])
else:
    print("\nError fetching current weather data:", weather_info["error"])
 
