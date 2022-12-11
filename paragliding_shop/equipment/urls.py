from django.urls import path

from paragliding_shop.equipment.views import wings, harnesses, reserves, instruments, helmets, wing_details, \
    harnesses_details, reserves_details, wing_add, wing_edit, wing_delete, harnesses_add, harnesses_edit, \
    harnesses_delete, reserves_add, reserves_edit, reserves_delete, instruments_add, instruments_details, \
    instruments_edit, instruments_delete, helmets_add, helmets_details, helmets_edit, helmets_delete

urlpatterns = (
    path('wings/', wings, name='wings'),
    path('wings_add/', wing_add, name='wings add'),
    path('wing_details/<int:pk>', wing_details, name='wing details'),
    path('wing_edit/<int:pk>', wing_edit, name='wing edit'),
    path('wing_delete/<int:pk>', wing_delete, name='wing delete'),

    path('harnesses/', harnesses, name='harnesses'),
    path('harnesses_add/', harnesses_add, name='harnesses add'),
    path('harnesses_details/<int:pk>', harnesses_details, name='harnesses details'),
    path('harnesses_edit/<int:pk>', harnesses_edit, name='harnesses edit'),
    path('harnesses_delete/<int:pk>', harnesses_delete, name='harnesses delete'),

    path('reserves/', reserves, name='reserves'),
    path('reserves_add/', reserves_add, name='reserves add'),
    path('reserves_details/<int:pk>', reserves_details, name='reserves details'),
    path('reserves_edit/<int:pk>', reserves_edit, name='reserves edit'),
    path('reserves_delete/<int:pk>', reserves_delete, name='reserves delete'),

    path('instruments/', instruments, name='instruments'),
    path('instruments_add/', instruments_add, name='instruments add'),
    path('instruments_details/<int:pk>', instruments_details, name='instruments details'),
    path('instruments_edit/<int:pk>', instruments_edit, name='instruments edit'),
    path('instruments_delete/<int:pk>', instruments_delete, name='instruments delete'),

    path('helmets/', helmets, name='helmets'),
    path('helmets_add/', helmets_add, name='helmets add'),
    path('helmets_details/<int:pk>', helmets_details, name='helmets details'),
    path('helmets_edit/<int:pk>', helmets_edit, name='helmets edit'),
    path('helmets_delete/<int:pk>', helmets_delete, name='helmets delete'),
)
