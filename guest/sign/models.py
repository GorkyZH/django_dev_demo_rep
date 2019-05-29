from django.db import models

# Create your models here.
# 发布会表

class Event(models.Model):
    name = models.CharField(max_length=100)  #发布会标题
    limit = models.IntegerField()  # 参加人数
    status = models.BooleanField()  # 状态
    address = models.CharField(max_length=200)  # 地点
    start_time = models.DateTimeField('events_time')  # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间

    def __str__(self):
        return self.name

# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    realname = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname