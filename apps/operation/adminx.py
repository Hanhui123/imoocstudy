# __author:   巧笑倩兮
# date  2018/11/8

import xadmin
from operation.models import UserAsk, CourseComments, UserFavorite,  UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'user_name', 'add_time']
    search_fields = ['name', 'mobile', 'user_name']
    list_filter = ['name', 'mobile', 'user_name', 'add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['fav_id', 'fav_type', 'add_time']
    search_fields = ['fav_id', 'fav_type']
    list_filter = ['fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
