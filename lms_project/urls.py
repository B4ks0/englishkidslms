from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import custom_404, custom_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('homework/', include('homework.urls')),
    # Test URL untuk halaman 404 custom
    path('test-404/', custom_404, name='test_404'),
]

# Custom error handlers
handler404 = 'lms_project.views.custom_404'
handler500 = 'lms_project.views.custom_500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
