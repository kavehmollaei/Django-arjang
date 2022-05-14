from django.contrib import admin
from Store.models import DataAccessed, EntryTable, Store,Topic,Page, TopicTable,Person



admin.site.register(Store)
admin.site.register(Page)
admin.site.register(DataAccessed)
admin.site.register(Topic)
admin.site.register(TopicTable)
admin.site.register(EntryTable)
admin.site.register(Person)

# Register your models here.
