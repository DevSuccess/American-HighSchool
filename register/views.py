from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import Registration


def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire si elles sont valides
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip_code']
            country = form.cleaned_data['country']
            message = form.cleaned_data['message']

            # Créez une instance du modèle Registration avec les données du formulaire
            registration = Registration(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                age=age,
                gender=gender,
                message=message,
                city=city,
                zip_code=zip_code,
                country=country,

            )

            # Enregistrez l'objet dans la base de données
            registration.save()
            messages.success(request, "Congratulations ! Register Successfully")
            # Redirigez vers une autre page ou effectuez d'autres actions
            return redirect('home:index')
        else:
            messages.warning(request, "Invalid Input Data")
    else:
        form = RegisterForm()

    return render(request, 'register/index.html', {'form': form})
