from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def post_list(req):
    if req.method == 'GET':
        return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.all(),
        })

    elif req.method == 'POST':
        if 'red' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            })
        if 'ore' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.filter(color_tag = 'red'),
            })
        if 'yel' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            })
        if 'gre' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.all(),
            })
        if 'blu' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            })
        if 'pur' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.all(),
            })
        if 'upload' in req.POST:
            form = PhotoForm(req.POST, req.FILES)
            if not form.is_valid():
                raise ValueError('invalid form')

            photo = Photo(color_tag = 'red')
            photo.image = form.cleaned_data['image']
            photo.save()

            return redirect('/')                                                   