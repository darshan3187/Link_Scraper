from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link
# Create your views here.

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')

        try:
            page = requests.get(site)
            soup = BeautifulSoup(page.text, 'html.parser')

            for link in soup.find_all('a'):
                link_address = link.get('href')
                if not link_address:
                    continue  # skip links without href
                link_text = link.string or "No text"
                Link.objects.create(address=link_address, name=link_text)
        except Exception as e:
            print("Error scraping site:", e)

        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data': data})

def clear(request):
    Link.objects.all().delete()
    # data = Link.objects.all()  # empty queryset
    return render(request, 'myapp/result.html')
