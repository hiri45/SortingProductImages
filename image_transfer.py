import csv
import requests
import os


def download_image(url, folder):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Extract the image file name from the URL

    filename = os.path.join(folder, (url.split("/")[-1]).split("?")[-2])

    # Send a GET request to the image URL
    response = requests.get(url)

    # Save the image file
    with open(filename, "wb") as file:
        file.write(response.content)
        print(f"Downloaded: {filename}")


# Open the CSV file
with open("amazon_image.csv") as csvfile:
    reader = csv.reader(csvfile)

    # Skip the header row
    next(reader)

    # Process each row in the CSV
    for row in reader:
        url = row[0]
        folder = row[1]

        download_image(url, folder)