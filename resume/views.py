from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm, EducationFormSet, ExperienceFormSet
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def home(request):
    return render(request, 'resume/index.html')


def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        education_formset = EducationFormSet(request.POST)
        experience_formset = ExperienceFormSet(request.POST)
        if form.is_valid() and education_formset.is_valid() and experience_formset.is_valid():
            resume = form.save()
            education_instances = education_formset.save(commit=False)
            for instance in education_instances:
                instance.resume = resume
                instance.save()
            education_formset.save_m2m()
            experience_instances = experience_formset.save(commit=False)
            for instance in experience_instances:
                instance.resume = resume
                instance.save()
            experience_formset.save_m2m()
            return redirect('resume_templates', resume_id=resume.id)
    else:
        form = ResumeForm()
        education_formset = EducationFormSet()
        experience_formset = ExperienceFormSet()
        
    return render(request, 'resume/create_resume.html', {
        'form': form,
        'education_formset': education_formset,
        'experience_formset': experience_formset
    })




def generate_pdf(request, resume_id, template_name):
    resume = get_object_or_404(Resume, pk=resume_id)
    template_path = f'resume/pdf/{template_name}.html'
    context = {'resume': resume}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{resume.full_name}_resume.pdf"'
    

    template = get_template(template_path)
    html = template.render(context)
    
   
    pisa_status = pisa.CreatePDF(html, dest=response)
  
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>') 
    return response

def resume_templates(request, resume_id=None):
    return render(request, 'resume/resume_templates.html', {'resume_id': resume_id})


def about(request):
    return render(request, 'resume/about.html')
