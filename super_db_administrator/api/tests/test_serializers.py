from django.test import TestCase
from api.models import ConnectionDb

from api.serializers.connection import ConnectionSerializer

class ConnectionSerializerTests(TestCase):
    def test_return_all_object(self):
        objectToSerialize = {
            'db_name':'db_name',
            'name':'test',
            'host':'127.0.0.1',
            'port':5432,
            'username':'username',
            'password':'password'
        }
        connectionDb = ConnectionDb()
        connectionDb.name = objectToSerialize['name']
        connectionDb.db_name = objectToSerialize['db_name']
        connectionDb.host = objectToSerialize['host']
        connectionDb.port = objectToSerialize['port']
        connectionDb.username = objectToSerialize['username']
        connectionDb.password = objectToSerialize['password']
        connectionDb.save()
        connectionDbToCheck = ConnectionDb.objects.get(id=connectionDb.id)
        serializer = ConnectionSerializer(connectionDbToCheck)
        print(serializer.data)
        print(objectToSerialize)
        self.assertDictEqual(serializer.data, objectToSerialize)
        self.assertEqual(serializer.data['db_name'], objectToSerialize['db_name'])
        self.assertEqual(serializer.data['host'], objectToSerialize['host'])
        self.assertEqual(serializer.data['port'], objectToSerialize['port'])
        self.assertEqual(serializer.data['username'], objectToSerialize['username'])
        self.assertEqual(serializer.data['password'], objectToSerialize['password'])
