import pandas as pd #for handling csv and csv contents
from rdflib import Graph, Literal, RDF, URIRef, Namespace #basic RDF handling
from rdflib.namespace import FOAF , XSD  #most common namespaces
import urllib.parse #for parsing strings to URI's

csv=pd.read_csv('example/input/orgA.csv' ,sep=",",quotechar='"')

g = Graph()
schema = Namespace('http://www.zayascilia.owl/')
OBO = Namespace('http://purl.obolibrary.org/obo/')

for index, row in csv.iterrows():
    if not pd.isnull(row['Age']):
        g.add(((URIRef(schema +  str(row['ID']) + '/age')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/age')), OBO.OBI_0002135, Literal(row['Age'], datatype=XSD.integer)))
        g.add(((URIRef(schema +  str(row['ID']) + '/age')), OBO.IAO_0000039, OBO.UO_0000036))

    if not pd.isnull(row['Temperature']):
        g.add(((URIRef(schema +  str(row['ID']) + '/temperature')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/temperature')), OBO.OBI_0002135, Literal(row['Temperature'], datatype=XSD.float)))
        g.add(((URIRef(schema +  str(row['ID']) + '/temperature')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#body_temperature_measurment_datum')))
        if float(row['Temperature']) > 50:
            g.add(((URIRef(schema +  str(row['ID']) + '/temperature')), OBO.IAO_0000039, OBO.UO_0000195))
        else:
            g.add(((URIRef(schema +  str(row['ID']) + '/temperature')), OBO.IAO_0000039, OBO.UO_0000027))

    if not pd.isnull(row['Systolic BP']):
        g.add(((URIRef(schema +  str(row['ID']) + '/systolic_bp')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/systolic_bp')), OBO.OBI_0002135, Literal(row['Systolic BP'], datatype=XSD.integer)))
        g.add(((URIRef(schema +  str(row['ID']) + '/systolic_bp')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#systolic_blood_pressure_measurement_datum')))
        g.add(((URIRef(schema +  str(row['ID']) + '/systolic_bp')), OBO.IAO_0000039, OBO.UO_0000272))

    if not pd.isnull(row['Pulse']):
        g.add(((URIRef(schema +  str(row['ID']) + '/pulse')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/pulse')), OBO.OBI_0002135, Literal(row['Pulse'], datatype=XSD.integer)))
        g.add(((URIRef(schema +  str(row['ID']) + '/pulse')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#heart_rate_measurement_datum')))

    if not pd.isnull(row['Respiratory Rate']):
        g.add(((URIRef(schema +  str(row['ID']) + '/respiratory_rate')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/respiratory_rate')), OBO.OBI_0002135, Literal(row['Respiratory Rate'], datatype=XSD.integer)))
        g.add(((URIRef(schema +  str(row['ID']) + '/respiratory_rate')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#respiratory_rate_measurement_datum')))

    if not pd.isnull(row['Peripheral Saturation']):
        g.add(((URIRef(schema +  str(row['ID']) + '/peripheral_saturation')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/peripheral_saturation')), OBO.OBI_0002135, Literal(row['Peripheral Saturation'], datatype=XSD.integer)))
        g.add(((URIRef(schema +  str(row['ID']) + '/peripheral_saturation')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#oxygen_saturation_measurement_datum')))
        g.add(((URIRef(schema +  str(row['ID']) + '/peripheral_saturation')), OBO.IAO_0000039, OBO.UO_0000187))

    if not pd.isnull(row['Supplemental Oxygen']):
        g.add(((URIRef(schema +  str(row['ID']) + '/supplemental_oxygen')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/supplemental_oxygen')), OBO.OBI_0002135, Literal(row['Supplemental Oxygen'], datatype=XSD.boolean)))
        g.add(((URIRef(schema +  str(row['ID']) + '/supplemental_oxygen')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#supplemental_oxygen_use_measurement_datum')))

    if not pd.isnull(row['Conciousness']):
        g.add(((URIRef(schema +  str(row['ID']) + '/AVPU')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/AVPU')), OBO.OBI_0002135, Literal(row['Conciousness'], datatype=XSD.string)))
        g.add(((URIRef(schema +  str(row['ID']) + '/AVPU')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#AVPU_measurement_datum')))

    if not pd.isnull(row['Urine']):
        g.add(((URIRef(schema +  str(row['ID']) + '/urine_output')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/urine_output')), OBO.OBI_0002135, Literal(row['Urine'], datatype=XSD.integer)))
        g.add(((URIRef(schema +  str(row['ID']) + '/urine_output')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#urine_output_measurement_datum')))

    if not pd.isnull(row['Glasgow Coma Scale']):
        g.add(((URIRef(schema +  str(row['ID']) + '/glasgow_coma_scale')), OBO.IAO_0000136, URIRef(schema +  str(row['ID']) + '/person' )))
        g.add(((URIRef(schema +  str(row['ID']) + '/glasgow_coma_scale')), OBO.OBI_0002135, Literal(row['Glasgow Coma Scale'], datatype=XSD.integer)))
        g.add(((URIRef(schema +  str(row['ID']) + '/glasgow_coma_scale')), RDF.type, URIRef('http://www.semanticweb.org/zayascilia/ontologies/2022/3/untitled-ontology-8#glasgow_coma_scale_measurement_datum')))

g.serialize('orgA.ttl',format='turtle')
