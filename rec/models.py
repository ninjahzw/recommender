from django.db import models

# Create your models here.
class Hyb(models.Model):
    uid = models.IntegerField()
    mid = models.IntegerField()
    ori_rat = models.FloatField()
    biasedmf = models.FloatField()
    regsvd = models.FloatField()
    bpmf = models.FloatField()
    itemknn = models.FloatField()
    hyb = models.FloatField()
    algo = models.IntegerField()
    biased = models.FloatField()
    gen_sec_regsvd = models.FloatField()
    hknn_reg = models.FloatField()
    iknn_bias = models.FloatField()

    def __unicode__(self):
        return ""

    class Meta:
        db_table = "hyb"
