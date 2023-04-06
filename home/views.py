# import the necessary modules
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from home.models import comment, Note
import openreview

def loginpage(request):
    page = 'login'
    if request.method =='POST':
        username= request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
          user = user.objects.get(username=username)
        except:
            messages.error(request , 'user does not exist')
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request  , user)
            return redirect('home')    
    context = {'page': page}
    return render(request ,'login.html',context)
# Create your views here.
def logoutuser(request):
    logout(request)
    return redirect('login')

def registeruser(request):
    page = 'register'
    form =  UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username  = user.username.lower()
            user.save()
            login(request , user)
            return redirect('home')


    context = {'form':form}
    return render(request , 'login.html' , context)
import openreview

def home(request):
    # Create an OpenReview client object
    client = openreview.Client(baseurl='https://api.openreview.net')
    n = []
    # Search for Article notes
    notes = Note.objects.all()
    for note in notes:
     search_results = client.get_note(id=note.note_id)
     print("Note:", note.author)
     comments = note.comments.all()
     c=[]
     for comment in comments:
        if comment.parent_comment is None:
         replies = comment.replies.all()
         c.append({"author":comment.author,"content":comment.content,"replies":replies,"id":comment.id})
     N = {'Title':search_results.content['title'],"abstract":search_results.content['abstract'],"comments":c,"id":note.note_id}
     n.append(N)    


    # Extract the article data from the search results


    # Render the homepage template with the list of articles
    context = {"notes":n}
    return render(request, 'home.html', context)
def comments(request):
   id = request.GET.get('pk')
   if request.method=='POST':
      com = request.POST.get('comment')
      c = comment()
      c.author=request.user
      c.content= com
      c.note= Note.objects.get(note_id  = id)
      c.save()
   return redirect('home')
def reply(request):
   id = request.GET.get('pk')
   comment__id = request.GET.get('cid')
   if request.method=='POST':
      com = request.POST.get('reply')
      c = comment()
      c.author=request.user
      c.content= com
      c.note= Note.objects.get(note_id  = id)
      c.parent_comment = comment.objects.get(id = comment__id)
      c.save()
   return redirect('home')
 
