# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Publishert(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=50)
    copywrite_text = models.TextField()
    support_email = models.CharField(unique=True, max_length=255)
    support_phone = models.CharField(unique=True, max_length=15)
    address = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'publishert'


class Gamestudiot(models.Model):
	gsid = models.AutoField(primary_key=True)
	pid = models.ForeignKey(Publishert, db_column='pid', on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

	class Meta:
		managed = False
		db_table = 'gamestudiot'
# Unable to inspect table 'gamestudiot'
# The error was: list index out of range
