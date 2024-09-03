import json
import boto3


docdb_endpoint = 'mongodb://LaveenaKithani:<password>@docdb-2024-09-03-05-48-52.cluster-c3acyimyebbs.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false'
docdb_username = ''
docdb_password = ''
docdb_db_name = ''
docdb_collection_name = ''
def lambda_handler(event, context):
    # TODO implement
    docdb_client = boto3.client('docdb', endpoint_url=docdb_endpoint)
    
    record={
        "orderId": "123",
        "clientName": "Laveena",
        "orderDate": "2024-09-02",
        "companyName": "Company1",
        "shares": "2"
    }
    
    docdb_client.insert_one(docdb_db_name, docdb_collection_name, records)
    
    return {
        "statusCode": 200,
        "body":json.dumps("Records inserted successfully.")
    }
