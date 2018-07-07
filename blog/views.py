from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PhotoForm
from .models import Photo
import PIL
from PIL import Image
import cv2
import sklearn
from sklearn.cluster import KMeans
import numpy as np
import io
import os

def select_color_tag(color):
    r = int(color[0:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:6], 16)
    
    if g == b and r > g:
    	return 'red'
    elif r == g and r > b:
    	return 'yellow'
    elif r == b and g > r:
    	return 'green'
    elif g == b and g > r:
    	return 'blue'
    elif r == g and b > r:
    	return 'blue'
    elif r == b and b > g:
    	return 'red'
    elif r > g > b:
    	if g/r*16 > 0 and g/r*16 <= 4.5:
    		return 'red'
    	elif g/r*16 > 4.5 and g/r*16 < 12.5:
    		return 'orange'
    	else:
    		return 'yellow'
    elif g > r > b:
    	if r/g*16 > 12.5 and r/g*16 <= 16:
    		return 'yellow'
    	elif r/g*16 > 4.5 and r/g*16 <= 12.5:
    		return 'green'
    	else:
    		return 'green'
    elif g > b > r:
    	if b/g*16 > 0 and b/g*16 <= 4.5:
    		return 'green'
    	elif b/g*16 > 4.5 and b/g*16 <= 12.5:
    		return 'blue'
    	else:
    		return 'blue'
    elif b > g > r:
    	if g/b*16 > 12.5 and g/b*16 <= 16:
    		return 'blue'
    	elif g/b*16 > 4.5 and g/b*16 <= 12.5:
    		return 'blue'
    	else:
    		return 'blue'
    elif b > r > g:
    	if r/b*16 > 0 and r/b*16 <= 4.5:
    		return 'blue'
    	elif r/b*16 > 4.5 and r/b*16 <= 12.5:
    		return 'purple'
    	else:
    		return 'purple'
    else:
    	if b/r*16 > 12.5 and b/r*16 <= 16:
    		return 'red'
    	if b/r*16 > 4.5 and b/r*16 <= 12.5:
    		return 'purple'
    	else:
    		return 'red'

def post_list(req):
    if req.method == 'GET':
        return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.all(),
            'color': '#ff7f7f',
            'up': 'up_red',
        })

    elif req.method == 'POST':
        if 'red' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.filter(color_tag = 'red'),
            'color': '#ff7f7f',
            'up': 'up_red',
            })
        if 'ore' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.filter(color_tag = 'orange'),
            'color': '#ffbf7f',
            'up': 'up_ore',
            })
        if 'yel' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.filter(color_tag = 'yellow'),
            'color': '#ffff7f',
            'up': 'up_yel',
            })
        if 'gre' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.filter(color_tag = 'green'),
            'color': '#bfff7f',
            'up': 'up_gre',
            })
        if 'blu' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.filter(color_tag = 'blue'),
            'color': '#7fbfff',
            'up': 'up_blu',
            })
        if 'pur' in req.POST:
            return render(req, 'blog/post_list.html', {
            'form': PhotoForm(),
            'photos': Photo.objects.filter(color_tag = 'purple'),
            'color': '#bf7fff',
            'up': 'up_pur',
            })
        
        if 'upload' in req.POST:
            form = PhotoForm(req.POST, req.FILES)
            if not form.is_valid():
                raise ValueError('invalid form')
            cv2_img = cv2.imread(req.FILES['image'].temporary_file_path())
            cv2_img = cv2.resize(cv2_img, (150, 150))
            cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
            cv2_img = cv2_img.reshape((cv2_img.shape[0] * cv2_img.shape[1], 3))
            cluster = KMeans(n_clusters = 1)
            cluster.fit(X = cv2_img)

            cluster_centers_arr = cluster.cluster_centers_.astype(int, copy=False)

            bright_color = '%02x%02x%02x' % tuple(cluster_centers_arr[0])
            
            photo = Photo(color_tag = select_color_tag(bright_color))
            photo.image = form.cleaned_data['image']
            photo.save()

            return redirect('/')                                                   