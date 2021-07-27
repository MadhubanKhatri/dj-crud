from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Person

#RETRIEVE
def home(request):
    #Retrieve all the persons' datas.
    get_persons = Person.objects.all()
    params = {'datas': get_persons}
    return render(request, 'home.html', params)


#CREATE
def add_person(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        is_married = request.POST['bool']

        create_person = Person.objects.create(first_name=fname, last_name=lname, age=age, is_married=is_married)
        create_person.save()
        return redirect('home')
    else:
        return HttpResponse('GET reques is not allowed.')


#UPDATE
def update_person(request, id):
    get_person = get_person = Person.objects.get(id=id)
    params = {'data': get_person}
    return render(request, 'update.html', params)


def update(request, id):
    get_person = get_person = Person.objects.get(id=id)
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        is_married = request.POST['bool']

        get_person.first_name = fname
        get_person.last_name = lname
        get_person.age = age
        get_person.is_married = is_married
        get_person.save()
    else:
        return HttpResponse('Error')

    return redirect('home')



#DELETE
def delete_person(request, id):
    get_person = Person.objects.get(id=id)
    get_person.delete()
    return HttpResponse("person deleted")