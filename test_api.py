import requests

# Endpoint URL
local_url = 'http://localhost:5000/predict'  # Update the URL if necessary
heroku_url = "https://dementia-prediction-a1a3078b20c1.herokuapp.com/upload"

# Image file path
image_file = 'images/26.jpg'  # Replace with the path to your image file

# Open the image file
with open(image_file, 'rb') as f:
    # Prepare the request data
    files = {'image': f}

    # Send the POST request to the API
    response = requests.post(heroku_url, files=files)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the prediction from the response
        prediction = response.json()['dementia']
        print(response.json())
        print('Prediction:', prediction)
    else:
        print('Error:', response.text)