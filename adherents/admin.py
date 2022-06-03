from django.contrib import admin

from .models import Adherent 
from .models import Entraineur
from .models import Coach
from .models import Entrainement
from .models import Role


admin.site.register(Adherent)
admin.site.register(Entraineur)
admin.site.register(Coach)
admin.site.register(Entrainement)
admin.site.register(Role)
