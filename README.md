# ⚽ Ankara Messi - FC Barcelona Goals Analysis🏟️

리오넬 메시의 FC 바르셀로나 시절 득점 데이터를 분석하고 시각화하는 FastAPI 기반 웹 애플리케이션입니다. 이 프로젝트는 메시의 득점 패턴, 득점 유형, 홈/원정 비율, 어시스트 분석 등을 시각적으로 보여줍니다.

---

![GIF](images/read.gif)

---

## 📋 주요 기능

1. **시즌별 득점 분석**:

   - 시즌별 득점 데이터를 막대 그래프로 시각화.

2. **연도별 득점 분석**:

   - 연도별 득점 데이터를 시각화하여 메시의 꾸준한 활약을 확인.

3. **월별 득점 패턴**:

   - 월별 득점 데이터를 통해 특정 시기에 득점이 집중되었는지 시각화.

4. **홈/원정 득점 비율**:

   - 홈 경기와 원정 경기에서의 득점 비율을 도넛 차트로 시각화.

5. **득점 유형 분석**:

   - 왼발, 오른발, 프리킥, 헤더, 페널티킥 등 다양한 득점 유형을 분석.

6. **어시스트 분석**:
   - 메시의 득점에 가장 많은 도움을 준 동료를 상위 10명으로 시각화.

---

## 👤 프로젝트 인원

- **개발자**: 1명
  - **역할**: 전체 프로젝트 설계, 개발, 테스트 및 배포.

---

## 🛠️ 기술 스택

- **Backend**: FastAPI
- **Frontend**: Jinja2 템플릿
- **Data Analysis**: Pandas, Plotly
- **Deployment**: Render
- **Visualization**: Plotly (Bar Chart, Pie Chart)

---

## 📂 프로젝트 구조

```
├── templates
│    └── index.html
│
├── Messi - All Goals for Barcelona.csv
├── messi_goal_fcb.py
├── README.md
├── requirements.txt
└── static
    ├── Debut.png
    ├── messi1.png
    ├── messi2.png
    ├── messi3.png
    ├── messi4.png
    ├── messi5.png
    ├── MSN.png
    └── 제목.png

```

---

## 📊 데이터 설명

- **파일명**: `Messi - All Goals for Barcelona.csv`
- **주요 컬럼**:
  - **Date**: 득점 날짜
  - **Season**: 시즌 정보
  - **Year**: 연도 정보
  - **Month**: 월 정보
  - **Venue**: Home/Away
  - **Type**: 득점 유형 (왼발, 프리킥, 헤더 등)
  - **Goal_assist**: 어시스트를 제공한 선수

---

## 📚 프로젝트에서 사용된 주요 기술

### 1. **FastAPI**

FastAPI는 Python 기반의 웹 프레임워크로, 빠르고 간단하며 효율적인 API를 개발할 수 있도록 설계되었습니다.  
이 프로젝트에서는 다음과 같은 역할로 사용되었습니다:

- **REST API 개발**: 클라이언트 요청을 처리하고 데이터를 반환하는 엔드포인트를 생성.
- **템플릿 렌더링**: Jinja2와 함께 HTML 페이지를 렌더링.
- **비동기 처리**: 비동기 함수(`async def`)를 사용하여 빠른 응답 속도를 제공.

#### FastAPI의 주요 장점:

- **빠른 개발**: 자동 문서화(Swagger UI, ReDoc) 제공.
- **비동기 지원**: 비동기 코드를 쉽게 작성 가능.

---

### 2. **Jinja2**

Jinja2는 Python 기반의 템플릿 엔진으로, HTML 파일에 동적으로 데이터를 삽입할 수 있습니다.  
이 프로젝트에서는 다음과 같은 역할로 사용되었습니다:

- **HTML 템플릿 렌더링**: FastAPI와 함께 데이터를 HTML 파일에 전달하여 동적인 웹 페이지 생성.
- **반복문과 조건문**: HTML에서 데이터를 반복 출력하거나 조건에 따라 다른 내용을 표시.
- **템플릿 상속**: 공통 레이아웃(헤더, 푸터 등)을 정의하고 재사용.

#### Jinja2의 주요 장점:

- **유연성**: HTML과 Python 데이터를 쉽게 결합.
- **템플릿 상속**: 코드 중복을 줄이고 유지보수를 용이하게 함.
- **사용법 간단**: Python 문법과 유사하여 배우기 쉬움.

---

### 3. **Plotly**

Plotly는 Python에서 데이터 시각화를 위한 라이브러리로, 대화형 그래프를 생성할 수 있습니다.  
이 프로젝트에서는 다음과 같은 역할로 사용되었습니다:

- **막대 그래프**: 시즌별, 연도별 득점 데이터를 시각화.
- **도넛 차트**: 홈/원정 득점 비율을 시각적으로 표현.
- **상호작용 지원**: 사용자가 그래프를 확대/축소하거나 세부 정보를 확인할 수 있도록 대화형 기능 제공.

#### Plotly의 주요 장점:

- **대화형 그래프**: 마우스 클릭, 확대/축소 등 상호작용 가능.
- **다양한 차트 지원**: 막대 그래프, 도넛 차트, 선 그래프 등.
- **웹 통합 용이**: HTML로 내보내기 쉬워 웹 애플리케이션에 적합.

---
