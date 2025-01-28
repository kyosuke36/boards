from django.urls import path
from . import views

app_name = "money"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("delete/<int:money_id>", views.delete, name="delete"),
    path("result/<int:money_id>/", views.result, name="result"),
    # path("result/<int:money_id>/create", views.create_result, name="create_result"),
]