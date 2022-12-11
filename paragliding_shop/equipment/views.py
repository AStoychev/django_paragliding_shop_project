from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from paragliding_shop.accounts.models import AppUser
from paragliding_shop.equipment.forms import CreateWingForm, EditWingForm, DeleteWingForm, \
    CreateHarnessesForm, EditHarnessesForm, DeleteHarnessForm, CreateReservesForm, EditReservesForm, \
    CreateInstrumentsForm, EditInstrumentsForm, CreateHelmetsForm, EditHelmetsForm, DeleteInstrumentsForm, \
    DeleteReservesForm, DeleteHelmetsForm
from paragliding_shop.equipment.models import Wings, Harness, Reserves, Instruments, Helmets

UserModel = get_user_model()


def get_profile():
    profiles = AppUser.objects.all()
    if profiles:
        return profiles[0]
    return None


def wings(request):
    profile = request.user
    context = {
        'wings': Wings.objects.all(),
        'profile': profile,
    }

    return render(request, 'equipments/wings.html', context)


def wing_add(request):

    if request.method == "POST":
        form = CreateWingForm(request.POST)
        if form.is_valid():
            wing = form.save(commit=False)
            wing.user = request.user
            wing.save()
            return redirect('index')
    else:
        form = CreateWingForm()

    context = {
        'form': form,
    }

    return render(request, 'equipments/equipment_create/wing_add.html', context)


def wing_details(request, pk):
    current_wing = Wings.objects.filter(pk=pk).get()
    owner = request.user.id == current_wing.user_id
    equipment_owner = UserModel
    profile = request.user
    context = {
        'owner': owner,
        'profile': profile,
        'current_wing': current_wing,
        'equipment_owner': equipment_owner,
    }

    return render(request, 'equipments/equipment_details/wing_details.html', context)


def wing_edit(request, pk):
    wing = Wings.objects.get(pk=pk)
    current_wing = Wings.objects.filter(pk=pk).get()
    owner = request.user.id == current_wing.user_id
    profile = request.user

    if request.method == "POST":
        form = EditWingForm(request.POST, instance=wing)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditWingForm(instance=wing)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'wing': wing,
    }
    return render(request, 'equipments/equipment_edit/wing_edit.html', context)


def wing_delete(request, pk):
    wing = Wings.objects.get(pk=pk)
    current_wing = Wings.objects.filter(pk=pk).get()
    owner = request.user.id == current_wing.user_id
    profile = request.user
    if request.method == "POST":
        form = DeleteWingForm(request.POST, instance=wing)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteWingForm(instance=wing)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'wing': wing,
    }
    return render(request, 'equipments/equipment_delete/wind_delete.html', context)


def harnesses(request):
    profile = request.user
    context = {
        'harnesses': Harness.objects.all(),
        'profile': profile,
    }

    return render(request, 'equipments/harness.html', context)


def harnesses_add(request):
    profile = request.user

    if request.method == "POST":
        form = CreateHarnessesForm(request.POST)
        if form.is_valid():
            harness = form.save(commit=False)
            harness.user = request.user
            harness.save()
            return redirect('index')
    else:
        form = CreateHarnessesForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'equipments/equipment_create/harnesses_add.html', context)


def harnesses_details(request, pk):
    current_harness = Harness.objects.filter(pk=pk).get()
    owner = request.user.id == current_harness.user_id
    profile = request.user

    context = {
        'owner': owner,
        'profile': profile,
        'current_harness': current_harness,

    }

    return render(request, 'equipments/equipment_details/harness_details.html', context)


def harnesses_edit(request, pk):
    harness = Harness.objects.get(pk=pk)
    current_harness = Harness.objects.filter(pk=pk).get()
    owner = request.user.id == current_harness.user_id
    profile = request.user
    if request.method == "POST":
        form = EditHarnessesForm(request.POST, instance=harness)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditHarnessesForm(instance=harness)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'harness': harness,
    }
    return render(request, 'equipments/equipment_edit/harnesses_edit.html', context)


def harnesses_delete(request, pk):
    harness = Harness.objects.get(pk=pk)
    current_harness = Harness.objects.filter(pk=pk).get()
    owner = request.user.id == current_harness.user_id
    profile = request.user
    if request.method == "POST":
        form = DeleteHarnessForm(request.POST, instance=harness)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteHarnessForm(instance=harness)

    context = {
        'form': form,
        'harness': harness,
        'owner': owner,
        'profile': profile,
    }
    return render(request, 'equipments/equipment_delete/harness_delete.html', context)


def reserves(request):
    profile = request.user
    context = {
        'reserves': Reserves.objects.all(),
        'profile': profile,
    }

    return render(request, 'equipments/reserves.html', context)


def reserves_add(request):
    profile = request.user

    if request.method == "POST":
        form = CreateReservesForm(request.POST)
        if form.is_valid():
            reserve = form.save(commit=False)
            reserve.user = request.user
            reserve.save()
            return redirect('index')
    else:
        form = CreateReservesForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'equipments/equipment_create/reserves_add.html', context)


