import requests
import json
import streamlit as st


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=uQ97TaTUkSZJwc6jKKIpd35V&client_secret=ur5lIdl0DG0abMuAX4e7OdpVXEUNyFjJ"

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def make_request(access_token, user_input):
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token={access_token}"
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()


def main():

    # 标题
    st.title("古诗词问答大模型")

    # 初始化会话状态，会话状态中没有"messages"键，则添加一个初始的消息列表，其中包含一条来自助手的消息
    if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "你想要了解古诗词的什么问题？"}]

    # 显示之前的消息
    for msg in st.session_state.messages:  
    st.chat_message(msg["role"]).write(msg["content"])

    # 处理用户输入
    if prompt := st.chat_input():
        
        # 发送请求，获取access_token
        access_token = get_access_token()
        # 调用百度API并获取响应
        response_data = make_request(access_token, user_input)
        
        # 提取响应  
        msg_content = response_data["result"]  
      
        # 将用户的输入和机器人的回复添加到消息列表中，并显示  
        st.session_state.messages.append({"role": "user", "content": prompt})  
        st.chat_message("user").write(prompt)  
        st.session_state.messages.append({"role": "assistant", "content": msg_content})  
        st.chat_message("assistant").write(msg_content)


if __name__ == '__main__':
    # 运行Streamlit应用
    main()
