from django.contrib import messages
from django.http import Http404
from .slack_api import SlackAPI
from django.shortcuts import render, redirect
from .forms import UserForm


def index(request):
    return render(request, 'slackbot/index.html')

def send_dm(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                intra_id = form.cleaned_data['intra_id']
                message = form.cleaned_data['message']
                slack = SlackAPI()
                user_id = slack.get_user_id(intra_id)
                slack.post_message(user_id, intra_id, message)
                messages.success(request, "메시지가 성공적으로 전송되었습니다.")
                return redirect('slackbot:send_dm')

            except Http404 as e:
                messages.error(request, str(e))
    else:
        form = UserForm()
    return render(request, 'slackbot/dm_form.html', {'form': form})
