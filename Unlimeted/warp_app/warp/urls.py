from django.urls import path
from .views import WarpView

urlpatterns = [
    path('warp/', WarpView.as_view(), name='warp'),
]
