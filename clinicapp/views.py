from django.shortcuts import render,redirect
from clinicapp.models import Patient,Clinicaldata
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from clinicapp.forms import ClinicalDataForm


class PatientlistView(ListView):
    model=Patient
    
    
class PatientCreateView(CreateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','secondname','age')
    
    
class PatientUpadateView(UpdateView):
    model=Patient
    success_url=reverse_lazy('index')
    fields=('firstname','secondname','age')
    
class PatientDeleteView(DeleteView):
    model=Patient
    success_url=reverse_lazy('index')
    
    
# FunctionBASED vIEWS
def addData(request,**kwargs):
    form=ClinicalDataForm()
    patient=Patient.objects.get(id=kwargs['pk'])
    if request.method=='POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
            
    return render(request, 'clinicapp/clinicaldata.html',{'form':form,
                'patient':patient})
    
def analyze(request,**kwargs):
    data=Clinicaldata.objects.filter(patient_id=kwargs['pk'])
    responsedata=[]
    for eachEntry in data:
        if eachEntry.componentName=='hw':
            heightAndWeight=eachEntry.componentsValue.split('/')
            if(len(heightAndWeight)>1):
                feetToMeter=float(heightAndWeight[0])*0.4536
                BMI=(float(heightAndWeight[1]))/(feetToMeter*feetToMeter)
                bmiEntry=Clinicaldata()
                bmiEntry.componentName='BMI'
                bmiEntry.componentsValue=str(BMI)
                responsedata.append(bmiEntry)
        responsedata.append(eachEntry)
    return render(request,'clinicapp/generate.html',{'data':responsedata})