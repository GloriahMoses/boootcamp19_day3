import requests

def university_search(country):
	"""this function consumes the hipolabs.com universities search api 
	to search for universities details from a country of interest. 
	The function prints out all university; web_page url, country, domain, name and alpha_two_code"""

	url = 'http://universities.hipolabs.com/search?country='
	country_search = country.replace(' ', '%20') #search input is assigned to the variable country in the api
	complete_url = url + country_search  #the full url to the searched resource
	json_obj = requests.get(complete_url) #a get reguest for data results in form of json object
	results = json_obj.json() #raw json data response
	for item in results: #results returned in form of a list of data in dictionaries
	    for item_key , item_value in item.items(): #iterating over each dictionary to get output in specified format
	        print (item_key + ": "+ item_value)

print(university_search('Uganda'))