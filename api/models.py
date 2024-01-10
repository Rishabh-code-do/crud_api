from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Count
from django.utils import timezone
# Create your models here.



class Box(models.Model):
    length = models.FloatField()
    breadth = models.FloatField()
    height = models.FloatField()
    area = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.area = self.calculate_area()
        self.volume = self.calculate_volume()
        self.check_conditions_on_save()
        super().save(*args, **kwargs)

    def calculate_area(self):
        return 2 * (self.length * self.breadth + self.length * self.height + self.breadth * self.height)

    def calculate_volume(self):
        return self.length * self.breadth * self.height
    

    def check_conditions_on_save(self):
        self.check_average_area()
        self.check_average_volume()
        self.check_total_boxes_added()
        self.check_total_boxes_added_by_user()

    def check_average_area(self):
        total_boxes = Box.objects.all().count()
        avg_area = Box.objects.aggregate(Avg('area'))['area__avg'] or 0
        avg_area = (self.area+avg_area)/(total_boxes+1)
        A1 = getattr(settings, 'A1', 100) 
        if avg_area > A1:
            raise ValueError("Average area exceeds the allowed limit.")

    def check_average_volume(self):
        total_boxes = Box.objects.all().count()
        user_boxes = Box.objects.filter(created_by=self.created_by)
        avg_volume = user_boxes.aggregate(Avg('volume'))['volume__avg'] or 0
        avg_volume = (self.area+avg_volume)/(total_boxes+1)
        V1 = getattr(settings, 'V1', 1000)  
        if avg_volume > V1:
            raise ValueError("Average volume for the user exceeds the allowed limit.")

    def check_total_boxes_added(self):
        week_ago = timezone.now() - timezone.timedelta(weeks=1)
        total_boxes_added = Box.objects.filter(created_at__gte=week_ago).count()
        L1 = getattr(settings, 'L1', 100)   
        if total_boxes_added > L1:
            raise ValueError("Total boxes added in the last week exceeds the allowed limit.")

    def check_total_boxes_added_by_user(self):
        week_ago = timezone.now() - timezone.timedelta(weeks=1)
        total_user_boxes_added = Box.objects.filter(created_by=self.created_by, created_at__gte=week_ago).count()
        L2 = getattr(settings, 'L2', 50)  
        if total_user_boxes_added > L2:
            raise ValueError("Total boxes added by the user in the last week exceeds the allowed limit.")




