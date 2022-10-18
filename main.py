from geopy.geocoders import Nominatim
import requests
import json
from flask import Flask, request, render_template
from extract import json_extract
from decouple import config
app = Flask(__name__)
  
# create HOME View
@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template("index.html")

    else:
        search = request.form["search"]
        API_Key =config('API_KEY')
        geolocator = Nominatim(user_agent="ezemiller")
        location = geolocator.geocode(search)
        
        search_contents =search.split(' ')
        for i in search_contents:
           item =i

        def search_str(file_path, word):
          with open(file_path, 'r') as file:
        # read all content of a file
            content = file.read()
        # check if string present in a file
            if word in content:
                return word
        
        word= search_str("item.txt",item)




        
        url_endpoint =f"https://api.tomtom.com/search/2/categorySearch/{word}.json?key={API_Key}&lat={location.latitude}&lon={location.longitude}"
        response = requests.get(url_endpoint)
        data = response.json()
        result = json_extract(data,"name")
        unwanted = ['hospital/polyclinic','general','special','Hospital']

      
        result=[ele for ele in result if ele not in unwanted]

        

        return render_template('index.html',result=result)




if __name__ == '__main__':
    app.run(debug=True)