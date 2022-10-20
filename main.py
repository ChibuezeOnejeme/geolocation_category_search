from asyncio.windows_events import NULL
from distutils.log import error
from types import NoneType
from geopy.geocoders import Nominatim
import requests
import json
from flask import Flask, request, render_template,redirect,url_for
from decouple import config
from forms import GeolocationForm
from extract import json_extract




app = Flask(__name__)

API_Key =config('API_KEY')
  
# create result

@app.route('/', methods=['GET', 'POST'])
def index():
    search=GeolocationForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    
    return render_template('index.html', form=search)



@app.route("/results", methods=["POST", "GET"])
def search_results( search):

       search_location =search.search_input.data
       print(search_location)
       search_category =search.search_category.data
       print(search_category)
       geolocator = Nominatim(user_agent="ezemiller")
       location = geolocator.geocode(search_location)
       
       
      

       def search_str(file_path, word):
         with open(file_path, 'r') as file:
       # read all content of a file
           content = file.read()
       # check if string present in a file
           for i in word:
             if i in content:
                 return i
         
       word= search_str("item.txt",search_category)
       url_endpoint =f"https://api.tomtom.com/search/2/categorySearch/{word}.json?key={API_Key}&lat={location.latitude}&lon={location.longitude}"
       response = requests.get(url_endpoint)
       data = response.json()
       print(data)
       result = json_extract(data,"queryType")
       
       unwanted = ['hospital/polyclinic','general','special','Hospital']
         
       result=[ele for ele in result if ele not in unwanted]
       print(result)
   
           
   
       return render_template('result.html',result=result)
  
      
             
   
   
   
   
           
           
   

if __name__ == '__main__':
    app.run(debug=True)