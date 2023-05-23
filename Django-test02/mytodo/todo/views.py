from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todo/todo_list.html', {'todos' : todos})


# 상세 보기 페이지
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

# To do 생성 페이지
def todo_post(request):
    if request.method == "POST" :
        # 만약 들어오는 request가 POST라면
        form = TodoForm(request.POST)
        # form에다가 request의 내용을 넣고
        if form.is_valid():
            #form에 내용이 있다면
            todo = form.save(commit=False)
            #todo에 form의 내용을 저장하고
            todo.save()
            #todo를 데이터베이스에 저장한다
            return redirect('todo_list')
            #그리고 todo_list라는 url로 redirect 하라는 것을 반환한다
    else:
        #만약 들어오는 요청이 POST가 아니라면
        form = TodoForm()
        #폼을 포함한 템플릿 페이지를 보여 준다
    return render(request, 'todo/todo_post.html', {'form' : form})
    #마지막으로 form을 전달해 템플릿에 폼을 나타내고, 정상적인 POST 요청은 form 데이터를 불러와 저장한다

## def todo_edit(request, pk): todo = Todo.objects.get (id-pk) if request.moedel == "TOST")
def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    #기존 Todo의 데이터를 pk라는 id값으로 구분해서 가지고 온 뒤 todo라는 변수에 저장
    if request.method == "POST":
        form = TodoForm(request.POST, instance = todo )
        #새로운 post와는 달리 instance를 통해 전달한다
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        #POST 요청이 아닌 다른 요청일 경우
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form' : form})
    #todo_edit.html로 값을 반환한다.

#완료 목록 뷰
def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todo/done_list.html', {'dones': dones})

#완료로 바꾸는 뷰
def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')

def todo_reload(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = False
    todo.save()
    return redirect('done_list')