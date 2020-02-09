# urls.py
from django.urls import path
from arnia.views import ArniaList, ArniaDetail, ArniaCreate, ArniaUpdate, ArniaDelete

urlpatterns = [
    path('', ArniaList.as_view(), name='arnie'),
    path('crea/', ArniaCreate.as_view(), name='arnia_create'),
    path('aggiorna/<int:pk>/', ArniaUpdate.as_view(), name='arnia_update'),
    path('elimina/<int:pk>/', ArniaDelete.as_view(), name='arnia_delete'),
]
