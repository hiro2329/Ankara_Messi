from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pandas as pd
import plotly.graph_objects as go
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CSV 데이터 읽기
df = pd.read_csv('Messi - All Goals for Barcelona.csv')


# 템플릿 렌더링 엔드포인트
@app.get("/", response_class=HTMLResponse)
async def render_graph(request: Request):
    # 데이터 처리
    assist_counts = df['Goal_assist'].value_counts().head(10)
    assist_counts = assist_counts.sort_values(ascending=True)

    # Plotly 그래프 생성
    fig = go.Figure(
        data=[
            go.Bar(
                x=assist_counts.values,  # 어시스트 횟수
                y=assist_counts.index,   # 어시스트 이름
                orientation="h",         # 수평 막대 그래프
                marker=dict(color="skyblue"),
            )
        ]
    )
    fig.update_layout(
        title="Top 10 Assists for Messi Goals",
        xaxis_title="Number of Goals",
        yaxis_title="Assisted by",
        margin=dict(l=150, r=50, t=50, b=50),
    )

    # 그래프를 HTML로 변환
    assist_html = fig.to_html(full_html=False)

    # 데이터 처리: Venue(H or A) 비율
    venue_counts = df['Venue'].value_counts()

    # Plotly 그래프 생성: Venue 비율
    fig_venue = go.Figure(
        data=[
            go.Pie(
                labels=venue_counts.index,  # H, A
                values=venue_counts.values,  # 각 비율
                hole=0.3,  # 도넛 차트
            )
        ]
    )
    fig_venue.update_layout(
        title="Home/Away 득점 비율",
    )
    home_away_html = fig_venue.to_html(full_html=False)

    # 데이터 처리: goalType 비율
    goalType_counts = df['Type'].value_counts()
    goalType_total = goalType_counts.sum()  # 골 타입의 총합 계산

    # Plotly 그래프 생성: Venue 비율
    fig_goalType = go.Figure(
        data=[
            go.Pie(
                labels=goalType_counts.index,  # goalType
                values=goalType_counts.values,  # 각 비율
                hole=0.5,  # 도넛 차트
            )
        ]
    )
    fig_goalType.update_layout(
        title="득점타입 비율",
        annotations=[
            dict(
                text=f"Total<br>{goalType_total}",  # 가운데 표시할 텍스트
                x=0.5,  # 도넛 차트의 중앙 (x축)
                y=0.5,  # 도넛 차트의 중앙 (y축)
                font=dict(size=15, color="black"),  # 텍스트 스타일
                showarrow=False,  # 화살표 숨김
            )
        ],
    )
    goalType_html = fig_goalType.to_html(full_html=False)

    # 데이터 처리: 시즌별 득점
    season_counts = df['Season'].value_counts().sort_index()

    # Plotly 그래프 생성: 시즌별 득점
    fig_season = go.Figure(
        data=[
            go.Bar(
                x=season_counts.index,  # 시즌
                y=season_counts.values,  # 득점 수
                marker=dict(color="orange"),
            )
        ]
    )
    fig_season.update_layout(
        title="Goals by Season",
        xaxis_title="Season",
        yaxis_title="Number of Goals",
        margin=dict(l=50, r=50, t=50, b=50),
    )
    season_html = fig_season.to_html(full_html=False)

    # 데이터 처리: 년도별 득점
    year_counts = df['Year'].value_counts().sort_index()

    # Plotly 그래프 생성: 년도별 득점
    fig_year = go.Figure(
        data=[
            go.Bar(
                x=year_counts.index,  # 년도
                y=year_counts.values,  # 득점 수
                marker=dict(color="blue"),
            )
        ]
    )
    fig_year.update_layout(
        title="Goals by Year",
        xaxis_title="Year",
        yaxis_title="Number of Goals",
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis=dict(
            tickmode="linear",  # x축 레이블을 모든 값에 대해 표시
            dtick=1,            # x축 레이블 간격을 1로 설정
        ),
    )
    year_html = fig_year.to_html(full_html=False)

   # 데이터 처리: 월별 득점
    df['Month'] = pd.to_datetime(df['Date']).dt.month  # Date 열에서 월 추출
    month_counts = df['Month'].value_counts().sort_index()

    # Plotly 그래프 생성: 월별 득점
    fig_month = go.Figure(
        data=[
            go.Bar(
                x=month_counts.index,  # 월 (1~12)
                y=month_counts.values,  # 득점 수
                marker=dict(color="green"),
            )
        ]
    )
    fig_month.update_layout(
        title="Goals by Month",
        xaxis_title="Month",
        yaxis_title="Number of Goals",
        margin=dict(l=50, r=50, t=50, b=50),
        xaxis=dict(
            tickmode="linear",  # x축 레이블을 모든 값에 대해 표시
            dtick=1,            # x축 레이블 간격을 1로 설정
        ),
    )
    month_html = fig_month.to_html(full_html=False)

    # 템플릿에 그래프 HTML 전달
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "assist_html": assist_html,
            "home_away_html": home_away_html,
            "goalType_html": goalType_html,
            "season_html": season_html,
            "year_html": year_html,
            "month_html": month_html,
        },
    )

# 스토리라인 및 그래프 순서
# 1. 도입: 메시의 득점 여정
# 그래프: season_html (시즌별 득점)
# 설명: 메시의 바르셀로나 시절은 시즌마다 새로운 기록을 세운 여정이었습니다. 시즌별 득점 그래프를 통해 그의 성장과 전성기를 확인할 수 있습니다.
# 2. 연도별 득점 분석
# 그래프: year_html (년도별 득점)
# 설명: 시즌별 득점에서 더 세부적으로 들어가, 연도별 득점 그래프를 통해 메시가 특정 연도에 얼마나 꾸준히 활약했는지 살펴봅니다.
# 3. 월별 득점 패턴
# 그래프: month_html (월별 득점)
# 설명: 메시의 득점은 특정 월에 집중되었을까요? 월별 득점 그래프를 통해 그의 득점 패턴을 확인합니다.
# 4. 홈과 원정에서의 활약
# 그래프: home_away_html (홈/원정 득점 비율)
# 설명: 메시의 득점은 홈 경기와 원정 경기에서 어떻게 나뉘었을까요? 홈과 원정 득점 비율을 통해 그의 경기력을 비교합니다.
# 5. 득점 유형 분석
# 그래프: goalType_html (득점 유형 비율)
# 설명: 메시의 득점은 어떤 방식으로 이루어졌을까요? 프리킥, 헤더, 페널티킥 등 다양한 득점 유형을 분석합니다.
# 6. 어시스트와의 관계
# 그래프: assist_html (어시스트 상위 10명)
# 설명: 메시의 득점은 혼자만의 힘으로 이루어진 것이 아닙니다. 그의 득점에 가장 많은 도움을 준 동료들을 확인합니다.
# http://127.0.0.1:8000/
