from django import forms
from clinicapp.models import Patient,Clinicaldata

class PatientsForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'
        
class ClinicalDataForm(forms.ModelForm):
    class Meta:
        model=Clinicaldata
        fields='__all__'