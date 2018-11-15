from django.shortcuts import render
from django.views.generic import View
from organization.models import CourseOrg, CityDict

# Create your views here.


class OrgView(View):
    """课程列表"""
    def get(self, request):
        # 课程机构
        all_org = CourseOrg.objects.all()
        # 所在城市
        all_city = CityDict.objects.all()
        return render(request, "org-list.html", {"all_org": all_org, "all_city": all_city})