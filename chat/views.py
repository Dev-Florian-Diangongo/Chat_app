from django.shortcuts import render,get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ChatMessageCreateForm


login_required
def chat(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public")
    chat_messages = chat_group.chat_messages.all()[:]
    form = ChatMessageCreateForm()
    if request.htmx :
        form = ChatMessageCreateForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                "message":message,
                'user':request.user
            }
            return render(request, "chat/partials/chat_message_p.html", context)
            
            
            
    return render(request, "chat/chat.html", {"chat_messages":chat_messages,
                                              'form':form})
