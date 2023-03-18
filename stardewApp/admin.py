from django.contrib import admin

# Register your models here.

from .models import Season, Location, Item, Villager, Schedule, SeasonAdmin, LocationAdmin, ItemAdmin, VillagerAdmin, \
    ScheduleAdmin

admin.site.register(Season, SeasonAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Villager, VillagerAdmin)
admin.site.register(Schedule, ScheduleAdmin)