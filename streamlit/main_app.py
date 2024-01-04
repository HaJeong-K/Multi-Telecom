# -*- coding:utf-8 -*-
import os
import requests
import streamlit as st
from PIL import Image
from io import BytesIO

from sub_app import home_app, digital, KT, total

# 이미지를 가져오는 함수
def fetch_image(url):
    response = requests.get(url)

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))
    else:
        st.error(f"Unable to load the image from {url}. Status code: {response.status_code}")
        return None

# main 함수
def main():
    with st.sidebar:
        # GitHub에서 이미지 가져오기
        sidebar_image_url = "https://raw.githubusercontent.com/DongWonC/telecom_deploy/main/Web/image/title.png"
        sidebar_image = fetch_image(sidebar_image_url)

        if sidebar_image:
            st.image(sidebar_image, use_column_width=True)

        menu = ['홈', 'KT 대리점 찾기', '디지털 배움터 찾기', '서비스 문자 발송', '서비스 제공자']
        choice = st.sidebar.selectbox("Menu", menu)

    if choice == '홈':
        home_app.main()

    elif choice == 'KT 대리점 찾기':
        KT.main()

    elif choice == '디지털 배움터 찾기':
        digital.main()

    elif choice == '서비스 문자 발송':
        total.main()

    elif choice == '서비스 제공자':
        provider_image_url = "https://raw.githubusercontent.com/DongWonC/telecom_deploy/main/Web/image/procider.png"
        provider_image = fetch_image(provider_image_url)

        if provider_image:
            st.image(provider_image, caption="서비스 제공자 이미지", use_column_width=True)

if __name__ == "__main__":
    main()
