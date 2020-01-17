import neo4j
import json


class Connector:
    def __init__(self):
        uri, user, password = Connector.load_connection_parameters('app/db/data.json')
        self.driver = neo4j.GraphDatabase.driver(uri, auth=(user, password))
        self.session = self.driver.session()


    @staticmethod
    def load_connection_parameters(cred_path):
        with open(cred_path, 'r') as f:
            data = json.load(f)
            return data['uri'], data['user'], data['password']


    def make_request(self, method, *args, **kwargs):
        return method(self.session, *args, **kwargs)


    def cleanup(self):
        self.session.close()
        self.driver.close()