from django.contrib import admin

from notice.models import Notice


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'create_at', 'modify_at') #보여줌
    list_filter = ('modify_at',) #보기분류(오늘/지난7일/지난30일)
    search_fields = ('title', 'content') #검색