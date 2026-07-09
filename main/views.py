from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import ContactForm, SignUpForm

DEPARTMENTS = [
    {
        'code': 'TXT',
        'name': 'Textile Technology',
        'blurb': 'Rooted in Faisalabad\u2019s heritage as Pakistan\u2019s textile hub, covering spinning, weaving and processing.',
    },
    {
        'code': 'MEC',
        'name': 'Mechanical Technology',
        'blurb': 'Manufacturing, machine design and industrial maintenance for the region\u2019s factories.',
    },
    {
        'code': 'ELE',
        'name': 'Electrical Technology',
        'blurb': 'Power systems, electrical machines and industrial automation.',
    },
    {
        'code': 'CIV',
        'name': 'Civil Technology',
        'blurb': 'Structural, surveying and construction fundamentals for public infrastructure work.',
    },
    {
        'code': 'CIT',
        'name': 'Computer Technology',
        'blurb': 'Programming, networking and computer hardware maintenance for the digital economy.',
    },
    {
        'code': 'FDT',
        'name': 'Food Technology',
        'blurb': 'Food processing, preservation and quality control for the region\u2019s agro-based industry.',
    },
    {
        'code': 'AFM',
        'name': 'Auto & Farm Machinery Technology',
        'blurb': 'Automotive systems and agricultural machinery maintenance for a farming-heavy province.',
    },
    {
        'code': 'INS',
        'name': 'Instrumentation Technology',
        'blurb': 'Process control, measurement and calibration instruments used across modern plants.',
    },
]

STATS = [
    {'value': '1959', 'label': 'Established'},
    {'value': '8', 'label': 'Diploma programs'},
    {'value': '3,000+', 'label': 'Alumni in industry'},
    {'value': '40+', 'label': 'Faculty members'},
]


def home(request):
    context = {
        'departments': DEPARTMENTS,
        'stats': STATS,
    }
    return render(request, 'main/home.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your message has been logged. The relevant office will get back to you soon.'
            )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form': form})


class CollegeLoginView(LoginView):
    template_name = 'main/login.html'
    redirect_authenticated_user = True


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'main/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, f'Welcome, {self.object.first_name}! Your account has been created.')
        return response
