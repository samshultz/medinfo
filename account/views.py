from collections import OrderedDict

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.views.generic import ListView
from django.views.generic.edit import FormView

from .fusioncharts import FusionCharts

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, MedicalInfoForm
from .models import Profile, MedicalInfo
from .utils import chart_config, map_data_to_dict

class UserRegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('user_detail')
    

    def form_valid(self, form):
        new_user = form.save()
        Profile.objects.create(user=new_user)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        
        return redirect("user_detail") 


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
                                                          'profile_form': profile_form,
                                                          'user_form': user_form})


def statistical_details(request):

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    allergiesChartConfig = chart_config("Users with and without Allergies")
    illnessChartConfig = chart_config("Users with and without Major illness")
    conditionChartConfig = chart_config("Users with different conditions", "Illness", "Number of users")
   

    allergies = {'with allergies': User.objects.filter(medical_info__allergies=True).count(),
                 'without allergies': User.objects.filter(medical_info__allergies=False).count()}
    
    major_illness = {'with major illness': User.objects.filter(medical_info__illness=True).count(),
                     'without major illness': User.objects.filter(medical_info__illness=False).count()}
    
    different_conditons = {'surgery': User.objects.filter(medical_info__surgery=True).count(),
                            'Blood Born Diseases':User.objects.filter(medical_info__blood_born_diseases=True).count(),
                            'Epilepsy': User.objects.filter(medical_info__epilepsy=True).count(),
                            'Pacemaker': User.objects.filter(medical_info__pacemaker=True).count(),
                            'Medication': User.objects.filter(medical_info__medication=True).count(),
                            'Liver Kidney Ailments': User.objects.filter(medical_info__liver_kidney_ailments=True).count(),
                            'Circulatory Problems': User.objects.filter(medical_info__circulatory_problems=True).count()}

    allergies_data = map_data_to_dict(allergies, allergiesChartConfig)
    major_illness_data = map_data_to_dict(major_illness, illnessChartConfig)
    different_conditons_data = map_data_to_dict(different_conditons, conditionChartConfig)
    
    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    allergies_chart = FusionCharts("doughnut2d", "ex1" , "100%", "400", "allergies", "json", allergies_data)
    major_illness_chart = FusionCharts("pie3d", "ex2" , "100%", "400", "illness", "json", major_illness_data)
    different_conditons_chart = FusionCharts("column2d", "ex3" , "800", "400", "different_conditions", "json", different_conditons_data)

    return  render(request, 
                   'account/users/statistical_details.html', 
                   {'allergies_chart' : allergies_chart.render(),
                    'major_illness_chart': major_illness_chart.render(),
                    'different_conditons_chart': different_conditons_chart.render(),
                    }
                  )