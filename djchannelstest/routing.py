from channels.routing import route
channel_routing = [
    route("http.request", "channelsapp.consumers.http_consumer"),
]