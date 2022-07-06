from django.contrib import admin
# from .models import Catigoriy, Test_Types
from .models import *


# Register your models here.
admin.site.register(Catigoriy)
admin.site.register(Test_Types)
admin.site.register(Test_question)