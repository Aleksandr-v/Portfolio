
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.JobListView.as_view(), name='home'),
    path('create-job/', jobs.views.create_job, name='create_job'),
    path('blog/', include('blog.urls', namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
