from django.test import TestCase
from api.models.connection import ConnectionDb

class ConnectionTests(TestCase):

    def test_can_save_object(self):
        """
        should save object
        """

        objectToSave = {
            'db_name':'db_name',
            'host':'127.0.0.1',
            'port':5432,
            'username':'username',
            'password':'password'
        }
        database = ConnectionDb()
        database.db_name = objectToSave['db_name']
        database.host = objectToSave['host']
        database.port = objectToSave['port']
        database.username = objectToSave['username']
        database.password = objectToSave['password']
        database.save()
        databaseToCheck = ConnectionDb.objects.get(id=database.id)

        self.assertEqual(database, databaseToCheck)
        self.assertEqual(objectToSave['db_name'], databaseToCheck.db_name)
        self.assertEqual(objectToSave['host'], databaseToCheck.host)
        self.assertEqual(objectToSave['port'], databaseToCheck.port)
        self.assertEqual(objectToSave['username'], databaseToCheck.username)
        self.assertEqual(objectToSave['password'], databaseToCheck.password)
