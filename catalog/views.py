from django.shortcuts import render, redirect
from catalog.models import Article, ArticleBias
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import os
from news_checker_website import settings
from django.http import HttpResponse

# Create your views here.
# Homepage view: sets the username cookie here (possibly change later?)
def index(request):
    # Renders page and gets response (so cookie can be set)
    response = render_to_response('index.html', {
        'authenticated': request.user.is_authenticated,
        'username': request.user.get_username()
    }, RequestContext(request))

    # Creates cookie used for extension
    if request.user.is_authenticated:
        response.set_cookie('news_checker_username', request.user.get_username())
    else:
        response.delete_cookie('news_checker_username')
    print(request.user.get_username())
    print(request.COOKIES.get('news_checker_username'))
    return response

# About page view
def about(request):
    return render(request, 'about.html')

# Download page view
def download(request):
    return render(request, 'download.html')

def firefox_download(request):
    zip_file = os.path.join(settings.STATIC_ROOT, 'zip/news_checker_extension_firefox.zip', 'r')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'news_checker_extension_firefox.zip'
    return response

def chrome_download(request):
    zip_file = os.path.join(settings.STATIC_ROOT, 'zip/news_checker_extension_chrome.zip', 'r')
    response = HttpResponse(zip_file, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'news_checker_extension_chrome.zip'
    return response

# Add view: adds an entry to the database here
def add(request):
    # Gets message from extension (which redirects here)
    url = request.GET.get('url')
    text = request.GET.get('text')
    bias = request.GET.get('bias')

    # Double checks that the url is set, and that the article is set. If the article doesn't exist, it creates it here.
    if url != None:
        bias = int(bias)
        try:
            article = Article.objects.get(url__exact=url)
        except:
            article = Article(url=url, text=text.replace("_", " "))
            article.save()
        try:
            article_bias = ArticleBias.objects.filter(article__exact=article).get(reader__exact=request.user)
            used_status = article_bias.used
            article_bias.delete()
            article_bias = ArticleBias(article=article, bias=bias, reader=request.user, used=used_status)
        except:
            article_bias = ArticleBias(article=article, bias=bias, reader=request.user)
        article_bias.save()
    return render(request, 'add.html')

# Register view: Uses the UserForm to register a new user.
def register(request):
    if request.method == 'POST':
        f = UserForm(request.POST)
        if f.is_valid():
            f.save()
            return render(request, 'register_success.html')
    else:
        f = UserForm()
    return render(request, 'register.html', {'form': f})

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email' ]

# View to list ArticleBiases readers make
class ArticleBiasesByUserListView(LoginRequiredMixin, generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = ArticleBias
    template_name ='articlebias_list_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ArticleBias.objects.filter(reader=self.request.user).order_by('used')

# Change password page
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form,
        'user': request.user
    })
