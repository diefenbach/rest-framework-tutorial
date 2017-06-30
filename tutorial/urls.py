from django.conf.urls import url, include

API_PREFIX = r'^v1/'
api_urlpatterns = [
    url(API_PREFIX, include("snippets.urls")),
    url(API_PREFIX, include("authors.urls")),
]

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(api_urlpatterns)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
