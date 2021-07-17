from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Client)
admin.site.register(Client_Database)
admin.site.register(Staff_Database_Access)
admin.site.register(Activity)