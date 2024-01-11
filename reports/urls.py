from django.urls import path
from . import views


urlpatterns = [
    path('base-report-list/', views.BaseReportListAPIView.as_view(), name='list-base-reports'),
    path('hv-report-list/', views.HVReportListAPIView.as_view(), name='hv-reports-list'),
    path('base-report-create/', views.BaseReportCreateAPIView.as_view(), name='base-report-create'),
    path('hv-report-create/', views.HVReportCreateAPIView.as_view(), name='hv-reports-create'),
    path('base-report-detail/<int:pk>/', views.BaseReportDetailView.as_view(), name='base-report-detail'),
    path('defect-list-create/', views.DefectListCreateAPIView.as_view(), name='defect-list-create'),
    path('forced-outages/', views.ForcedOutageListCreateView.as_view(), name='forced-outages'),
    path('planned-outages/', views.PlannedOutageListCreateAPIView.as_view(), name='planned-outages'),
]