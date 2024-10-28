import streamlit as st

from utils import generate_xiaohongshu

st.header("爆款小红书写作助手 ✏️")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI API密钥：", type="password")
    openai_api_base = st.text_input("请输入OpenAI 地址（可选）", value="https://api.gptapi.us/v1")
    model_name = st.text_input("请输入模型版本（可选）", value="gpt-4o")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api_keys)")

theme = st.text_input("主题")
submit = st.button("开始写作")

if submit and not openai_api_key:
    st.info("请输入你的OpenAI API 密钥")
    st.stop()
if submit and not theme:
    st.info("请输入生成内容的主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_xiaohongshu(theme, openai_api_key, openai_api_base, model_name)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        for i in range(0, len(result.titles)):
            st.markdown(f"##### 小红书标题{i+1}")
            st.write(result.titles[i])
    with right_column:
        st.markdown("##### 小红书正文")
        st.write(result.content)

