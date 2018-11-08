#__author:   巧笑倩兮
#date  2018/11/8


import xadmin
from courses.models import Course, Lesson, Video, CourseResource


# 注册课程
class CourseAdmin(object):
    list_display = ['name', 'desc', 'detil', 'degree', 'lenarn_times',
                    'students', 'fav_nums', 'image', 'clink_nums', 'add_time']
    search_fields = ['name', 'desc', 'detil', 'degree', 'lenarn_times', 'students', 'fav_nums', 'image', 'clink_nums']
    list_filter = ['name', 'desc', 'detil', 'degree', 'lenarn_times', 'students',
                   'fav_nums', 'image', 'clink_nums', 'add_time']


# 课程章节注册
class LessonAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


# 视频信息
class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


# 课程资源
class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
