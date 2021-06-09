from django.apps import AppConfig


class GatewaysTutorialAppConfig(AppConfig):
    name = 'gateways_tutorial_app'
    label = name
    verbose_name = "Gateways Tutorial App"
    fa_icon_class = "fa-comment"
    url_home = "gateways_tutorial_app:hello_world"
