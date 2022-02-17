from symphony.bdk.core.extension import retry_aware, register_extension


@register_extension
@retry_aware  # so that _retry_config attribute is set and @retry decorator can be used with the same retry config
class MyDefaultExtension:
    def __init__(self):
        self._bot_session = None
        self._config = None
        self._api_client_factory = None

    def set_auth_session(self, auth_session):
        print("Registering auth session")
        self._bot_session = auth_session

    def set_configuration(self, bdk_config):
        print("Registering config: " + bdk_config.host)
        self._config = bdk_config

    def set_api_client_factory(self, api_client_factory):
        print("Registering api client factory: " + str(api_client_factory))
        self._api_client_factory = api_client_factory

    def get_service(self):
        return self

    async def get_session_token(self):
        return await self._bot_session.session_token
