from django.http import HttpResponse


def index(request):
    return HttpResponse("peer-noti slackbot 페이지입니다.")