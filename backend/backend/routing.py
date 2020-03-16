from django.urls import path  # new
from channels.auth import AuthMiddlewareStack  # new
from channels.routing import ProtocolTypeRouter, URLRouter  # changed
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

# changed
from events.consumers import EventConsumer
application = ProtocolTypeRouter({

    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    path('eventConsumer/', EventConsumer)
                ]
            )
        )
    )


    
})
