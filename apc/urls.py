from django.conf.urls import include,url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users',views.UserView)
router.register('post',views.PostView)
router.register('comments',views.CommentsView)


urlpatterns = [

        url('',include(router.urls)),
        url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]