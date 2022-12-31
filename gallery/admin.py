from django.contrib import admin
from gallery.models import Gallery
from .models import UserProfile
from .models import Customer
from .models import Message


admin.site.register(Gallery)
admin.site.register(UserProfile)
admin.site.register(Customer)
admin.site.register(Message)
