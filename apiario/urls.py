# urls.py
from django.urls import path
from apiario.views import ApiarioList, ApiarioDetail, ApiarioCreate, ApiarioUpdate, ApiarioDelete

urlpatterns = [
    path('', ApiarioList.as_view(), name='apiari'),
    path('crea/', ApiarioCreate.as_view(), name='apiari_create'),
    path('aggiorna/<int:pk>/', ApiarioUpdate.as_view(), name='apiari_update'),
    path('elimina/<int:pk>/', ApiarioDelete.as_view(), name='apiari_delete'),
    path('apicoltore/<int:pk>/', ApiarioDetail.as_view()),
]
