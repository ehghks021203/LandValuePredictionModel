# **LandValuePredictionModel**
> 본 프로젝트는 2023년 2월부터 시작되어 진행 중인 프로젝트입니다.\
> **2023 빅콘테스트 공모전**에서는 "토지 가치 예측을 위한 AI 모델 개발" 주제로 참가하여 **수상**하였습니다!


_다른 언어로 읽기:_
_[English](README.md)_

------

## **배경**
현재 우리 사회에서는 부동산 시장이 빠르게 성장하고 변화하고 있으며, 이에 따른 토지 가치의 정확한 예측은 부동산 투자, 도시 계획, 자산 관리 등 다양한 분야에서 중요한 역할을 하고 있습니다.
부동산 시장은 투자 및 개발자, 정부 기관, 도시 계획자, 시민들에게 영향을 미치는 핵심적인 부분 중 하나로, 정확한 토지 가치 예측은 이들 모두에게 이익을 제공합니다.
<br/>
최근 인공지능 및 기계학습 기술의 발전은 대량의 데이터를 기반으로 한 토지 가치 예측의 정확도와 신뢰성을 향상시킬 수 있는 새로운 기회를 제공하고 있습니다. 
따라서 토지 가치 예측을 위한 AI 모델의 개발은 현실적이고 필수적인 과제가 되었습니다.

## **목적 및 필요성**
본 프로젝트의 주요 목적은 토지 가치 예측을 위한 AI 모델을 개발하고, 이 모델을 활용하여 부동산 시장의 미래 흐름을 예측하는 것입니다. 
이를 통해 다음과 같은 목표를 달성하고자 합니다.
- 부동산 투자자들에게 정확한 투자 의사 결정을 돕습니다.
- 도시 계획에 관련된 결정에 과학적 근거를 제공하여 도시의 지속 가능한 발전을 지원합니다.
- 부동산 시장의 투명성을 높여 시장 건전성을 유지합니다.

## **분석 수행 범위**
본 프로젝트에서 수행한 주요 작업은 다음과 같습니다.

### **데이터 수집 및 전처리**
토지 관련 데이터를 다양한 소스로부터 수집하였으며, 데이터 품질을 향상시키기 위한 전처리 작업을 수행하였습니다. 이 데이터는 국토교통부에서 제공하는 토지 특성 정보 및 토지 거래 기록, 인구 통계 데이터 등 다양한 출처에서 수집했습니다.

### **AI 모델 학습**
XGBoost를 사용하여 토지 가치 예측을 위한 AI 모델을 학습하였습니다. 이 모델은 다양한 변수를 고려하여 토지 가치를 예측하며, 모델의 학습과 테스트를 위해 큰 규모의 데이터셋을 활용했습니다.

### **모델 평가 및 성능 개선**
학습한 모델의 성능을 평가하고, 필요한 경우 모델의 성능을 개선하기 위한 실험을 수행하였습니다.
성능 평가는 평균 제곱근 오차(RMSE), 예측 오차(MAPE) 등을 기록하여 평가했습니다.

### **결과 해석 및 시각화**
모델의 결과를 해석하고, 시각화를 통해 이해하기 쉽게 전달할 수 있도록 하였습니다. 지도 시각화(예정) 및 그래프를 사용하여 토지 가치 예측 결과를 시각적으로 표현했습니다.

### **응용 및 확장**
학습한 AI 모델은 부동산 시장 예측, 도시 계획, 자산 관리 등 다양한 분야에 적용될 수 있도록 하였으며, 해당 데이터를 웹 페이지를 통해 쉽게 접근 가능하도록 구현했습니다. 이를 통해 미래의 토지 가치 예측에 대한 정확한 정보를 제공하고 지속 가능한 도시 발전을 지원할 수 있습니다.

<br/>

## **Key Steps:**
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

**4. XGBoost를 사용한 모델 훈련:**
- 비선형 관계를 처리하고 데이터 내의 복잡한 패턴을 해석할 수 있는 `XGBoost` 모델을 선택하였습니다.
- 모델은 데이터 세트의 일부로 훈련되었습니다.

<br/>

**5. 평가 및 검증:**
- 평가 지표로 `RMSE`를 사용하였고, 추가로 `에측오차(MAPE)`를 사용하였습니다.

<br/>

**6. 하이퍼파라미터 튜닝 (아직 진행 X):**
- 모델의 최적의 성능을 위해 하이퍼파라미터를 조정하였습니다.
- 조정에 사용된 알고리즘은 `GridSearchCV`, `RandomSearchCV`, `BayesSearchCV` 중에 하나를 사용했습니다.

<br/>

**7. 배포 및 통합:**
- 모델을 웹 서비스나 애플리케이션으로 배포하였습니다. 
- [토지가격예측웹서비스](https://blue.kku.ac.kr)

<br/>

## **Project Organization**
```
├── data
│   ├── seoul_data.csv  <= 서울 지역에 대한 데이터셋
│   ├── seoul_data_add_place_100.csv  <= 주변 상권 데이터를 포함한 100개 데이터
│   └── seoul_data_add_place_500.csv  <= 주변 상권 데이터를 포함한 500개 데이터
├── model
├── notebooks
│   └── lvpm.ipynb      <= Jupyter notebooks. 데이터 전처리 및 시각화, 
│                          모델 학습 및 튜닝 작업을 진행하였습니다.
├── src
│   └── data
│       └── make_dataset.py  <= 데이터셋 생성 파이썬 코드.
└── README.md
```

<br/>

## **TODO**
- XGBoost 모델과 LSTM 모델의 앙상블 학습
- 데이터셋의 이상치 선정 방식 고민