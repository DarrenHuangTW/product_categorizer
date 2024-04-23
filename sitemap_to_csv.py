
import requests
import xml.etree.ElementTree as ET
import csv

# URL of the XML sitemap
url = 'https://proof.com.sg/sitemap_products_1.xml?from=4534676095039&to=7624565129402'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    xml_data = response.text
    # Parse the XML data
    root = ET.fromstring(xml_data)

    # Define namespaces to search tags properly
    namespaces = {
        '': 'http://www.sitemaps.org/schemas/sitemap/0.9',  # default namespace
        'image': 'http://www.google.com/schemas/sitemap-image/1.1'
    }

    # Open a CSV file for writing
    with open('products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Product Name', 'Product Image', 'Product URL'])

        # Iterate through each URL in the XML
        for url in root.findall('url', namespaces):
            loc = url.find('loc', namespaces).text
            image = url.find('image:image', namespaces)
            if image is not None:
                image_loc = image.find('image:loc', namespaces).text
                image_title = image.find('image:title', namespaces).text
                # Write the product details to the CSV
                writer.writerow([image_title, image_loc, loc])
else:
    print(f"Failed to retrieve XML: HTTP {response.status_code}")