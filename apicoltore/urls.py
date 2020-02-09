# urls.py
from django.urls import path
from apicoltore.views import ApicoltoreDetailView

urlpatterns = [
    path('<pk>/', ApicoltoreDetailView.as_view(), name='apicoltore'),
]
