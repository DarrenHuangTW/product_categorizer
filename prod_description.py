import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_product_description(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product_description = soup.select_one('div.product__description').get_text().strip()
        return product_description.strip()
    else:
        return None

# Load the products.csv file
df = pd.read_csv('products.csv')


# Apply the extract_product_description function to all URLs and store the results in a new column
df['Product Description'] = df['Product URL'].apply(extract_product_description)

# Save the updated DataFrame to a new CSV file
df.to_csv('products_with_description.csv', index=False)

