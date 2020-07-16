from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class Router(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'retrieve'},
            name='{basename}-retrieve',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]