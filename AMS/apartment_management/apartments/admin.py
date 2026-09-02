from django.contrib import admin
from .models import User, Apartment, Complaint, Payment

# Register models
admin.site.register(User)
admin.site.register(Apartment)
admin.site.register(Complaint)
admin.site.register(Payment)
