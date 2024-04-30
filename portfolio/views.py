from django.shortcuts import render
from .models import Project, Skill, Experience

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {'projects': projects})

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def skill_list(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio/skill_list.html', {'skills': skills})

def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience_list.html', {'experiences': experiences})