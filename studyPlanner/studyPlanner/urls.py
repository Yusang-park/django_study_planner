"""studyPlanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diary/',include('diary.urls')),
    path('calender/', include('calender.urls')),
    path('',include('community.urls')),
    path('profileapp/',include('profileapp.urls')),
    path('favoriteapp/',include('favoriteapp.urls')),
    #allauth
    path('accounts/', include('allauth.urls')),
    
]


# 0. 앱 생성, install 설정
# 1. URL 설정, 모든 앱
# 2. view.py에 def 생성
# 3. 앱 폴더내에 tamplates 폴더 생성 -> html 파일 생성
# 4. setting.py에 static 설정하기
# 5. static/css폴더에 css 생성
# 6. css를 부르는 html에
#     {% load static %}
#     <link rel="stylesheet" type="text/css" href="{% static 'css/index.css' %}">

# 7. 새로운 html 생성해서 views 함수를 통해 연결하기

# 8. models.py에 class 생성
# 9. python manage.py makemigrates 입력하면 새로운 모델이 생성됨.
# 9-2. python manage.py migrate
# 10. main에 forms.py 생성하고 내부 작성
# 11. views에서 form 관련 함수 작성하기 (create) <-> html과 연결(create.html 확인)
