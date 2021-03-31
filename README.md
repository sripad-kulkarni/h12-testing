# H12 

**This is an app in Python-Django** to Implement an H12 error on Heroku and resolving with an application level timeout.

Heroku app name: `h12-testing-hyd`
App URL: `h12-testing-hyd.herokuapp.com`

Paths available on the app:

- https://h12-testing-hyd.herokuapp.com/         -----------> This path should throw an H12 error if removed the timeout.
- https://h12-testing-hyd.herokuapp.com/office/
- https://h12-testing-hyd.herokuapp.com/school/

Currently the app has a timeout of 10 seconds set in the `Procfile`-
```
web: gunicorn h12testing.wsgi --timeout 10
```
*You can remove `--timeout 10` to see the Heroku router throw H12 on the path `https:\\<app-name>.herokuapp.com\`.*

**How did we implement the H12?**

We added a small line of code that delays the response for more than 30 seconds- time.sleep(`<time-in-seconds>`). You can check this out in the file `testing/views.py`.
```
def home(request):
    time.sleep(40)
    return render(request, 'home.html')
```

Paths on the app are defined in the file `h12testing/urls.py`:
```
    path('admin/', admin.site.urls),                    ----------->  Default path (We do not work with this here).
    path('', views.home),                               ----------->  https://h12-testing-hyd.herokuapp.com/
    path('office/', views.office),                      ----------->  https://h12-testing-hyd.herokuapp.com/office/
    path('school/', views.school),                      ----------->  https://h12-testing-hyd.herokuapp.com/school/
```
As you can see here, the path `https://h12-testing-hyd.herokuapp.com/` points to a function `home` inside the `views` (`views.py`). Similarly, other two paths point to functions `office` and `school` in `views.py`.



Feel free to clone this repo and implement it yourself!
