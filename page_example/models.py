# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
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
    full_witc = models.CharField(max_length=30, primary_key=True)
    combo_short_witc = models.CharField(max_length=10)
    image = models.ImageField(upload_to="connectorCable/")
    comments = models.CharField(max_length=100)
    reserved1 = models.CharField(max_length=100)
    reserved2 = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)


class ConnectorPcb(models.Model):
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
    time = models.DateTimeField(auto_now_add=True)


class Converter(models.Model):
    a_content_type = models.ForeignKey(Category, related_name="a_category")
    a_polar_type = models.ForeignKey(Polar, related_name="a_polar")
    b_content_type = models.ForeignKey(Category, related_name="b_category")
    b_polar_type = models.ForeignKey(Polar, related_name="b_polar")
    standing_wave = models.FloatField()
    upper_frequency = models.FloatField()
    outlook_type = models.ForeignKey(OutLook)
    install_type = models.ForeignKey(InstallType)
    material = models.CharField(max_length=40)
    property = models.ForeignKey(Property)
    full_witc = models.CharField(max_length=30)
    document = models.FileField(upload_to="converter/")
    image = models.ImageField(upload_to="converter/")
    comments = models.CharField(max_length=100)
    reserved1 = models.CharField(max_length=100)
    reserved2 = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)


class CableCategory(models.Model):
    content = models.CharField(max_length=30)
    code = models.CharField(max_length=10)

    def __unicode__(self):
        return self.content


class Cable(models.Model):
    category_type = models.ForeignKey(CableCategory)
    upper_frequency = models.FloatField()
    outer_diameter = models.FloatField()
    resistance = models.FloatField()
    loss_coef_k1 = models.FloatField()
    loss_coef_k2 = models.FloatField()
    property = models.ForeignKey(Property)
    full_witc = models.CharField(max_length=30)
    document = models.FileField(upload_to="cable/")
    image = models.ImageField(upload_to="cable/")
    comments = models.CharField(max_length=100)
    reserved1 = models.CharField(max_length=100)
    reserved2 = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)



class ConverterForm(ModelForm):
    class Meta:
        model = Converter
        exclude = ['comments', 'reserved1', 'reserved2', 'time']


class ConnectorPcbForm(ModelForm):
    class Meta:
        model = ConnectorPcb
        exclude = ['comments', 'reserved1', 'reserved2', 'time']

    def __init__(self, *args, **kwargs):
        super(ConnectorPcbForm, self).__init__(*args, **kwargs)


class ConnectorCableForm(ModelForm):
    class Meta:
        model = ConnectorCable
        exclude = ['comments', 'reserved1', 'reserved2', 'time']


class CableForm(ModelForm):
    class Meta:
        model = Cable
        exclude = ['comments', 'reserved1', 'reserved2', 'time']





