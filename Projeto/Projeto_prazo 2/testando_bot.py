import requests, time

while True:
    token = '6687576480:AAFF7zx-2CYzRV77LB_0vjhMy9C2I5wVCBA'
    strURL = f"https://api.telegram.org/bot{token}/getUpdates"
    resultado = requests.get(strURL)
    print(resultado.json())
    time.sleep(15)