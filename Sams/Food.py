
import requests
import json


client_id = "CuyK_Nviuv3km8gryYuiqg"
api_key = "tGjtDDhoM96gsB8uJc8qEiBXB-xcU-60aXJ8yZfT9aBArhjYB1wplGaZNYIKUUyk-g5bvqkY2gZzdIsWKwbdoGudeRMXXTUiA1JjLAIY-kRnjy6eRnWjUK6fPOP2YHYx"
headers = {'Authorization': 'Bearer %s' % api_key}



def get_information():

    zip_code = input ("Enter your zip code: ")

    return zip_code

def parse_reply (parsed_input):

    businesses = parsed_input["businesses"]

    return (businesses)

def print_results (businesses_table):

    for business in businesses_table:
        print ("Name:", business["name"])
        print ("Rating:", business["rating"])
        print ("Address:", " ".join(business["location"]["display_address"]))
        print ("Phone", business["phone"])
        print ("\n")

    return

def get_buisness_id (rname, business_table):

    for business in business_table:
        if rname == business["name"]:
            id = business["id"]
            break

    return (id)

def query_yelp (search_terms):

    

    url='https://api.yelp.com/v3/businesses/search'

    # Making a get request to the API
    req=requests.get(url, params=search_terms, headers=headers)
 
    # proceed only if the status code is 200
    print('The status code is {}'.format(req.status_code))
 
    return json.loads(req.text)

def get_url (rest_id,business_table):
    #url = "https://api.yelp.com/v3/businesses/" + rest_id + "/reviews"
    #req = requests.get(url, headers=headers)
    #parsed = json.loads(req.text)
    #print(json.dumps(parsed, indent=4))
    for business in business_table:
        if rest_id == business["id"]:
            print (business["url"])
            break

rest_params = {'term':'seafood','location':'New York City'}

parsed = query_yelp (rest_params)

results = parse_reply (parsed)

#print_results(results)

test_id = get_buisness_id("A+ Crab Seafood", results)

print ("A+ Crab Seafood's id is", test_id)
get_url(test_id,results)


#print(json.dumps(parsed, indent=4))

