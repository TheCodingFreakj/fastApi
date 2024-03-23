from django.apps import AppConfig
from shopify_auth.exceptions import get_env_value
# https://github.com/Shopify/shopify_django_app/blob/master/shopify_app/middleware.py

class ShopifyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = get_env_value('APP_ONE')
    # Replace the API Key and Shared Secret with the one given for your
    # App by Shopify.
    #
    # To create an application, or find the API Key and Secret, visit:
    # - for private Apps:
    #     https://${YOUR_SHOP_NAME}.myshopify.com/admin/api
    # - for partner Apps:
    #     https://www.shopify.com/services/partners/api_clients
    #
    # You can ignore this file in git using the following command:
    #   git update-index --assume-unchanged shopify_settings.py
    SHOPIFY_API_KEY = get_env_value('SHOPIFY_API_KEY')
    SHOPIFY_API_SECRET = get_env_value('SHOPIFY_APP_API_SECRET')
    print(SHOPIFY_API_SECRET)

    # API_VERSION specifies which api version that the app will communicate with
    SHOPIFY_API_VERSION = get_env_value('SHOPIFY_API_VERSION')

    # See http://api.shopify.com/authentication.html for available scopes
    # to determine the permisssions your app will need.
    SHOPIFY_API_SCOPE = get_env_value('SHOPIFY_API_SCOPE')