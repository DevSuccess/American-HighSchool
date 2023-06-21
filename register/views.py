from django.shortcuts import render, redirect
from .forms import FirstStepForm
from .models import Registration


def index(request):
    if request.method == 'POST':
        form = FirstStepForm(request.POST)
        if form.is_valid():
            # Traitez les données du formulaire si elles sont valides
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']

            # Créez une instance du modèle Registration avec les données du formulaire
            registration = Registration(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                age=age,
                gender=gender
            )

            # Enregistrez l'objet dans la base de données
            registration.save()

            # Redirigez vers une autre page ou effectuez d'autres actions
            return redirect('home:index')
    else:
        form = FirstStepForm()

    return render(request, 'register/index.html', {'form': form})
