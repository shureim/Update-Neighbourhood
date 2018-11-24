from django.contrib import admin
from .models import Neighborhood,UserStatus,Business,Post,Health,Police


# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(UserStatus)
admin.site.register(Business)
admin.site.register(Post)
admin.site.register(Health)
admin.site.register(Police)
