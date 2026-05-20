import pytest
import yaml
import os

# 读取yaml配置
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

# 定义一个pytest fixture，供所有测试用例使用
@pytest.fixture(scope="session")
def base_url():
    config = load_config()
    return config["base_url"]