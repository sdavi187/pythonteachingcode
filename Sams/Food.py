
import requests
import json
from Yelp_Functions import *


rest_params = {'term':'seafood','location':'New York City'}

parsed = query_yelp (rest_params)

results = parse_reply (parsed)

#print_results(results)

test_id = get_buisness_id("A+ Crab Seafood", results)

print ("A+ Crab Seafood's id is", test_id)
get_url(test_id,results)


#print(json.dumps(parsed, indent=4))

