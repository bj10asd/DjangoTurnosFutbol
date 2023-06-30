from django.forms import ModelForm, DateInput
from canchas.models import Turnos
from django import forms


class TurnosForm(ModelForm):
    class Meta:
        model = Turnos
        fields = ["user_id", "cancha_id", "fecha_ini", "fecha_fin"]
        
        widgets = {
            "user_id": forms.TextInput(
                
                attrs={"class": "form-control","disabled":"disabled"}#, "placeholder": "Enter event title"}
            ),
            "cancha_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    #"placeholder": "Enter event description",
                }
            ),
            "fecha_ini": forms.DateTimeInput(
                format=('%Y-%m-%dT%H:%M'),
                attrs={'type'       : 'datetime-local',
                       'placeholder': 'dd-mm-yyyy (DOB)',
                       'class'      : 'form-control'}
            ),
                
                    #DateInput(
                #attrs={"type": "datetime-local", "class": "form-control"},
                #format="%Y-%m-%dT%H:%M",
                #),
            "fecha_fin": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                #format="%Y-%m-%dT%H:%M",
            ),
        }
        #exclude = ["user"]

    """def __init__(self, *args, **kwargs):
        super(TurnosForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)"""


