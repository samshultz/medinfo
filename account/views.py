from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.views.generic import ListView
from django.views.generic.edit import FormView

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, MedicalInfoForm
from .models import Profile, MedicalInfo


class UserRegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('account:user_detail')
    

    def form_valid(self, form):
        new_user = form.save()
        Profile.objects.create(user=new_user)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        
        return redirect("account:user_detail") 


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "account/users/user_list.html"
    # permission_required = 'account.can_vote'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset()
        user_type = self.request.GET.get('type')
        if user_type:
            if user_type == 'medication':
                queryset = queryset.filter(medical_info__medication=True)
            elif user_type == 'surgery':
                queryset = queryset.filter(medical_info__surgery=True)
            elif user_type == 'illness':
                queryset = queryset.filter(medical_info__illness=True)
            elif user_type == 'blood_born_diseases':
                queryset = queryset.filter(medical_info__blood_born_diseases=True)

        return queryset

@login_required
def user_detail_edit_view(request):
    med_form = None
    user_form = None
    profile_form = None
    med_info = MedicalInfo.objects.get(patient=request.user)
    user = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":
        med_form = MedicalInfoForm(instance=request.user.medical_info, data=request.POST)
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if med_form.is_valid() and user_form.is_valid() and profile_form.is_valid():
            med_form.save()
            user_form.save()
            profile_form.save()
    else:
        med_form = MedicalInfoForm(instance=request.user.medical_info)
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/users/display.html', {'med_form': med_form, 
                                                          'user':user,
                                                          'profile_form': profile_form,
                                                          'user_form': user_form})