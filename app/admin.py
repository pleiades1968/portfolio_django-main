from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Profile, Work, Experience, Education, Software, Technical

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)
# Register your models here.
