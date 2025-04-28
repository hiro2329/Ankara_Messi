# ⚽ Ankara Messi - FC Barcelona Goals Analysis🏟️

리오넬 메시의 FC 바르셀로나 시절 득점 데이터를 분석하고 시각화하는 FastAPI 기반 웹 애플리케이션입니다. 이 프로젝트는 메시의 득점 패턴, 득점 유형, 홈/원정 비율, 어시스트 분석 등을 시각적으로 보여줍니다.

---

### 홈 화면

![Home](images/header.png)

### 도입부

![Messi](images/legend.png)

### 시각화

![Visualization](images/visualization.png)

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
