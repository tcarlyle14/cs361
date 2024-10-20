from django.shortcuts import render, get_object_or_404, redirect
from .models import Team, Player
from .forms import TeamForm, PlayerForm
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'nbaapp/team_list.html', {'teams': teams})
def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'nbaapp/team_detail.html', {'team': team})
def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'nbaapp/player_detail.html', {'player': player})
def home(request):
    return render(request, 'nbaapp/home.html')
def create_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm()
    return render(request, 'nbaapp/team_form.html', {'form': form})
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team_list')  # Redirect to a relevant page
    else:
        form = PlayerForm()
    return render(request, 'nbaapp/player_form.html', {'form': form})
def edit_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('team_list')
    else:
        form = TeamForm(instance=team)
    return render(request, 'nbaapp/team_form.html', {'form': form})
def delete_team(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('team_list')
    return render(request, 'nbaapp/confirm_delete.html', {'team': team})
def edit_player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('team_detail', team_id=player.team.id)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'nbaapp/player_form.html', {'form': form})
def delete_player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    team_id = player.team.id  # Capture the team ID to redirect after deletion
    if request.method == 'POST':
        player.delete()
        return redirect('team_detail', team_id=team_id)
    return render(request, 'nbaapp/confirm_delete_player.html', {'player': player})