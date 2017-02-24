from django.db import models

class urltable(models.Model):
    myurl=models.CharField(name="myurl",verbose_name="myurl",max_length=30)
    orgurl=models.URLField(name="orgurl",verbose_name="orgurl")

    def __str__(self):
        return self.orgurl