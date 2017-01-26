# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Bankaccountt(models.Model):
    card_number = models.TextField(primary_key=True)
    cvv2 = models.TextField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('Gamert', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bankaccountt'


class Buyt(models.Model):
    gid = models.ForeignKey('Gamert', models.DO_NOTHING, db_column='gid', related_name='+')
    gtid = models.ForeignKey('Gametitlet', models.DO_NOTHING, db_column='gtid', related_name='+')
    date = models.DateField()
    bank_useracc_flag = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'buyt'
        unique_together = (('gid', 'gtid', 'date'),)


class Discountt(models.Model):
    gtid = models.ForeignKey('Gametitlet', models.DO_NOTHING, db_column='gtid')
    disc_date = models.DateField()
    disc_from = models.DateField(blank=True, null=True)
    disc_due = models.DateField(blank=True, null=True)
    disc_percentage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discountt'
        unique_together = (('gtid', 'disc_date'),)


class Dlct(models.Model):
    gtid = models.ForeignKey('Gametitlet', models.DO_NOTHING, db_column='gtid', primary_key=True, related_name='+')
    main_gtid = models.ForeignKey('Gametitlet', models.DO_NOTHING, db_column='main_gtid', blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'dlct'


class Feedbackt(models.Model):
    gid = models.ForeignKey('Gamert', models.DO_NOTHING, db_column='gid', related_name='+')
    pid = models.ForeignKey('Publishert', models.DO_NOTHING, db_column='pid', related_name='+')
    date = models.DateField()
    title = models.CharField(max_length=40, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feedbackt'
        unique_together = (('gid', 'pid', 'date'),)


class Friendshipt(models.Model):
    gid1 = models.ForeignKey('Gamert', models.DO_NOTHING, db_column='gid1', related_name='+')
    gid2 = models.ForeignKey('Gamert', models.DO_NOTHING, db_column='gid2', related_name='+')
    date = models.DateField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'friendshipt'
        unique_together = (('gid1', 'gid2'),)


class Gaintrophyt(models.Model):
    tid = models.ForeignKey('Trophyt', models.DO_NOTHING, db_column='tid', related_name='+')
    gtid = models.ForeignKey('Gametitlet', models.DO_NOTHING, db_column='gtid', related_name='+')
    gid = models.ForeignKey('Gamert', models.DO_NOTHING, db_column='gid', related_name='+')
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gaintrophyt'
        unique_together = (('tid', 'gtid', 'gid'),)


class Gamert(models.Model):
    gid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    username = models.TextField(unique=True, blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    email = models.TextField(unique=True, blank=True, null=True)
    phone_number = models.TextField(unique=True, blank=True, null=True)
    user_account_balance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamert'


class Gamestudiot(models.Model):
    gsid = models.IntegerField()
    pid = models.ForeignKey('Publishert', models.DO_NOTHING, db_column='pid')
    name = models.CharField(unique=True, max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamestudiot'
        unique_together = (('gsid', 'pid'),)


class Gametitlet(models.Model):
    gtid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40, blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)
    gener = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    mp_support = models.NullBooleanField()
    refund_duration = models.IntegerField(blank=True, null=True)
    pid = models.ForeignKey('Publishert', models.DO_NOTHING, db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gametitlet'


class Gamingdevicet(models.Model):
    gdid = models.IntegerField(primary_key=True)
    is_active = models.NullBooleanField()
    owner = models.ForeignKey(Gamert, models.DO_NOTHING, blank=True, null=True)
    regitration_date = models.DateField(blank=True, null=True)
    registered_name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamingdevicet'
        unique_together = (('regitration_date', 'owner'), ('registered_name', 'owner'),)


class Hasgamet(models.Model):
    gdid = models.ForeignKey(Gamingdevicet, models.DO_NOTHING, db_column='gdid', related_name='+')
    gtid = models.ForeignKey(Gametitlet, models.DO_NOTHING, db_column='gtid', related_name='+')
    backed_up = models.NullBooleanField()
    download_date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hasgamet'
        unique_together = (('gdid', 'gtid'),)


class Messaget(models.Model):
    gid1 = models.ForeignKey(Gamert, models.DO_NOTHING, db_column='gid1', related_name='+')
    gid2 = models.ForeignKey(Gamert, models.DO_NOTHING, db_column='gid2', related_name='+')
    date = models.DateField()
    type = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=40, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    voice = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    gtid = models.ForeignKey(Gametitlet, models.DO_NOTHING, db_column='gtid', blank=True, null=True, related_name='+')
    tid = models.ForeignKey('Trophyt', models.DO_NOTHING, db_column='tid', blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'messaget'
        unique_together = (('gid1', 'gid2', 'date'),)


class Publishert(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=40, blank=True, null=True)
    copywrite_text = models.CharField(unique=True, max_length=100, blank=True, null=True)
    support_email = models.TextField(unique=True, blank=True, null=True)
    support_phone = models.TextField(unique=True, blank=True, null=True)
    address = models.CharField(unique=True, max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publishert'


class Ratet(models.Model):
    gid = models.ForeignKey(Gamert, models.DO_NOTHING, db_column='gid', related_name='+')
    gtid = models.ForeignKey(Gametitlet, models.DO_NOTHING, db_column='gtid', related_name='+')
    date = models.DateField(blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratet'
        unique_together = (('gid', 'gtid'),)


class Refundt(models.Model):
    gid = models.ForeignKey(Gamert, models.DO_NOTHING, db_column='gid', related_name='+')
    gtid = models.ForeignKey(Gametitlet, models.DO_NOTHING, db_column='gtid', related_name='+')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'refundt'
        unique_together = (('gid', 'gtid', 'date'),)


class Reviewt(models.Model):
    gid = models.ForeignKey(Gamert, models.DO_NOTHING, db_column='gid', related_name='+')
    gtid = models.ForeignKey(Gametitlet, models.DO_NOTHING, db_column='gtid', related_name='+')
    date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=40, blank=True, null=True)
    reviewtext = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reviewt'
        unique_together = (('gid', 'gtid'),)


class Sendgiftt(models.Model):
    gid1 = models.ForeignKey(Gamert, models.DO_NOTHING, db_column='gid1', related_name='+')
    gtid = models.ForeignKey(Gametitlet, models.DO_NOTHING, db_column='gtid', related_name='+')
    gid2 = models.ForeignKey(Gamert, models.DO_NOTHING, db_column='gid2', related_name='+')
    date = models.DateField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sendgiftt'
        unique_together = (('gid1', 'gtid', 'gid2'),)


class Trophyt(models.Model):
    tid = models.IntegerField()
    gtid = models.ForeignKey(Gametitlet, models.DO_NOTHING, db_column='gtid')
    name = models.CharField(max_length=40, blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trophyt'
        unique_together = (('tid', 'gtid'), ('name', 'gtid'),)
