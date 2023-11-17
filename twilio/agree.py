import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from message import show_message

def main():
    st.markdown("""
        <h1 style='text-align: center;'>개인정보 처리방침 동의서</h1>
    """, unsafe_allow_html=True)

    # 이미지 다운로드
    image_url = "https://github.com/HaJeong-K/Multi-Telecom/raw/main/twilio/개인정보처리방침.png"
    response = requests.get(image_url)
    
    if response.status_code == 200:
        with open("temp_image.png", "wb") as f:
            f.write(response.content)

        # 이미지 표시
        image = Image.open("temp_image.png")
        st.image(image, caption="이미지", use_column_width=True)
    else:
        st.error("이미지를 불러올 수 없습니다.")

    # 메시지 표시
    st.header("Twilio를 통한 메시지 발송 시 유의사항")
    st.markdown("""
        - 목적 제한: 개인정보는 명시된 목적 이외에 사용되지 않음.
        - 안전한 전송: Twilio를 통한 메시지 전송 시 암호화 및 보안 프로토콜 사용.
        - 동의 절차: 개인정보를 Twilio를 통해 처리 전, 사용자 동의 얻어야 함.
        - 접근 제어: Twilio 계정에 접근 권한을 제한하여 불법 접근 방지.
        - 보안 업데이트: Twilio 및 관련 서비스의 보안 업데이트 주기적으로 확인.
    """)

    # 동의 버튼
    if st.button("동의하기"):
        st.session_state.agreed = True
        st.success("동의가 완료되었습니다. 메세지 발송을 위해 아래를 확인해주세요.")
        show_message()

if __name__ == "__main__":
    main()
