from django.db import models
from utils import models as utils_models

class Calculation(models.Model):
    pages = models.IntegerField()
    cpages = models.IntegerField()
    fmt = models.ForeignKey(utils_models.PrintFormat)
    inks = models.ForeignKey(utils_models.InkFaceBack)
    ps = models.ForeignKey(utils_models.PubSquare)
    
    
