import json

listings_found = []


# Parse listo listings
with open('C:/Users/raymo/Github/ai-tools/hunter-ai/json/listo.json', 'r') as file:
    data = json.load(file)

    print(f"LISTO: Found {len(data)} items")
    
    for item in data:
        houses = item['rows']  
        for house in houses:
            # print(f"MLS: {house['id']}, {house['sub_type']}, {house['addr']}, Price: ${house['lp_dol']}")
            # print(f"Lat: {house['lng']} Long: {house['lat']}")
            # print(f"Sqft: {house['sqft']} ")
            # print(f"Title: {house['title']} ")
            # print(f"Thumbnail: {house['thumbnail']} ")
            # print(f"Community: {house['community']} ")
            # print(f"Bedroom: {house['br']} Bathroom: {house['bath_tot']}")
            # print(f"Sale: {house['s_r']}")
            # print(f"#Photos: {house['photos_total']} \n")
            # print(f"#Photos: {house['photos_total']} Photos: {house['photos']}\n\n")
            
            _ = {
                'mls': house['id'],
                'type': house['sub_type'],
                'address': house['addr'],
                'price': house['lp_dol'],
                'lng': house['lng'],
                'lat': house['lat'],
                'sqft': house['sqft'],
                'title': house['title'],
                'thumb': house['thumbnail'],
                'community': house['community'],
                'bedrooms': house['br'],
                'bathrooms': house['bath_tot'],
                'status': house['s_r'],
                'photos': house['photos'],
                'listed_date': house['badges1'][1]['text']
            }
            listings_found.append(_)
            
        

# Parse house sigma
with open('C:/Users/raymo/Github/ai-tools/hunter-ai/json/house-sigma.json', 'r') as file:
    data = json.load(file)
    print(f"HOUSE-SIGMA: Found {len(data)} items")
    
    for item in data:
        houses = item['data']['houseList']
        for house in houses:
            _ = {
                'mls': house['ml_num'],
                'type': house['house_type_name'],
                'address': house['address'],
                'price': house['price_int'],
                'lng': house['map']['lon'],
                'lat': house['map']['lat'],
                'sqft': house['house_area']['area'],
                'title': house['address_navigation'],
                'thumb': house['photo_url'],
                'community': house['community_name'],
                'bedrooms': house['bedroom'],
                'bathrooms': house['washroom'],
                'status': house['list_status']['s_r'],
                'photos': house['photo_url'],
                'listed_date': house['date_added'] 
            }
            listings_found.append(_)
    
    
print(f"Total houses: {len(listings_found)}")

for idx, i in enumerate(listings_found):
    if not str(i['mls']).startswith('X'):
        listings_found[idx]['mls'] = 'None'
    # print(listings_found[idx]['mls'])

house_set = {}

for idx, i in enumerate(listings_found):
    if str(i['mls']).startswith('X'):
        house_set[i['mls']] = i
    else:
        house_set[f'U{idx}'] = i

print(f"Total unique houses: {len(house_set)}")

with open('C:/Users/raymo/Github/ai-tools/hunter-ai/json/house_listings.json', 'w') as fp:
    json.dump(house_set, fp)
