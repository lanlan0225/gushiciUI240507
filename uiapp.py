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
    # 获取access_token
    access_token = get_access_token()

    # 在Streamlit中创建输入字段
    user_input = st.text_input("请输入你想问的问题：")

    
    st.write("回答：")
    st.write("深山破屋苔已凝")

    # # 如果用户输入了问题，则发送请求并显示回答
    # if user_input:
    #     # 发送请求
    #     response_data = make_request(access_token, user_input)

    #     # 提取并显示回答
    #     if "result" in response_data:
    #         st.write("回答：")
    #         st.write(response_data["result"])
    #     else:
    #         st.write("没有获取到回答。")


if __name__ == '__main__':
    # 运行Streamlit应用
    st.markdown(  
    f"""   
    <h1 style="text-align: center; font-size: 36px; font-weight: bold;">古诗词问答</h1>
    """,  
    unsafe_allow_html=True,  
    )  
    main()
