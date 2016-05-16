from __future__ import unicode_literals

from django.db import models

from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save, post_delete


# Create your models here.


class Stopage(models.Model):
    name=models.CharField(max_length=120)
    adjacent=models.ManyToManyField("self",blank=True)
    # cost_from_source=models.DecimalField(max_digits=20, decimal_places=6, default=100000000)
    lattitude=models.DecimalField(max_digits=20, decimal_places=6, blank=True,null=True)
    longitude=models.DecimalField(max_digits=20, decimal_places=6, blank=True,null=True)


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name



class BusOption(models.Model):
    bus_name=models.CharField(max_length=120)
    cost=models.DecimalField(max_digits=10,decimal_places=2,default=10)
    edges=models.ManyToManyField('Edge',blank=True)



    def __unicode__(self):
        return self.bus_name+" "+str(self.cost)

    def __str__(self):
        return self.bus_name+" "+str(self.cost)


class Edge(models.Model):
    source=models.ForeignKey(Stopage,related_name="source")
    dest=models.ForeignKey(Stopage,related_name="dest")
    distance=models.DecimalField(max_digits=10,decimal_places=2,default=1.0)
    best_option=models.ForeignKey(BusOption,related_name="best_option",blank=True,null=True)

    def __unicode__(self):
        return self.source.name+" >> "+self.dest.name

    def __str__(self):
        return self.source.name+" >> "+self.dest.name

    def update_best_option(self):
        if self.busoption_set.all():
            print "Updating Best Option For "+self.__unicode__()
            best_option=self.busoption_set.order_by('cost')[0]
            self.best_option=best_option
            self.save()



def edge_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.source.adjacent.add(instance.dest)
    instance.dest.adjacent.add(instance.source)

pre_save.connect(edge_pre_save_receiver, sender=Edge)



def bus_option_post_save_receiver(sender, instance, *args, **kwargs):
    print "In bus option post save singnal"
    # edges=instance.edges.all()
    edges=Edge.objects.all()
    for edge in edges:
        edge.update_best_option()



post_save.connect(bus_option_post_save_receiver,sender=BusOption)
