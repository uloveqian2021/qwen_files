import requests


def main():
    # 内网就可以调用，现在在A800上，后面迁移A10。
    url = 'http://10.10.181.10:51867/chat/zkpt_chat'

    # 这个不要变，是告诉服务器端这次请求是以json格式发送的。
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # 只需要给出最小部分就行了，其余参数在服务器端会根据每个任务动态配置。
    data = {
        "model": "Qwen-14B-Chat",
        "messages": [
            {
                "role": "user",
                "content": "你知道王东升是谁吗？"
            },
            {
                "role": "assistant",
                "content": "对不起，我不知道。"
            },
            {
                "content": "你知道王东升是谁吗？"
            },
            {
                "role": "assistant",
                "content": "对不起，我不知道。"
            },
            {
                "role": "user",
                "content": "你知道王东升是谁吗？"
            },
            {
                "role": "assistant",
                "content": "对不起，我不知道。"
            },
            {
                "role": "user",
                "content": "京东方今年的营收？"
            }
        ]
    }

    print(data['messages'])
    # 已优化，中间结果不返回。======zsl 1120
    res = requests.post(url, headers=headers, json=data, stream=True)  # 此处四个组建都不可以少，stream必须是True。
    for line in res.iter_content(None, decode_unicode=True):
        print(line, end="", flush=True)


if __name__ == '__main__':
    main()
