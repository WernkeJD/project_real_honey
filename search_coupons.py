import requests

if __name__ == '__main__':
    response = requests.get("http://localhost:5000/search_coupons")
    if response.status_code == 200:
        coupons = response.json()
        print(coupons)
    else:
        print("No json")
    