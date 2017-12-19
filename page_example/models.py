# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm, ModelChoiceField


# Create your models here.
class InstallType(models.Model):
    title = "安装类型"
    # description of the install type
    content = models.CharField(max_length=30, verbose_name="描述")
    code = models.CharField(max_length=10, verbose_name="编号")

    def __unicode__(self):
        return self.content


class InstallTypeForm(ModelForm):
    class Meta:
        model = InstallType
        fields = ['content', 'code']


class CombineType(models.Model):
    title = "组装"
    content = models.CharField(max_length=30, verbose_name="描述")
    code = models.CharField(max_length=10, verbose_name="编号")

    def __unicode__(self):
        return self.content


class CombineTypeForm(ModelForm):
    class Meta:
        model = CombineType
        fields = ['content', 'code']


class Category(models.Model):
    title = "类型"
    content = models.CharField(max_length=30, verbose_name="描述", primary_key=True)
    code = models.CharField(max_length=10, verbose_name="编号")

    def __unicode__(self):
        return self.content


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["content", "code"]


class Polar(models.Model):
    title = "极性"
    content = models.CharField(max_length=30, verbose_name="描述")
    code = models.CharField(max_length=10, verbose_name="编号")

    def __unicode__(self):
        return self.content


class PolarForm(ModelForm):
    class Meta:
        model = Polar
        fields = [ u'content', 'code']


class Property(models.Model):
    title = "特性"
    content = models.CharField(max_length=30, verbose_name="描述")
    code = models.CharField(max_length=10, verbose_name="编号")

    def __unicode__(self):
        return self.content


class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['content', 'code']


class OutLook(models.Model):
    title = "外形"
    content = models.CharField(max_length=30, verbose_name="描述")
    code = models.CharField(max_length=10, verbose_name="编号")

    def __unicode__(self):
        return self.content


class OutLookForm(ModelForm):
    class Meta:
        model = OutLook
        fields = ['content', 'code']




class ConnectorCable(models.Model):
    title = "Cable"
    content_type = models.ForeignKey(Category)
    polar_type = models.ForeignKey(Polar)
    install_type = models.ForeignKey(InstallType)
    loss_rate = models.FloatField()
    outer_diameter = models.FloatField()
    inner_diameter = models.FloatField()

    cable_type = models.CharField(max_length=30)
    upper_frequency = models.FloatField()
    outlook_type = models.ForeignKey(OutLook)
    property = models.ForeignKey(Property)
    combine_type = models.ForeignKey(CombineType)
    document = models.FileField(upload_to="connectorCable/")
    full_witc = models.CharField(max_length=30)
    combo_short_witc = models.CharField(max_length=10)
    image = models.ImageField(upload_to="connectorCable/")
    comments = models.CharField(max_length=100)
    reserved1 = models.CharField(max_length=100)
    reserved2 = models.CharField(max_length=100)


class ConnectorPcb(models.Model):
    title = "connector_pcb"
    content_type = models.ForeignKey(Category)
    polar_type = models.ForeignKey(Polar)
    install_type = models.ForeignKey(InstallType)
    standing_wave = models.FloatField()
    upper_frequency = models.FloatField()
    outlook_type = models.ForeignKey(OutLook)
    property = models.ForeignKey(Property)
    full_witc = models.CharField(max_length=30)
    combo_short_witc = models.CharField(max_length=10)
    document = models.FileField(upload_to="connectorCable/")
    image = models.ImageField(upload_to="connectorCable/")
    comments = models.CharField(max_length=100)
    reserved1 = models.CharField(max_length=100)
    reserved2 = models.CharField(max_length=100)


class ConnectorPcbForm(ModelForm):
    class Meta:
        model = ConnectorPcb
        exclude = ['comments', 'reserved1', 'reserved2']


class ConnectorCableForm(ModelForm):
    class Meta:
        model = ConnectorCable
        exclude = ['comments', 'reserved1', 'reserved2']






