# Ontosheep

## Usage

Instructions for running a containerized version with a triplestore loaded with example data can be found in `test-deploy/`.  The following instructions will explain how to set up the `ews-calculator.py` script to work with a triplestore of your choosing (GraphDB will require the least amount of manual changes).  Instructions will assume a triplestore is already available.

(To install python requirements, run `pip install -r test-deploy/requirements.txt`)

1. Process the input files into triples.  Example input files for two organizations (orgA and orgB) are provided in `test-deploy/example/input/`.  A python script has been provided as an example that converts the input .csv files into .ttl files.  Usage: `python csv2rdf.py inputfile outputfile`.  Example: `python csv2rdf.py example/input/orgA.csv orgA.ttl`.
2. Import the EWS ontology into your triplestore.  A version already merged with imports is located at `test-deploy/full_ews.owl`.  
3. Import the UO ontology into your triplestore. The uo.owl file can be located [here](https://raw.githubusercontent.com/bio-ontology-research-group/unit-ontology/master/uo.owl).
4. Import the .ttl files from the example organizations into your triplestore.  If you did not create your own in Step 1, examples are provided: `test-deploy/orgA.ttl` and `test-deploy/orgB.ttl`.
5. Modify `ews-calculator.py` to point to the address of your triplestore.  As is, the request defined in `ews-calculator.py` works with GraphDB.  The request, parameters, or SPARQL query may need to be modified for other triplestores.
6. Run `python ews-calculator.py`. Once complete, the output will be stored in `results.txt`.  Your output can be compared to the example output in `test-deploy/example/output/results.txt`.
