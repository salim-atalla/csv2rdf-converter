import csv
from rdflib import Graph, Literal, Namespace, URIRef

# Define a custom namespace without a URL
ns = Namespace("")  # Modify the namespace as needed

# Initialize an RDF graph
g = Graph()

# Open the CSV file for reading
csv_file = "data.csv"  # Replace with your CSV file path

with open(csv_file, "r") as csvfile:
    csv_reader = csv.DictReader(csvfile)

    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Create a unique URI for each row
        subject_uri = URIRef(ns + row["url"])

        # Add RDF triples for each column in the CSV
        for key, value in row.items():
            # Create a predicate using the column name
            predicate = URIRef(ns + key)

            # Convert the value to an RDF Literal
            obj = Literal(value)

            # Add the triple to the graph
            g.add((subject_uri, predicate, obj))

# Serialize the RDF graph to a file in "turtle" format
rdf_file = "output.ttl"
g.serialize(destination=rdf_file, format="turtle")
print(f"RDF data saved to {rdf_file}")
