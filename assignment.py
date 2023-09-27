import requests

def get_weather_data():
    url="https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response=requests.get(url)
    return response.json()

def get_temp(data,date):
    for x in data['list']:
        if x['dt_txt']==date:
            return x['main']['temp']

def get_wind_speed(data,date):
    for x in data['list']:
        if x['dt_txt']==date:
            return x['wind']['speed']

def get_pressure(data,date):
    for x in data['list']:
        if x['dt_txt']==date:
            return x['main']['pressure']

def main():
    data=get_weather_data()
    while True:
        print("1. Get Temperature\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
        option=int(input("Enter your option: "))
        if option==0:
            break
        elif option==1:
            date=input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            temp=get_temp(data,date)
            print(f"Temperature: {temp}")
        elif option==2:
            date=input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            w_speed=get_wind_speed(data,date)
            print(f"Wind Speed: {w_speed}")
        elif option==3:
            date=input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
            pressure=get_pressure(data,date)
            print(f"Pressure: {pressure}")
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()
