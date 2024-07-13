# Importation des modules de formulaire
from datetime import datetime, time, timedelta
from django import forms
from django.utils import timezone
from tempus_dominus.widgets import DateTimePicker


from functools import partial



from accueil.models import TITLE_CHOICES, Rend

# Importation du widget DateInput
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

# Créer une liste d'horaires pour le champ d'horaire
TIME_CHOICES = [
    ('08:00', '08:00'),
    ('09:00', '09:00'),
    ('10:00', '10:00'),
    # Ajoutez d'autres heures au besoin
]
CHOIX_ANCIEN_PATIENT = [
    ('Oui', 'Oui'),
    ('Non', 'Non')
]

# Classe pour définir les champs du formulaire
class RendForm(forms.ModelForm):
    nom = forms.CharField(label="nom complet*", max_length=40, required=True)
    courriel = forms.EmailField(label="courriel", max_length=50)
    Ancien_patient = forms.ChoiceField(
        label='Etes-vous déjà patient à notre cabinet?*', 
        choices=CHOIX_ANCIEN_PATIENT,
        widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}),
        required=True
    )
    téléphone = forms.IntegerField(required=True)
    Raison = forms.ChoiceField(label='Raison de votre visite* :', choices=TITLE_CHOICES,required=True)
    La_Date = forms.DateTimeField(widget=DateTimePicker(
        options={
            'format': 'YYYY-MM-DD HH:mm',  # Format de date et heure
            'sideBySide': True  # Afficher le sélecteur de date et heure côte à côte
        }
    ))
    L_Heure = forms.TimeField(label='Heure*', widget=forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),required=True)


    def clean_La_Date(self):
        date_selected = self.cleaned_data['La_Date']
        appointments_on_date = Rend.objects.filter(La_Date=date_selected)
        if appointments_on_date.exists():
            raise forms.ValidationError("Cette date est déjà prise. Veuillez choisir une autre date.")
        return date_selected

    def clean(self):
        cleaned_data = super().clean()
        rendezvous_date = cleaned_data.get('La_Date')

        # Récupérer toutes les heures déjà prises pour la date choisie
        heures_prises = Rend.objects.filter(La_Date=rendezvous_date).values_list('L_Heure', flat=True)

        # Créer une liste d'heures disponibles
        heures_disponibles = [heure for heure, _ in TIME_CHOICES if heure not in heures_prises]
        heures_disponibles = [datetime.strptime(heure, '%H:%M').time() for heure in heures_disponibles]

        # Exclure les heures après 17h00 et avant 8h00
        heures_disponibles = [heure for heure in heures_disponibles if time(8, 0) <= heure <= time(17, 0)]

        # Vérifier s'il existe au moins une heure disponible pour la date choisie
        if not heures_disponibles:
            raise forms.ValidationError("Toutes les heures pour cette date sont prises. Veuillez choisir une autre date.")

        return cleaned_data

    class Meta:
        model = Rend
        fields = ['nom', 'courriel', 'Ancien_patient', 'téléphone', 'Raison', 'La_Date', 'L_Heure','cancel_reason']
        widgets = {
            'La_Date': DateInput(),
        }


from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    
   
    
    sujet = forms.CharField()

    email = forms.CharField(required = True)
    
    message = forms.CharField(widget=forms.Textarea , required = True)


    def __str__(self):
        return self.sujet

    class Meta:
          model = Contact
          fields = ['sujet', 'email','message']          