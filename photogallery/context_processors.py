import datetime

def current_year(request):
    return { "CURRENT_YEAR": datetime.datetime.now().strftime('%Y') }