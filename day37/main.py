import requests as req
from datetime import datetime
#pre requisites and user creation------------->
pixel_endpoint="https://pixe.la/v1/users"
token="hjhktyu123bnduis"
user_name="umesh69"
user_params={
    "token":token,
    "username":"umesh69",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response=req.post(pixel_endpoint,json=user_params)
# graph creation once created doesnt need to create again------->
graph_endpoint=f"{pixel_endpoint}/{user_name}/graphs"
graph_params={
    "id":"graph2",
    "name":"study python",
    "unit":"hours",
    "type":"float",
    "color":"momiji"
}
headers={
    "X-USER-TOKEN":token
}
response=req.post(graph_endpoint,json=graph_params,headers=headers)
#for posting days track----------->
today=datetime.now()
print(today.strftime("%Y%m%d"))
pixel_creation_endpoint=f"{pixel_endpoint}/{user_name}/graphs/graph2"
pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many hours you studied: ")
}
response=req.post(pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)
#for updating else u dont need it ---->
# pixel_put_endpoint=f"{pixel_endpoint}/{user_name}/graphs/graph2/{today.strftime('%Y%m%d')}"
# new_pixel={
#     "quantity":"2.5"
# }
# response=req.put(pixel_put_endpoint,json=new_pixel,headers=headers)
#for deleting------------->
# delete_endpoint=f"{pixel_endpoint}/{user_name}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response=req.delete(delete_endpoint,headers=headers)
