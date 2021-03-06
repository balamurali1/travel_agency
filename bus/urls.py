from django.views.generic.base import TemplateView

from bus.models import Bus
from bus.models import Car
from bus.models import Passenger
from bus.models import Trip

from django.urls import path
from bus.views import bus_create,bus_update,bus_delete,car_create,car_update,car_delete,passenger_create,passenger_update,passenger_delete,trip_create,trip_update,trip_delete

urlpatterns = [
    path('',TemplateView.as_view(template_name="bus/home.html",
      extra_context={"data":Bus.objects.all()}
      )),
    path("create/",bus_create),
    path("update/<int:pk>/",bus_update),
    #path("delete/<int:pk>/",bus_delete),

    path("delete/<int:pk>/",bus_delete),



    # path('car1/',home1),
    path('car1/',TemplateView.as_view(template_name="bus/home1.html",
      extra_context={"data":Car.objects.all()}
      )),

    path("car_create/",car_create),
    path("car_update/<int:pk>/",car_update),
    path("car_delete/<int:pk>/",car_delete),

   
   #path('passenger1/',home2),
   path('passenger1/',TemplateView.as_view(template_name="bus/home2.html",
     extra_context={"data":Passenger.objects.all()}
    )),
   
   path("passenger_create/",passenger_create),
   path("passenger_update/<int:pk>/",passenger_update),
   path("passenger_delete/<int:pk>/",passenger_delete),



   #path('trip1/',home3),
   path('trip1/',TemplateView.as_view(template_name="bus/home3.html",
    extra_context={"data":Trip.objects.all()}
    )),

   path("trip_create/",trip_create),
   path("trip_update/<int:pk>/",trip_update),
   path("trip_delete/<int:pk>/",trip_delete),




]