def reserves_details(request, pk):
    current_reserves = Reserves.objects.filter(pk=pk).get()
    owner = request.user.id == current_reserves.user_id
    profile = request.user

    context = {
        'owner': owner,
        'profile': profile,
        'current_reserves': current_reserves,
    }

    return render(request, 'equipments/equipment_details/reserves_details.html', context)


def reserves_edit(request, pk):
    current_reserves = Reserves.objects.get(pk=pk)
    reserve = Reserves.objects.filter(pk=pk).get()
    owner = request.user.id == reserve.user_id
    profile = request.user
    if request.method == "POST":
        form = EditReservesForm(request.POST, instance=current_reserves)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditReservesForm(instance=current_reserves)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'current_reserves': current_reserves,
    }
    return render(request, 'equipments/equipment_edit/reserves_edit.html', context)


def reserves_delete(request, pk):
    current_reserves = Reserves.objects.get(pk=pk)
    reserve = Reserves.objects.filter(pk=pk).get()
    owner = request.user.id == reserve.user_id
    profile = request.user
    if request.method == "POST":
        form = DeleteReservesForm(request.POST, instance=current_reserves)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteReservesForm(instance=current_reserves)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'current_reserves': current_reserves,
    }
    return render(request, 'equipments/equipment_delete/reserves_delete.html', context)


def instruments(request):
    profile = request.user
    context = {
        'instruments': Instruments.objects.all(),
        'profile': profile,
    }

    return render(request, 'equipments/instruments.html', context)


def instruments_add(request):
    profile = request.user

    if request.method == "POST":
        form = CreateInstrumentsForm(request.POST)
        if form.is_valid():
            instrument = form.save(commit=False)
            instrument.user = request.user
            instrument.save()
            return redirect('index')
    else:
        form = CreateInstrumentsForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'equipments/equipment_create/instruments_add.html', context)


def instruments_details(request, pk):
    current_instruments = Instruments.objects.filter(pk=pk).get()
    owner = request.user.id == current_instruments.user_id
    profile = request.user

    context = {
        'owner': owner,
        'profile': profile,
        'current_instruments': current_instruments,
    }

    return render(request, 'equipments/equipment_details/instruments_details.html', context)


def instruments_edit(request, pk):
    current_instruments = Instruments.objects.get(pk=pk)
    instrument = Instruments.objects.filter(pk=pk).get()
    owner = request.user.id == instrument.user_id
    profile = request.user
    if request.method == "POST":
        form = EditInstrumentsForm(request.POST, instance=current_instruments)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditInstrumentsForm(instance=current_instruments)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'current_instruments': current_instruments,
    }
    return render(request, 'equipments/equipment_edit/instruments_edit.html', context)


def instruments_delete(request, pk):
    current_instruments = Instruments.objects.get(pk=pk)
    instrument = Instruments.objects.filter(pk=pk).get()
    owner = request.user.id == instrument.user_id
    profile = request.user
    if request.method == "POST":
        form = DeleteInstrumentsForm(request.POST, instance=current_instruments)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteInstrumentsForm(instance=current_instruments)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'current_instruments': current_instruments,
    }
    return render(request, 'equipments/equipment_delete/instruments_delete.html', context)


def helmets(request):
    profile = request.user
    context = {
        'helmets': Helmets.objects.all(),
        'profile': profile,
    }

    return render(request, 'equipments/helmets.html', context)


def helmets_add(request):
    profile = request.user

    if request.method == "POST":
        form = CreateHelmetsForm(request.POST)
        if form.is_valid():
            helmet = form.save(commit=False)
            helmet.user = request.user
            helmet.save()
            return redirect('index')
    else:
        form = CreateHelmetsForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'equipments/equipment_create/helmets_add.html', context)


def helmets_details(request, pk):
    current_helmets = Helmets.objects.filter(pk=pk).get()
    owner = request.user.id == current_helmets.user_id
    profile = request.user

    context = {
        'owner': owner,
        'profile': profile,
        'current_helmets': current_helmets,
    }

    return render(request, 'equipments/equipment_details/helmets_details.html', context)


def helmets_edit(request, pk):
    current_helmets = Helmets.objects.get(pk=pk)
    helmet = Helmets.objects.filter(pk=pk).get()
    owner = request.user.id == helmet.user_id
    profile = request.user
    if request.method == "POST":
        form = EditHelmetsForm(request.POST, instance=current_helmets)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditHelmetsForm(instance=current_helmets)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'current_helmets': current_helmets,
    }
    return render(request, 'equipments/equipment_edit/helmets_edit.html', context)


def helmets_delete(request, pk):
    current_helmets = Helmets.objects.get(pk=pk)
    helmet = Helmets.objects.filter(pk=pk).get()
    owner = request.user.id == helmet.user_id
    profile = request.user
    if request.method == "POST":
        form = DeleteHelmetsForm(request.POST, instance=current_helmets)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteHelmetsForm(instance=current_helmets)

    context = {
        'owner': owner,
        'profile': profile,
        'form': form,
        'current_helmets': current_helmets,
    }
    return render(request, 'equipments/equipment_delete/helmets_delete.html', context)
