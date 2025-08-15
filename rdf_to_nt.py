# Instructions to convert RDF/XML to N-Triples using rdflib

# 1. Install rdflib if you haven't already:
# pip install rdflib

# 2. Place it inside the folder of the ontology (e.g., "/pinakes/rdf_to_nt.py")

# 3. Run the script with python inside of that folder (e.g., "python rdf_to_nt.py")



from rdflib import Graph

g = Graph()
g.parse("ontology.rdf", format="xml")   # RDF/XML
g.serialize("ontology.nt", format="nt") # N-Triples
