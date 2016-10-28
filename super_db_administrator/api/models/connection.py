from django.db import models

# class DataBaseConfiguration(models.Model):
#     name = models.CharField(max_length=200, blank=False)

class ConnectionDb(models.Model):
    db_name = models.CharField(max_length=200, blank=False, null=False)
    host = models.CharField(max_length=500, blank=False, null=False)
    port = models.IntegerField(blank=False, null=False)
    ssl = models.IntegerField(blank=True, null=True)
    # when we will have more databases
    # maintenance_db = models.ForeignKey(MaintenanceDB, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)
