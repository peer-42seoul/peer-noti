from django.http import HttpResponse
from django.http import Http404
from .slack_api import SlackAPI

def index(request):
    return HttpResponse("peer-noti slackbot 페이지입니다.<br>"
                        "dm을 보내려면 [http://127.0.0.1:8000/slackbot/send/dm/]로 이동하세요!")


def send_dm(request):
    try:
        intra_id = request.GET.get('id')
        if intra_id is None:
            raise Http404("id: Param not found. <br>"
                          "dm을 보낼 유저의 intra id를 아래 주소의 파라미터로 넣어주세요! <br>"
                          "http://127.0.0.1:8000/slackbot/send/dm/?id=[intra_id]")

        slack = SlackAPI()
        user_id = slack.get_user_id(intra_id)
        slack.post_message(user_id, intra_id)


    except Http404 as e:
        # 요청 매개변수가 없는 경우 예외 처리
        response = HttpResponse(str(e))
        response.status_code = 404
        return response

    return HttpResponse(intra_id + "님께 DM을 전송합니다.")