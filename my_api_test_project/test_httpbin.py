import requests
import pytest

# # 1. 测试一个最简单的公开接口
# response = requests.get("https://httpbin.org/get")
# print("状态码:", response.status_code)
# print("响应体:", response.text)
#
# # 2. 做一个简单的断言
# assert response.status_code == 200, f"请求失败，状态码：{response.status_code}"
# print("√ 基本接口测试通过！")

# def test_get_method():
#     """测试httpbin的get接口"""
#     response = requests.get("http://httpbin.org/get")
#     assert response.status_code == 200
#     #断言返回的url是请求的url
#     json_data = response.json()
#     #assert json_data['headers']['Content-Type'] == 'application/json'
#     #assert json_data['headers']['Accept'] == 'application/json'
#     assert json_data["url"] == "http://httpbin.org/get"
#
# if __name__ == '__main__':
#     # 这样可以直接用python运行，也可以用pytest运行
#     pytest.main([__file__])


def test_get_method(base_url):  # 注意！这里参数名base_url和fixture名字一样，pytest会自动注入
    """测试httpbin的get接口"""
    response = requests.get(f"{base_url}/get")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["url"] == f"{base_url}/get"

def test_post_method(base_url):
    """测试httpbin的post接口"""
    test_data = {"name": "你的名字", "salary": 18000}  # 对的，想着你的目标薪资！
    response = requests.post(f"{base_url}/post", json=test_data)
    assert response.status_code == 200
    json_data = response.json()
    # 断言我们发送的数据被正确返回了
    assert json_data["json"] == test_data