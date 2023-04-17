from django.shortcuts import render, get_object_or_404, redirect
from .models import DiaryEntry
from .forms import DiaryEntryForm
from django.contrib.auth.decorators import login_required

@login_required
def entry_list(request):
    entries = DiaryEntry.objects.all()
    return render(request, 'entry_list.html', {'entries': entries})

@login_required
def entry_detail(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)
    return render(request, 'entry_detail.html', {'entry': entry})

@login_required
def entry_create(request):
    form = DiaryEntryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('entry_list')
    return render(request, 'entry_form.html', {'form': form})

def entry_update(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)
    form = DiaryEntryForm(request.POST or None, instance=entry)
    if form.is_valid():
        form.save()
        return redirect('entry_detail', entry_id=entry_id)
    return render(request, 'entry_form.html', {'form': form})

def entry_delete(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry_list')
    return render(request, 'entry_confirm_delete.html', {'entry': entry})
