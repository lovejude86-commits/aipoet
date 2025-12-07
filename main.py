# main.py
import streamlit as st
from langchain_openai import ChatOpenAI

# Streamlit Secrets에서 자동으로 OPENAI_API_KEY를 읽어옵니다.
# Secrets 설정 예시:
# OPENAI_API_KEY = "교수님이 공지한 키"

st.title("AI Poet ✨")
st.write("주제를 입력하면 AI가 시를 지어드립니다.")

# 언어 모델 설정
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.9  # 시 생성이므로 창의성을 조금 높임
)

# 사용자 입력
subject = st.text_input("시의 주제를 입력하세요:")

# 버튼 클릭 시 시 생성
if st.button("시 작성"):
    if not subject.strip():
        st.warning("먼저 시의 주제를 입력해주세요!")
    else:
        with st.spinner("AI 시인이 시를 쓰고 있습니다... ✍️"):
            prompt = f"""
            '{subject}'을(를) 주제로 감성적인 한국어 자유시를 4연으로 작성해줘.
            너무 딱딱하지 않게, 문학적 표현을 사용해서 아름답게 써줘.
            """
            result = llm.invoke(prompt)
            st.markdown("---")
            st.subheader("AI Poet 작품")
            st.write(result.content)
