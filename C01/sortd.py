dic = {"bob": 23, "charlie": 36, "alice": 72, "david": 9} 
sort_data_asc = sorted(dic.items(), key=lambda x: x[0]) 
print("Dictionary in ascending order:", sort_data_asc) 
sort_data_desc = sorted(dic.items(), key=lambda x: x[0], reverse=True) 
print("Dictionary in descending order:", sort_data_desc)
