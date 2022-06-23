from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('cat/',views.cat,name='cat'),
    path('categ/<str:cat>',views.categ,name='categ'),
    path('contact/',views.contact,name='contact'),
    path('single/<int:code>',views.single,name='single'),
    path('login/',views.login, name='login'),
    path ('showall/',views.showall,name='showall'),
    path("delete/<int:obj>",views.delete,name='delete'),
    path("edit/<int:id>",views.edit,name='edit'),
    path('createpost/',views.createPost,name='createPost')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)