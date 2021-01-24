# Django REST Framework + Vue.jsで求人情報アプリを構築しよう！

## Python・Django設定
### 1. 仮想環境作成

```
python -m venv django-rest
source django-rest/bin/activate
```

### 2. モジュールインストール

開発で必要なパッケージを記載します。
requirements.txt
```
Django==2.2.10
djangorestframework==3.11.0
```

モジュールインストール
```
pip install -r requirements.txt
```

### 3. job_boardプロジェクトを作成しjob_board/settings.pyの編集

```
django-admin startproject job_board
vim job_board/settings.py

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'
```

### 4. DBセットアップしサーバー起動

```
python manage.py migrate
python manage.py runserver
```

### 5. アプリケーション作成

```
python manage.py startapp jobs
```

### 6. スーパーユーザー作成


```
python manage.py createsuperuser
ユーザー名 (leave blank to use 'takahashifuyuki'): ftakahashi
メールアドレス: 
Password: 
Password (again): 
Superuser created successfully.
```

### 7. jobsアプリケーションを使用可能にするため、job_board/settings.pyの編集

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'jobs',
]
```

### 8. jobsアプリケーションのモデルを作成し、DBを再構築する。

```
class JobOffer(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField()
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    prefectures = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name
    
```

```
(django-rest) takahashifuyuki@FTakahashi-BizMac-mini django_rest_framework % python manage.py makemigrations
Migrations for 'jobs':
  jobs/migrations/0001_initial.py
    - Create model JobOffer

(django-rest) takahashifuyuki@FTakahashi-BizMac-mini django_rest_framework % python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, jobs, sessions
Running migrations:
  Applying jobs.0001_initial... OK

```

### 9. URL設定 

job_board/urls.py
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobs.api.urls')),
]
```

jobs/api/urls.py

```
from django.urls import path
from jobs.api import views

urlpatterns = [
    path('jobs/', views.ListView.as_view(), name='list'),
    path('jobs/<int:pk>/', views.DetailView.as_view(),name='detail'),
]
```

### 10.Serializer設定

Serializer：クエリセットやモデルインスタンスのような複雑なデータをJson形式のフォーマットに変換


http://127.0.0.1:8000/admin/


## Vue.js設定

'''
node -v
npm -v
'''

```
vue create frontend
```

```
cd frontend
npm install webpack-bundle-tracker@0.4.3
npm run serve
```


python manage.py runserver
pip install django-webpack-loader