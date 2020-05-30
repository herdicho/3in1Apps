from django.db import models

# Create your models here.

class Topic(models.Model):
    topic = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # output name di list model(database) customer
    def __str__(self):
        return self.topic 

class Note(models.Model):
    topic = models.ForeignKey(Topic, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(max_length=3000, null=True)
    title = models.CharField(max_length=200, null=True)
    clear = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return 'Topic : %s, Title : %s' % (self.topic, self.title)
