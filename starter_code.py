import dashscope
from dashscope import Generation

dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'
dashscope.api_key = 'sk-8562322a046f4a0298e5cbff98f01598'

response = Generation.call(
    model='qwen-plus',
    prompt='Explain climate change in simple terms.'
)

print("🤖 Response:")
print(response.output.text)
