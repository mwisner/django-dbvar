import json
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from jsonfield import JSONField


class Variable(models.Model):
    '''
    generic variable storage... all the other options seemed to kind of suck.
    this one kind of sucks too because I don't know what I'm doing.
    '''
    key = models.SlugField(unique=True)
    value = JSONField(default={})
    
    @classmethod
    def set(cls, key, value):
        try:
            val = cls.objects.get(key=key)
            val.value = json.dumps(value)
        except cls.DoesNotExist:
            val = cls(key=key, value=json.dumps(value))

        val.save()
        val = val.value
        return val

    @classmethod
    def get(cls, key, default):
        try:
            val = cls.objects.get(key=key).value
        except cls.DoesNotExist:
            val = default
        return val
        
        
        
        
        
