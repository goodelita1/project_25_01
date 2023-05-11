from datetime import datetime
from django.shortcuts import render
from .forms import StartScrapForm
from .tasks import bs_scraping

# Create your views here.
def start_scraping(request):
    if request.method=='POST':
        form = StartScrapForm(request.POST)
        if form.is_valid():
            time = str(request.POST.get('time', ''))
            bs_scraping.delay()
            return render(request, 'scrap_soup/start.html')
    else:
        form=StartScrapForm()
    return render(request, 'scrap_soup/start.html', {'form':form})
