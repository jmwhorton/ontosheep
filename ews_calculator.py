import os
import sys
import json 
import requests
from importlib import import_module


def get_ews_dict(pid):
    query = """
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select * where {{
    ?ind a ?class.
    ?class rdfs:subClassOf obo:IAO_0000109 .
    ?ind obo:IAO_0000136 <http://www.zayascilia.owl/{0}/person> .
    OPTIONAL {{ ?ind obo:OBI_0002135 ?value }} .
    OPTIONAL {{ ?ind obo:IAO_0000039 ?unitlabel }} .
}}
	 """.format(pid)
    body = {'query': query, 'Accept': 'application/sparql-results+json' }
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    try:
        r = requests.request('POST', "http://triplestore:7200/repositories/ontosheep-test", data=body, headers=headers)
        if r.ok:
            try:
                data = r.json()
                ewsResults = {}
                for element in data['results']['bindings']:
                    result = {'uri':element['ind']['value']}
                    if element.get('value'): 
                        result['value'] = element['value']['value']
                    if element.get('unitlabel'):
                        result['unitlabel'] = element['unitlabel']['value']
                    ewsResults[element['class']['value']] = result

                return ewsResults
            except ValueError:
                print('Bad json data')
                return []
        else:
            return []
    except:
        print('failed rdf')

def get_spec():
    if not os.path.exists('lib/ews_spec.json'):
        url = 'https://raw.githubusercontent.com/jmwhorton/ontosheep-ews/main/ews_spec.json'
        r = requests.get(url, allow_redirects=True)
        open('lib/ews_spec.json', 'wb').write(r.content)

    with open('lib/ews_spec.json') as f:
        data = json.load(f)
    return data

directory_path = "lib"

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

if not os.path.exists('lib/ews_calc.py'):
    url = 'https://raw.githubusercontent.com/jmwhorton/ontosheep-ews/main/ews_calc.py'
    r = requests.get(url, allow_redirects=True)
    open('lib/ews_calc.py', 'wb').write(r.content)

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
module = import_module('lib.ews_calc')
spec = get_spec()
with open('results.txt', 'w') as out:
    for i in range(1, 2001):
        person = get_ews_dict(i)
        results = module.run(person, spec)
        results['Person ID'] = i
        out.write(str(results) + '\n')
        print(results)
