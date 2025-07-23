from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, CustomPasswordChangeForm, UserRegisterForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def lobby(request):
    return render(request, 'home.html') 

@login_required
def home(request):
    show_login_toast = request.session.get('show_login_toast', False)
    show_approved_toast = request.session.get('show_approved_toast', False)
    if request.user.is_authenticated:
        response = render(request, 'welcome.html', {'user': request.user, 'show_login_toast': show_login_toast, 'show_approved_toast': show_approved_toast})
    else:
        response = render(request, 'welcome.html', {'show_login_toast': show_login_toast, 'show_approved_toast': show_approved_toast})
    # Hapus flag setelah render
    request.session.pop('show_login_toast', None)
    request.session.pop('show_approved_toast', None)
    return response

@login_required
def dashboard_redirect(request):
    role = getattr(request.user, 'role', None)

    if role == 'teacher':
        return redirect('teacher_dashboard')
    elif role == 'student':
        return redirect('student_dashboard')
    else:
        return HttpResponse("Akun ini belum punya role yang benar.")  # type: ignore

@login_required
def course_redirect(request):
    return redirect('course_list')  

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # ganti nama url sesuai punya kamu
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'users/profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # supaya user tidak logout
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'users/change_password.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_approved = False  # default
            user.role = 'student'     # Set role to student otomatis
            user.save()
            return render(request, 'users/register_success.html')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_approved:
                messages.error(request, "Akun ini belum di-ACC admin. Silakan hubungi admin/guru.")
                return render(request, 'registration/login.html', {'form': form})
            # Cek jika user baru saja di-ACC (login pertama setelah di-ACC)
            if user.is_approved and user.approved_at and (user.last_login is None or user.last_login < user.approved_at):
                request.session['show_approved_toast'] = True
            login(request, user)
            request.session['show_login_toast'] = True
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

class CustomLoginView(LoginView):
    def form_valid(self, form):
        user = form.get_user()
        if not getattr(user, 'is_approved', True):
            messages.error(self.request, "Akun masih belum di acc oleh admin.")
            auth_logout(self.request)
            return redirect('login')
        self.request.session['show_login_toast'] = True
        return super().form_valid(form)