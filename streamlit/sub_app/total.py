import streamlit as st
import requests
from PIL import Image
from twilio.rest import Client
import re

def send_twilio_message(message_body, to_phone_number):
    account_sid = 'AC31cd4ff285aa2abe7a96856c2812b252'
    auth_token = 'e8c357ab182216bb1452e1b56b4f0b39'
    twilio_client = Client(account_sid, auth_token)

    try:
        message = twilio_client.messages.create(
            from_='+17753414446',
            body=message_body,
            to=to_phone_number
        )
        st.success("메시지가 성공적으로 전송되었습니다. SID: {}".format(message.sid))
    except Exception as e:
        st.error("메시지 전송 중 오류가 발생했습니다: {}".format(str(e)))

# Twilio 메시지 전송 함수
def send_twilio_message(message_body, to_phone_number):
    account_sid = 'AC31cd4ff285aa2abe7a96856c2812b252'
    auth_token = 'e8c357ab182216bb1452e1b56b4f0b39'
    twilio_client = Client(account_sid, auth_token)

    try:
        message = twilio_client.messages.create(
            from_='+17753414446',
            body=message_body,
            to=to_phone_number
        )
        st.success("메시지가 성공적으로 전송되었습니다. SID: {}".format(message.sid))
    except Exception as e:
        st.error("메시지 전송 중 오류가 발생했습니다: {}".format(str(e)))

# 메인 페이지의 내용
def main():
    st.markdown("""
        <h1 style='text-align: center;'>개인정보 수집 · 활용 동의서</h1>
    """, unsafe_allow_html=True)

    image_url = "https://github.com/DongWonC/telecom_deploy/raw/main/Web/image/개인정보처리방침.png"
    response = requests.get(image_url)
    
    if response.status_code == 200:
        with open("temp_image.png", "wb") as f:
            f.write(response.content)

        image = Image.open("temp_image.png")
        st.image(image, caption="개인정보 수집 및 활용을 위한 동의서", use_column_width=True)
    else:
        st.error("이미지를 불러올 수 없습니다.")


    st.header("Twilio를 통한 메시지 발송 시 유의사항")
    st.markdown("""
        - 목적 제한: 개인정보는 명시된 목적 이외에 사용되지 않음.
        - 안전한 전송: Twilio를 통한 메시지 전송 시 암호화 및 보안 프로토콜 사용.
        - 동의 절차: 개인정보를 Twilio를 통해 처리 전, 사용자 동의 얻어야 함.
        - 접근 제어: Twilio 계정에 접근 권한을 제한하여 불법 접근 방지.
        - 보안 업데이트: Twilio 및 관련 서비스의 보안 업데이트 주기적으로 확인.
        
        ※ 해외 API를 사용하기 때문에 국외 발신으로 오는 것이 정상입니다. (스팸 아닙니다!)
    """)

    # 동의하기 버튼
    agreed = st.checkbox("개인정보 수집 및 활용에 동의합니다.")

    if agreed:
        # 전화번호 입력
        to_phone_number = st.text_input("수신자 전화번호", "+8210", help="예: +821012345678")

        # 전송 버튼
        if st.button("전송하기"):

            message_body = '''
    
(안내)[KT안내]서울 지역 65세 이상 고객 대상 디지털 기기 무료 교육 및 요금 할인, 새로운 가족 결합 안내 

1) 서울 지역 65세 이상 고객에게만 드리는 디지털 기기 무료 교육 이벤트♥
가까운 디지털 배움터, 대리점, 플라자, 체험형 플라자에 방문하셔서 이용해 보세요!

▶무료 교육에 대해 자세히 알아보기 : multitelecom.site:8501

서울 지역 디지털 기기 무료 교육
▶기간 : 2023.12.01.~2023.12.31.
▶대상 : 서울에 주소를 두고 있는 서울 특별 시민인 65세 이상 고객
▶장소 : 서울 전 지역의 디지털 배움터, 대리점, 플라자, 체험형 플라자
▶혜택 : 디지털 기기 무료 교육을 수료한 고객에게는 월 10% 요금 할인까지

2) 새로운 가족 결합 안내
인터넷 사용을 안 하신다고요? 5회선 이상 결합을 하고 싶으시다고요? 걱정마세요 저희 KT가 해드릴게요. 거기다 급하게 데이터가 필요한 고객님이라면 가족 간 데이터 공유도 가능합니다.

▶내용 : 인터넷 사용 안 하는 사람도 결합 가능, 회선 제한 X, 데이터 쉐어링 제한 없음

▶변경 전 : 5회선까지, 인터넷 + 모바일 결합 기준, 데이터 쉐어링 제한 있음

고객님을 위해 항상 최선을 다하는 KT가 되겠습니다.

감사합니다.

[마음을 담다 DIGICO KT]
        '''
            send_twilio_message(message_body, to_phone_number)

if __name__ == "__main__":
    main()
