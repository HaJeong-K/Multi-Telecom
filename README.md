# Multi-Telecom
고객 특성에 따른 이탈 및 요금 분석과 예측을 기반으로 한 통신사 해지율 개선 마케팅 서비스
<br>
<br>

## 프로젝트 설명
- 언어 : python, google colab, jupyter lab
- 개발 환경 : Google Cloud Project (GCP), Looker studio, BigQuery, Django
- 인원 : 5명 (팀장 : [shinyeop hwang](https://github.com/HSYhrae), 팀원 4명)
- 기간 : 2023.10.26 - 2023.12.05
- 주요내용
  + 통신사 고객 이탈에 대한 예측 및 요금에 따른 통신사의 매출 예측을 기반으로 함.
  + 최종적으로 이탈율이 높은 노령층을 타겟층으로 삼아 마케팅 서비스 제안을 목표로 함.
  + 대시보드의 경우 Looker studio를 기반으로 깔끔한 버전의 제작을 목표로 함.
  + ~~웹 배포의 경우 Django를 사용해서 Looker studio 대시보드와는 차별성을 두려함.~~
  +  Django의 해결법을 찾기 어려운 오류의 지속으로 진전이 없어 제작 툴을 Streamlit으로 변경함.(23.11.15)
 
- 역할
  + 팀원들이 희망하는 진로에 따라 역할을 분담함.
    + 데이터 분석 : [shinyeop hwang](https://github.com/HSYhrae), HaJeong-K(본인)
    + 대시보드 제작 및 마케팅 관련 : [Sohyeon Choi](https://github.com/Sohyeon-Choi), [Sumin Choi](https://github.com/sumin0308)
    + 웹 배포 : [Dongwon_Choi](https://github.com/DongWonC)
   
- 데이터
  + 데이터는 IBM 데이터 셋 [Telco Customer Churn](https://www.kaggle.com/datasets/sibelius5/telco-customer-churn?select=Telco_customer_churn_cleaned.csv) 을 사용함.
  + 국내, 해외 모두 통신사 관련 데이터는 존재하지 않아 가상의 데이터 셋을 사용함.
 
<br>

## 주제 변천사
### 선택한 대주제 : 통신사 고객 데이터 분석과 해지율 개선 및 마케팅 서비스
<br>

1. 통신사 데이터 셋을 IBM 데이터 셋으로 정함.
<br>

2. 1차 마케팅에 대한 방향성 토론.
   + B2B / B2C 방향성 토론 => B2C 선택
     + 기업간의 마케팅을 대상으로 하려면 추가적으로 데이터 셋을 구해야하는데 데이터를 구할 방법이 없음.
<br>

3. 2차 마케팅에 대한 방향성 토론.
   + 전반적인 마케팅 방안 보다 타겟층을 두고 마케팅을 하는 의견.
     + EDA를 기반으로 연령대로 분석한 부분에서 노령층의 이탈율이 높은 확실한 특징을 보이고 있어서 노령층을 타겟팅함.
    
<br>

## 목표

- 분석의 경우 예측을 중점으로 두고 2가지 예측을 진행함.
  + 고객 이탈에 대한 예측을 중심으로 하며, 추가적으로 고객 특성에 대한 요금을 기반으로 한 통신사 매출에 대한 예측을 진행함.
  + 고객 이탈 예측의 경우 다양한 머신러닝을 사용해서 비교하는 것을 목표로 함.
  + 통신사 매출에 대한 예측의 경우 폭넓은 머신러닝보단 평가지표가 높아지는 것을 목표로 함.
 <br>
 
- 대시보드
  + Looker studio를 사용해서 시각화 기반의 대시보드를 제작하는 것을 목표로 함.
  + 최대한 많은 내용을 담기 보다는 핵심만을 담아 깔끔하게 정리하는 것을 목표로 함.
 <br>
 
- 웹 배포
  + ~~Django를 기반으로 Looker studio 대시보드와는 다르게 원 데이터부터 예측된 데이터까지의 내용을 담아 마케팅에 대한 제안 및 최종 분석 결과 전달을 목표로 함.~~
  + Streamlit을 기반으로 Looker studio 대시보드와는 다르게 원 데이터부터 예측된 데이터까지의 내용을 담아 마케팅에 대한 제안 및 최종 분석 결과 전달을 목표로 함.
  + 분석의 내용을 중점으로 배포하기보단, 분석의 내용을 기반으로 제안되는 마케팅 서비스에 대해 배포함.
 
<br>

## 개발 로그 기록
- 레포 생성일자를 기준으로 작성됨.(23.10.31)
<br>

[2023.10.31]
- 오늘 한 일
  + 데이터 분석 : 데이터 전처리, EDA, 머신러닝 관련 코드 작업 + 빅쿼리 추가 연동.
  + 대시보드 : Looker studio 제작을 위한 심화 공부. (및 추가 마케터 프로젝트로 광고 제작 진행.)
  + 웹 배포 : Django 관련 틀 제작.
 
- 오늘 못한 일
  + 데이터 분석 : 데이터 EDA 마무리.
  + 기획 발표 준비 : ppt 1차 정리.
 
- 내일 할 일
  + 데이터 분석 : 데이터 EDA 마무리 및 머신러닝 1차 구체화.
  + 대시보드 : Looker studio 제작을 위한 심화 공부 및 제작 준비.
  + 웹 배포 : Django 관련 틀 제작.
  + 기획 발표 준비 : ppt 1차 정리.
 <br>
 
[2023.11.01]
- 오늘 한 일
  + 데이터 분석 : 통신사 데이터 전처리 및 EDA 완료.
  + 대시보드 : 마케팅 관련 자료 수집. (및 추가 마케터 프로젝트로 광고 노출수 증가를 위한 공부.)
  + 웹 배포 : Django 복습.
  + 기획 발표 준비 : ppt 1차 정리.
 
- 오늘 못한 일
  + 데이터 분석 : 고객 이탈 머신러닝 코드 초안 작성.
  + 대시보드 : Looker studio 제작을 위한 심화 공부.
  + 웹 배포 : 대시보드 UI 구상.
  + 기획 발표 준비 : ppt 1차 마무리.
 
- 내일 할 일
  + 데이터 분석 : 노령층 데이터로만 추가 EDA 수행, 고객 이탈 머신러닝 코드 초안 작성.
  + 대시보드 : Looker studio 제작을 위한 심화 공부 및 제작 준비.
  + 웹 배포 : Django 복습 및 대시보드 UI 구상.
  + 기획 발표 준비 : ppt 2차 정리.
<br>
 
[2023.11.02]
- 오늘 한 일
  + 데이터 분석 : 노령층 데이터 한정 추가 EDA 및 마케팅용 지도 시각화, 머신러닝 코드 초안 작성.
  + 대시보드 : side project 문제 원인 및 해결방안 마련.
  + 웹 배포 : Django 복습.
  + 기획 발표 준비 : ppt 마무리.
 
- 오늘 못한 일
  + 데이터 분석 : Cauasallmpact 라이브러리 리뷰 및 통신사 대리점 정보 크롤링.
  + 대시보드 : Looker studio 제작을 위한 심화 공부.
  + 웹 배포 : 대시보드 UI 구상.
 
- 내일 할 일
  + 데이터 분석 : Cauasallmpact 라이브러리 리뷰 및 머신러닝 모델 학습 및 평가 수행, 통신사 대리점 지도시각화까지 마무리.
  + 대시보드 : Looker studio 제작을 위한 심화 공부 및 제작 준비. (및 추가 마케터 프로젝트로 광고 노출 확인.)
  + 웹 배포 : Django 복습 및 대시보드 UI 구상.

- Trouble-shooting
  + 디지털 배움터 크롤링을 하면서 제대로 알지 못해 오류가 생겼음.
    + 해결방법을 찾아 해결했고, 블로그에 상세히 작성함. (https://forky-develop.tistory.com/entry/selenium-crawling)
<br>
 
[2023.11.03]
- 오늘 한 일
  + 데이터 분석 : 고령 인구 데이터 전처리 및 EDA 완성 및 크롤링 틀 제작.
  + 대시보드 : 프로젝트 마케팅 기획.
  + 웹 배포 : Django 복습.
 
- 오늘 못한 일
  + 데이터 분석 : Cauasallmpact 라이브러리 리뷰 및 고객 이탈 머신러닝 모델 평가, 크롤링 미완.
  + 대시보드 : Looker studio 제작을 위한 심화 공부.
  + 웹 배포 : 대시보드 UI 구상.
 
- 월요일 할 일
  + 데이터 분석 : 주제 선정 배경 구체화, Cauasallmpact 라이브러리 리뷰 및 머신러닝 모델 학습 및 평가 수행, 통신사 대리점 지도시각화까지 마무리.
  + 대시보드 : Looker studio 제작을 위한 심화 공부 및 제작 준비. (및 side project 구글 애즈 변경 확인.)
  + 웹 배포 : Django 복습 및 대시보드 UI 구상.
<br>
 
[2023.11.06]
- 오늘 한 일
  + 데이터 분석 : 머신러닝 모델별 평가코드 초안 작성, SHAP 라이브러리 활용 변수 중요도 확인, 통신사 2사 크롤링 완료.
  + 대시보드 : Looker studio 제작을 위한 심화 공부.
  + 웹 배포 : 기본 구상.
 
- 오늘 못한 일
  + 데이터 분석 : 주제 선정 배경 구체화, 통신사(한군데) 대리점 정보 크롤링.
  + 대시보드 : Looker studio 공부 중 이해 못한부분 다시 짚기.
  + 웹 배포 : 대시보드 UI 심화 구상.
 
- 내일 할 일
  + 데이터 분석 : 변수 중요도를 기반으로 모델 재평가, 주제 선정 배경 구체화, 통신사 대리점 지도시각화까지 마무리.
  + 대시보드 : 마케팅 방향 확정 후 홍보용 포스터 제작 및 안내문자 구상.
  + 웹 배포 : 대시보드 UI 구상.

- Trouble-shooting
  + 통신사 대리점 크롤링을 하면서 방향을 잡지 못해 오류가 생겼음.
    + 해결방법을 찾아 해결했고, 블로그에 상세히 작성함. (https://forky-develop.tistory.com/entry/selenium-crawling-Deep-version)
<br>
 
[2023.11.07]
- 오늘 한 일
  + 데이터 분석 : 머신러닝 모델별 평가코드 확인, SHAP 라이브러리 과적합 확인, 통신사 대리점 크롤링 및 지도시각화 완료.
  + 대시보드 : 마케팅 기획 구체화, 포스터 제작 및 문자 문안 샘플 제작, Looker studio 공부.
  + 웹 배포 : UI 기본 구상.
 
- 오늘 못한 일
  + 데이터 분석 : 주제 선정 배경 구체화, 머신러닝 과적합 문제 해결.
  + 대시보드 : Looker studio 공부 마무리.
  + 웹 배포 : 대시보드 UI 심화 구상.
 
- 내일 할 일
  + 데이터 분석 : 주제 선정 배경 구체화, 머신러닝 과적합 문제 해결(컬럼을 선정하거나, 여러개로 나눠서 혼합으로 사용해도 되는지 확인).
  + 대시보드 : Looker studio 공부 마무리 및 대시보드 및 시각화 구상.
  + 웹 배포 : 대시보드 UI 구상.
<br>
 
[2023.11.08]
- 오늘 한 일
  + 데이터 분석 : 주제 선정 배경 수집, 머신러닝 pipeline 알아보기, CLV(고객 수명 가치) 분석에 대한 예측 틀 생성.
  + 대시보드 : Looker studio 공부.
  + 웹 배포 : UI 기본 구상.
 
- 오늘 못한 일
  + 데이터 분석 : 머신러닝 pipeline 활용.
  + 대시보드 : Looker studio 공부 마무리.
  + 웹 배포 : 대시보드 UI 심화 구상.
 
- 내일 할 일
  + 데이터 분석 : 머신러닝 pipeline 활용, CLV 예측 마무리 및 매출 예측 틀 생성.
  + 대시보드 : Looker studio 공부 마무리 및 대시보드 및 시각화 구상.
  + 웹 배포 : 대시보드 UI 구상.
  + 멘토링 : 멘토링 때 팀 질문사항 수집 및 마케팅관련 검토할 부분 체크, 대시보드 초안 마무리
<br>
 
[2023.11.09]
- 오늘 한 일
  + 데이터 분석 : 모든 부분의 머신러닝 코드 초안 구현.
  + 대시보드 : Looker studio 공부.
  + 웹 배포 : UI 기본 구상 및 깃액션 확인.
 
- 오늘 못한 일
  + 데이터 분석 : CLV 머신러닝 마무리.
  + 대시보드 : Looker studio 대시보드 구상.
  + 웹 배포 : 웹 내용 추가.
 
- 내일 할 일
  + 데이터 분석 : 전반적으로 머신러닝 마무리하기.
  + 대시보드 : Looker studio 대시보드 및 시각화 초안 구상.
  + 웹 배포 : 웹 내용 추가.
<br>
 
[2023.11.10]
- 오늘 한 일
  + 데이터 분석 : 모든 부분의 머신러닝 코드 완료.
  + 대시보드 : Looker studio 대시보드 기획 및 초안 제작.
  + 웹 배포 : 웹 내용 추가.
 
- 오늘 못한 일
  + 데이터 분석 : CLV 머신러닝 활용관련 고민중.
  + 대시보드 : Looker studio 대시보드 전체 구상.
  + 웹 배포 : 웹 내용 추가.
 
- 내일 할 일
  + 데이터 분석 : CLV 머신러닝 활용 확정짓기, 통계분석 진행.
  + 대시보드 : Looker studio 대시보드 구현에 사용할 데이터셋 체크.
  + 웹 배포 : 웹 내용 추가 및 깃액션 활용하기.
<br>
 
[2023.11.11]
- 오늘 한 일
  + 전반적인 프로젝트 진행 방향에 대한 멘토링.
<br>

[2023.11.13]
- 오늘 한 일
  + 데이터 분석 : 머신러닝 추가 확인, 군집분석 진행.
  + 대시보드 : 구글 스프레드 시트 공부(Looker studio 대시보드 보완용).
  + 웹 배포 : Github Actions 연동.
 
- 오늘 못한 일
  + 데이터 분석 : 군집분석 결과 활용방법 모색.
  + 대시보드 : 구글 스프레드 시트 공부.
  + 웹 배포 : 분석 기반 내용 추가.
 
- 내일 할 일
  + 데이터 분석 : 머신러닝 보강 및 마무리, 요인분석 진행.
  + 대시보드 : 구글 스프레드 시트 공부.
  + 웹 배포 : 분석 기반 내용 추가.

- Trouble-shooting
  + 전체 컬럼에 대해 군집분석을 시행하는데 군집 평가가 좋지 않았음.
    + 나이대에 대한 군집분석을 세부적으로 시행했고, 이와 관련한 내용을 블로그에 상세히 작성함. (https://forky-develop.tistory.com/entry/final-project-cluster-analysis)
<br>

[2023.11.14]
- 오늘 한 일
  + 데이터 분석 : 머신러닝 케이스별 앙상블 틀 생성, 군집분석 결과 활용방법 체크, 요인분석 진행.
  + 대시보드 : Looker studio 막대차트 수정.
  + 웹 배포 : 팝업창 생성.
  + PPT : 전반적인 틀 확정, 프로젝트 개요부분 마무리.
 
- 오늘 못한 일
  + 데이터 분석 : 머신러닝 케이스별 앙상블 마무리.
  + 대시보드 : Looker studio 스타일 적용.
  + 웹 배포 : 분석 기반 내용 추가.
 
- 내일 할 일
  + Python : 머신러닝 케이스별 앙상블 마무리, 매출 예측 관련 보강.
  + 대시보드 : Looker studio 스타일 적용.
  + 웹 배포 : 분석 기반 내용 추가.
  + PPT : 1차 제작 마무리.
<br>

[2023.11.15]
- 오늘 한 일
  + 데이터 분석 : 머신러닝 케이스별 앙상블 진행.
  + 대시보드 : Looker studio 대시보드 작업.
  + 웹 배포 : Streamlit 제작 공부.
  + PPT : 전체적인 틀 확정, 프로젝트 개요부분 마무리.
 
- 오늘 못한 일
  + 데이터 분석 : 머신러닝 케이스별 앙상블 마무리.
  + 웹 배포 : Streamlit 제작 틀 생성.
 
- 내일 할 일
  + 데이터 분석 : 머신러닝 케이스별 앙상블 마무리.
  + 대시보드 : Looker studio 대시보드 내용 추가.
  + 웹 배포 : Streamlit 제작 틀 생성.
  + PPT : 컨펌 전 ppt 마무리(이탈 예측, 데이터 정의서 제외).
<br>

[2023.11.16]
- 오늘 한 일
  + 데이터 분석 : 머신러닝 케이스별 앙상블 진행.
  + 대시보드 : 구글 스프레드 시트 학습, 마케팅 방안 최종 기획 및 이메일 발송할 내용 작성.
  + Streamlit : Streamlit과 GCP, Bigquery, Github 연동.
  + PPT : 전체적인 틀 확정, 프로젝트 개요부분 마무리.
 
- 오늘 못한 일
  + 대시보드 : 마케팅 기대효과 기획.
  + Streamlit : Streamlit 구성 추가.
 
- 내일 할 일
  + 데이터 분석 : 이탈 예측 머신러닝 모델별 하이퍼파라미터 튜닝 적용.
  + 대시보드 : 마케팅 기대효과 기획.
  + Streamlit : Streamlit 구성 추가, 로컬환경에서 Twilio를 이용한 문자 발송 구현해보기.
  + PPT : 컨펌 전 ppt 마무리(EDA ~ 이탈 예측, 한계점 페이지 마무리).
<br>

[2023.11.16]
- 오늘 한 일
  + 데이터 분석 : 이탈 예측 머신러닝 모델별 하이퍼파라미터 튜닝 적용.
  + 대시보드 : 루커 스튜디오 대시보드 수정, 구글 스프레드 시트 공부.
  + Streamlit : sidebar, 메뉴 탭 개발, 문자메세지 전송 페이지.
  + PPT : 이탈 예측, 기대효과, 한계점 부분 추가.
 
- 오늘 못한 일
  + 데이터 분석 : 이탈 예측 머신러닝 통합 모델 생성.
  + 대시보드 : 마케팅 기대효과 기획.
  + Streamlit : 지도 시각화 부분 탭 생성 및 추가, 문자메세지 전송버튼 구현.
 
- 월요일 할 일
  + 데이터 분석 : 이탈 예측 머신러닝 모델별 마무리 확인.
  + 대시보드 : 마케팅 기대효과 기획.
  + Streamlit : 지도 시각화 부분 탭 생성 및 추가, 문자메세지 전송버튼 마지막으로 확인.
  + PPT : 이번주에 수정/추가 못한 부분 마무리.

- Trouble-shooting
  + 문자메세지 전송버튼의 기능이 제대로 구현되지 않음.
    + 해당 부분에 대한 해결이 되지 않았으나, 한계점과 함께 진행한 내용을 작성함. (https://forky-develop.tistory.com/entry/twilio-with-python-streamlit)
