import requests
import datetime

USERNAME = "karim23"
TOKEN = "kjajdfhjAfklasf123jsaf"
pixela_endpoint = "https://pixe.la/v1/users"

# graph creation (assuming user is already created)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Health Care",
    "unit": "steps",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment if you need to create the graph
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# ✅ Correct pixel endpoint
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# ✅ Generate today's date automatically
today = datetime.datetime.now().strftime("%Y%m%d")

post_pixel_params = {
    "date": today,  # or use "20250421" as you had
    "quantity": "10",
}

pixel_response = requests.post(url=post_pixel_endpoint, json=post_pixel_params, headers=headers)
print(pixel_response.text)


