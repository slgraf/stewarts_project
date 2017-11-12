from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

#https://github.com/hanneshapke/pyzillow



address = '2928 W WAGONER RD'
zipcode = '85053'

zillow_data = ZillowWrapper("X1-ZWz1fak7wz8iyz_4lr3d")
deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)

result.zillow_id # zillow id, needed for the GetUpdatedPropertyDetails

#print result

print result.zillow_id
print result.home_detail_link

#print deep_search_response