import logging
from datetime import datetime

from tornado.gen import coroutine, Return

from data.query import Query


class NamespacesActions(object):

    def __init__(self, settings):
        logging.info("Initializing NamespacesActions")
        self.kube_client = settings['kube']

    @staticmethod
    def check_permissions(user, operation):
        logging.debug("Checking permissions for user %s and operation %s on namespaces", user["username"], operation)
        return True

    @coroutine
    def create(self, namespace):
        logging.info("Creating namespace")
        body = {
            'kind': 'Namespace',
            'apiVersion': 'v1',
            'metadata': {
                'name': namespace['name'],
                'labels': [
                    {'name': namespace['name']}
                ]
            }
        }

        response = self.kube_client.namespaces.post(body)
        raise Return(response)

    @coroutine
    def update(self, document):
        logging.info("Updating namespace")

        user = yield Query(self.database, "Users").find_one(document['_id'])
        yield Query(self.database, "Users").save(user)

        raise Return(user)

    @coroutine
    def delete(self, namespace_id):
        logging.info("Deleting namespace")

        user = yield Query(self.database, "Users").find_one(namespace_id)
        user['deleted'] = datetime.now()

        yield Query(self.database, "Users").save(user)

        raise Return(user)
