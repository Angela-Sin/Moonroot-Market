from django.shortcuts import render, redirect, get_object_or_404
from .models import Profiles
from django.contrib.auth.decorators import login_required
from .forms import ProfileEditForm

@login_required
def profile_detail(request):
    """Display the user's profile."""
    profile = get_object_or_404(Profiles, user=request.user)
    return render(request, 'userprofile/profile_detail.html', {'profiles': profile})

@login_required
def profile_edit(request):
    """Edit the user's profile."""
    profile = get_object_or_404(Profiles, user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'userprofile/profile_edit.html', {'form': form})
