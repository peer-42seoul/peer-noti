from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config.settings import SLACK_INFO
from django.http import Http404


class SlackAPI:
    """
    슬랙 API 핸들러
    """

    def __init__(self):
        self.client = WebClient(token=SLACK_INFO["BOT_TOKEN"])

    def get_user_id(self, intra_id):
        response = self.client.users_list()
        for member in response['members']:
            if member['profile']['real_name'] == intra_id:
                return member['id']
        raise Http404("id: [" + intra_id + "]에 해당하는 유저가 존재하지 않습니다.")

    def post_message(self, channel_id, name, message):
        """
        슬랙 채널에 메세지 보내기
        channel: user id를 넣을 경우 user에게, channel id를 넣을 경우 channel에게 메세지가 전송됨
        """
        try:
            result = self.client.chat_postMessage(
                channel=channel_id,
                text= name + "님 안녕하세요! \n" + message
            )
        except SlackApiError as e:
            print(f"Error posting message: {e}")
        return result
