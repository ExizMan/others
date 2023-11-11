from django.shortcuts import render, redirect
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
def index(request):
    """ Домашня страница представления"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics_two': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Выводит отдельную тему"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries_two':entries}
    return render(request, 'learning_logs/topic.html',context)

def new_topic(request):
    """Новая тема"""
    if request.method != 'POST':
        #Данные не отправлялись, создается новая форма
        form = TopicForm()
    else:
        #Отправлены данные, обрабатываем+++
        form=TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # Вывести пустую или недействительную форму
    context = {'form_two':form}
    return render(request,'learning_logs/new_topic.html',context)

def new_entry(request,topic_id):
    topic=Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid():
            new_entry=form.save(commit=False)
            new_entry.topic=topic
            new_entry.save()
            redirect('learning_logs:topic ', topic_id=topic.id)
    context = {'topic':topic,'form_two':form}
    return render(request, 'learning_logs/new_entry.html',context)

# Create your views here.