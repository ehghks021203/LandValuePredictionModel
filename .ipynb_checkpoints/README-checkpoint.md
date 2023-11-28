# **LandValuePredictionModel**
> 본 프로젝트는 2023년 2월부터 시작되어 진행 중인 프로젝트입니다.\
> **2023 빅콘테스트 공모전**에서는 "토지 가치 예측을 위한 AI 모델 개발" 주제로 참가하였습니다!

------

## **Overview**
이 프로젝트에서는 토지 가치를 추정하기 위한 예측 모델을 개발했으며, XGBoost 알고리즘을 사용했습니다.

### Key Steps:
**1. 데이터 수집 및 데이터셋 생성:**
- 국토교통부의 `토지매매신고조회서비스`, `토지특성정보`, `지가변동률`과 통계청 SGIS 오픈플랫폼의 `인구통계 데이터`, `사업체통계 데이터`를 사용했습니다.
- 아직 정확한 토지 가치 예측을 위한 특성이 부족하다고 판단되어 추후 보강할 예정입니다.

<br/>

**2. 데이터 분석:**
- 특성별 실거래가에 미치는 영향을 파악하기 위해 `matplot`과 `seaborn`을 활용해 특성간의 관계를 시각화하였습니다.
- 상관계수 분석 및 `box plot`을 통해 데이터간 연관성을 판단하였습니다.

<br/>

**3. 데이터 전처리:**
- 데이터를 모델에 입력하기 전에 철저한 전처리를 진행하였습니다.
- 결측값 처리, 이상치 제거 등의 작업을 진행하였으며, 범주형 변수에 대해 `One-Hot Encoding` 작업을 진행하였습니다.

<br/>

**4. XGBoost를 사용한 모델 훈련**
- 비선형 관계를 처리하고 데이터 내의 복잡한 패턴을 해석할 수 있는 `XGBoost` 모델을 선택하였습니다.
- 모델은 데이터 세트의 일부로 훈련되었습니다.

<br/>

**5. 평가 및 검증**
- 평가 지표로 `RMSE`를 사용하였고, 추가로 `에측오차(MAPE)`를 사용하였습니다.

<br/>

**6. 하이퍼파라미터 튜닝 (아직 진행 X)**
- 모델의 최적의 성능을 위해 하이퍼파라미터를 조정하였습니다.
- 조정에 사용된 알고리즘은 `GridSearchCV`, `RandomSearchCV`, `BayesSearchCV` 중에 하나를 사용했습니다.

<br/>

**7. 배포 및 통합**
- 모델을 웹 서비스나 애플리케이션으로 배포하였습니다. 
- [토지가격예측웹서비스](https://blue.kku.ac.kr)

<br/>

## **Project Organization**
```
├── data
│   └── seoul_data.csv  <= 서울 지역에 대한 데이터셋
├── model
├── notebooks
│   └── lvpm.ipynb      <= Jupyter notebooks. 데이터 전처리 및 시각화, 
│                          모델 학습 및 튜닝 작업을 진행하였습니다.
└── README.md
```

<br/>

## **TODO List**
- [ ] 소규모 데이터셋 업로드