import requests

#create repo
headers = {
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}
files = {
    'config': open('repo-config.ttl', 'rb'),
}
response = requests.post('http://triplestore:7200/rest/repositories', headers=headers, files=files);


#import ews
headers = {
    'Content-Type': 'application/rdf+xml',
}

with open('full_ews.owl', 'rb') as f:
    data = f.read()

response = requests.post('http://triplestore:7200/repositories/ontosheep-test/statements', headers=headers, data=data);

#import uo 
headers = {
    'Content-Type': 'application/rdf+xml',
}

with open('uo.owl', 'rb') as f:
    data = f.read()

response = requests.post('http://triplestore:7200/repositories/ontosheep-test/statements', headers=headers, data=data)



#import orgA 
headers = {
    'Content-Type': 'application/x-turtle',
}

with open('orgA.ttl', 'rb') as f:
    data = f.read()

response = requests.post('http://triplestore:7200/repositories/ontosheep-test/statements', headers=headers, data=data)

#import orgB
headers = {
    'Content-Type': 'application/x-turtle',
}

with open('orgB.ttl', 'rb') as f:
    data = f.read()

response = requests.post('http://triplestore:7200/repositories/ontosheep-test/statements', headers=headers, data=data)
