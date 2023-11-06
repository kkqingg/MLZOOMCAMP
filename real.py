import requests
url = "http://localhost:9696/predict"

customer_id = "xyz-123"

person= {
 "pclass": 1,
 "sex": "male",
 "age": 26.0,
 "fare": 30.0,
 "embarked": "C",
 "class": "First",
 "who": "man",
 "deck": "C",
 "alone": True}
response = requests.post(url,json = person).json()

print(response)

if response["survive"] == True:
    print(f"The person {customer_id}survived ")
else:
    print(f"Sorry the {customer_id} did not survive")