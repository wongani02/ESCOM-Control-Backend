from django.urls import path
from django.contrib import admin

from . import views 


urlpatterns = [
    path('substations/', views.SubstationsAPIView.as_view(), name='substations'),
    path('substation-single/<int:pk>/', views.SubstationsingleAPIView.as_view(), name='ss-single'),
    path('feeder-single/<int:pk>/', views.FeederSingleAPIView.as_view(), name='feeder-single'),
    path('loadshedding/', views.LoadSheddingAPIView.as_view(), name='loadshedding'),
    path('feeders/', views.FeedersAPIView.as_view(), name='feeders'),
    path('mimic-numbers/', views.MimicNumberListCreateAPIView.as_view(), name='mimic-numbers'),
    path('tx-records/', views.TXRecordSerializerListCreateView.as_view(), name='tx-records'),
]


admin.site.site_header = "SES Control Administration"
admin.site.site_title = "SES Control"
admin.site.index_title = "SES Control"




