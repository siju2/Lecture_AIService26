import streamlit as st

# 1. 제목 설정
st.title("사용자 입력 폼 🔗")

# 폼을 사용하여 입력창들을 그룹화합니다.
with st.form("my_form"):
    # 2. 이름 입력 (Text Input)
    name = st.text_input("이름", value="이혜정")
    
    # 3. 나이 입력 (Number Input / 이미지와 유사하게 +/- 버튼이 포함됨)
    age = st.number_input("나이", min_value=0, max_value=120, value=24)
    
    # 4. 약관 동의 (Checkbox)
    agree = st.checkbox("약관에 동의합니다", value=True)
    
    # 5. 제출 버튼
    submitted = st.form_submit_button("제출")

# 6. 제출 후 결과 출력 부분
if submitted:
    # 텍스트 출력
    st.write(f"이름: {name}, 나이: {age}")
    
    # 약관 동의 시 성공 메시지 박스 (초록색 배경)
    if agree:
        st.success("약관에 동의했습니다.")
    else:
        st.warning("약관에 동의하지 않았습니다.")