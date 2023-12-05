import streamlit as st
import requests
from PIL import Image
from io import BytesIO

def main():
    # 페이지의 제목
    st.markdown(
        f"<h1 style='text-align: center;'>디지털 기기 무료 교육</h1>",
        unsafe_allow_html=True
    )

    # 두 개의 열 생성
    col1, col2 = st.columns(2)

    # 첫 번째 열
    image_url = "https://raw.githubusercontent.com/DongWonC/telecom_deploy/main/Web/image/kt_poster.png"
    response = requests.get(image_url)

    if response.status_code == 200:
        # 이미지를 열기
        marketing_image = Image.open(BytesIO(response.content))

        # 첫 번째 열에 이미지 추가
        col1.image(marketing_image, caption="디지털 기기 무료 교육", use_column_width=True)
    else:
        # 이미지를 불러오지 못한 경우 에러 메시지 출력
        col1.error("이미지를 불러올 수 없습니다.")

    # 두 번째 열에 텍스트 추가
    col2.write('''
    서울 지역 65세 이상 고객에게만 드리는 디지털 기기 무료 교육 이벤트♥
    
    가까운 디지털 배움터, 대리점, 플라자, 체험형 플라자에 방문하여서 이용해 보세요!

    서울 지역 디지털 기기 무료 교육
    
    ▶기간 : 2023.12.01.~2023.12.31.
    
    ▶대상 : 서울에 주소를 두고 있는 서울 특별 시민인 65세 이상 고객
    
    ▶장소 : 서울 전 지역의 디지털 배움터, 대리점, 플라자, 체험형 플라자
    
    ▶혜택 : 디지털 기기 무료 교육을 수료한 고객에게는 월 10% 요금 할인까지
    ''')

    # 다른 컨텐츠를 추가하려면 계속해서 st 함수들을 사용하세요.

if __name__ == "__main__":
    main()