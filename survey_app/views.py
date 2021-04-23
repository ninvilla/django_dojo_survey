from django.shortcuts import render, redirect

# IMPORTANT: run python manage.py migrate in project directory to update database and manage sessions

LOCATIONS = (
    'Schertz',
    'San Marcos',
    'Houston'
)

LANGS = (
    'Python',
    'Java',
    'Ruby'
)

def index(request):
    context = {
        'locations': LOCATIONS,
        'languages': LANGS
    }
    return render(request, 'index.html', context)

def survey(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
