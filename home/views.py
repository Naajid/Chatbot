from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
import wolframalpha
import wikipedia
from textblob import TextBlob
import threading
from home.models import Order, Wishlist, Complaint


# from pathlib import Path

question = "none"
# Create your views here.
# df = Path("../static/")
# file1 = df / "sample.txt"


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    else:
        return render(request, 'index.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        # CHECK IF CREDENTIALS ARE CORRECT
        user = authenticate(username=username, password=password)
        # A BACKEND AUTHENTICATED THE CREDENTIALS
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # NO BACKEND AUTHENTICATED THE CREDENTIALS

            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")


def botfunc():
    global question
    question = TextBlob(question).correct()


def check(string, sub_str):
    if (string.find(sub_str) == -1):
        return 0
    else:
        return 1


def botsearch(request):
    global question
    question = request.GET.get('question')
    question = question.lower()
    print(question)
    name = "your name"
    made = "made you"
    create = "created you"
    creator = "your creator"
    string = "orders complaints wishlist"

    if(check(question, name) == 1):
        ans = "My name is JGI BOT and I am made by Naajid."
        print(ans)
        text_file = open("static/sample.txt", "w")
        n = text_file.write(ans)
        return render(request, 'index.html', {'ans': ans})

    elif(check(string, question) == 1):
        if(question == "orders"):
            user = Order.objects.first()
            ans1 = getattr(user, "item")
            ans2 = getattr(user, "price")
            ans3 = getattr(user, "id")
            ans = "Your last order was    " + str(ans1)+ " " + "priced at" + " " + str(ans2)+ " " + "with Order ID   "+ str(ans3)
            text_file = open("static/sample.txt", "w")
            n = text_file.write(str(ans))
            return render(request, 'index.html', {'ans': ans})

        if(question == "complaints")  :
            user = Complaint.objects.first()
            ans1 = getattr(user, "desc")
            ans2 = getattr(user, "status")
            ans = "Your last complaint was :   " + str(ans1)+ " " + ". Status :" + " " + str(ans2)
            text_file = open("static/sample.txt", "w")
            n = text_file.write(str(ans))
            return render(request, 'index.html', {'ans': ans})

        if(question == "wishlist"):
            user = Wishlist.objects.first()
            ans1 = getattr(user, "item")
            ans2 = getattr(user, "price")
            ans = "The last item you wishlisted was :   " + str(ans1)+ " " + " presently priced at" + " " + str(ans2)
            text_file = open("static/sample.txt", "w")
            n = text_file.write(str(ans))
            return render(request, 'index.html', {'ans': ans})
            
    elif(check(question,made)==1 or check(question, create)==1 or check(question, creator)==1):
            ans = "I am made by Naajid."
            print(ans)
            text_file = open("static/sample.txt", "w")
            n = text_file.write(ans)
            return render(request, 'index.html', {'ans': ans})





    else:
        t1 = threading.Thread(target=botfunc)
        t1.start()
        t1.join()

    try:
        client = wolframalpha.Client("6QV2GX-XQ98P6YTAQ")
        res = client.query(question)
        ans = next(res.results).text
        text_file = open("static/sample.txt", "w")
        n = text_file.write(ans)
        text_file.close()
        print(ans)
        return render(request, 'index.html', {'ans': ans})
    except Exception:
        try:
            ans = "I got nothing related to your query."
            print(ans)
            text_file = open("static/sample.txt", "w")
            n = text_file.write(ans)
            text_file.close()
            return render(request, 'index.html', {'ans': ans})

        except Exception:
            print("TRY RE-RUNNING THE PROGRAM")


def botsearch1(request):
    global question
    question = request.GET.get('question')
    print(question)
