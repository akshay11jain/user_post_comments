from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users',views.UserView)
router.register('post',views.PostView)
router.register('comments',views.CommentsView)


urlpatterns = [

        path('',include(router.urls)),
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]