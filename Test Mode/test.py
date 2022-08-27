
# !pip install -U craiyon.py
from craiyon import Craiyon

generator = Craiyon() # Instantiates the api wrapper
query = input("Write Description : ")

if query == '':
    query = "Man eating Apple"
    
result = generator.generate(query)
result.save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path
