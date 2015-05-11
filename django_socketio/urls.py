from django.conf.urls import patterns, url


urlpatterns = patterns(
    "",
    url("^socket\.io", "socketio", name="socketio"),
)
