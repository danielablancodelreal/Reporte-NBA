dicty = '{"get":"teams\/","parameters":{"name":"Atlanta Hawks"},"errors":[],"results":1,"response":[{"id":1,"name":"Atlanta Hawks","nickname":"Hawks","code":"ATL","city":"Atlanta","logo":"https:\/\/upload.wikimedia.org\/wikipedia\/fr\/e\/ee\/Hawks_2016.png","allStar":False,"nbaFranchise":True,"leagues":{"standard":{"conference":"East","division":"Southeast"},"vegas":{"conference":"summer","division":None},"utah":{"conference":"East","division":"Southeast"},"sacramento":{"conference":"East","division":"Southeast"}}}]}'
print(dicty.strip(''))
print(dict(dicty))
print(dicty["response"])
print(dicty["response"][0]["id"])