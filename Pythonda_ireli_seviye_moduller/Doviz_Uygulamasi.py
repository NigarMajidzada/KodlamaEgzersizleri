import requests
def convert_curr():
    init_curr=input("Enter the inital currency: ")
    target_curr=input("Enter the target currency: ")

    while True:
        try:
            amount=float(input("Enter the amount: "))
        except:
            print('The amount needs  to be numeric.')
            continue

        if  not amount>0:
            print("Amount needs greather then 0.")
            continue

        else:
            break

    url = f"https://api.apilayer.com/fixer/convert?to={target_curr}&from={init_curr}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "fXSXOJyaJtBBC6Eq3AYRd6c9Ir6ymXBj"
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    status_code=response.status_code

    if status_code !=200:
        result=response.json()
        print("Error response: "+ str(result))
        quit()

    result=response.json()
    print("Conversion result is:" +str(result))

if __name__=='__main__':
    convert_curr()
