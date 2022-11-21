import osmnx as ox
import json
from flask import Flask, request, render_template,redirect,url_for
from forms import GeolocationForm





app = Flask(__name__)


  
# create result

@app.route('/', methods=['GET', 'POST'])
def index():
    search=GeolocationForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    
    return render_template('index.html', form=search)



@app.route("/results", methods=["POST", "GET"])
def search_results( search):
       """This function takes in put from the the index form and processes it using osmnx  """
       
       place_name= search.search_input.data #This grabs the name or the location for search
      
       search_category =search.search_category.data # This grabs the category for the search

       recieved_tags =search.tags.data # This are the tags eg amenity, building

       tags ={recieved_tags:search_category}
      
       point_of_interest_search = ox.geometries_from_place(place_name,tags=tags) #This the algorithm that performs point of interest search

       list_result =point_of_interest_search['name'].values
       result=[]
       for i in list_result:
          result.append(i)
       
           
   
       return render_template('result.html',result=result)
  
      
             
   
   
   
   
           
           
   

if __name__ == '__main__':
    app.run(debug=True)