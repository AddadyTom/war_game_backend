from config.environment_service import EnvironmentService
from config.general import PROD_ENV, TEST_ENV, DEV_ENV


class DefaultConfig:
    HOST, PORT = '0.0.0.0', 8000
    ELASTIC_HOST = '192.168.27.179'


class ProdConfig(DefaultConfig):
    pass


class TestConfig(DefaultConfig):
    pass


class DevConfig(DefaultConfig):
    pass


env_configs = {
    PROD_ENV: ProdConfig,
    TEST_ENV: TestConfig,
    DEV_ENV: DevConfig
}

CONFIG = env_configs[EnvironmentService.get_environment()]
