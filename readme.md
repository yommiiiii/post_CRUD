# 📝 Flask 게시판 웹사이트

간단한 게시글 작성, 조회, 수정, 삭제가 가능한 웹 게시판입니다.  
Python + Flask + MySQL 기반으로 제작되었으며, ORM 없이 SQL 문법을 직접 사용합니다.

---

## 🔧 사용 기술

- **Backend**: Python, Flask
- **Database**: MySQL
- **Frontend**: HTML, CSS (with custom 디자인)
- **DB 연동**: `pymysql`
- **버전관리**: Git + GitHub

---

## 🚀 주요 기능

### ✅ 1. 게시글 CRUD 구현 (`app.py`)
- `/` : 게시글 목록 및 검색 (제목/내용/전체 기준)
- `/create` : 글 작성 (GET, POST)
- `/post/<id>` : 글 상세 보기
- `/update/<id>` : 글 수정 (GET, POST)
- `/delete/<id>` : 글 삭제

SQL 직접 작성으로 `INSERT`, `SELECT`, `UPDATE`, `DELETE` 동작 처리

---

### ✅ 2. 검색 기능
- 키워드 입력 + 검색 범위 선택 (제목/내용/전체)
- `LIKE` 쿼리를 사용하여 부분 검색
- 검색 후 검색어/카테고리 유지
- 전체 목록 보기 버튼으로 초기화 가능

---

### ✅ 3. 프론트엔드 스타일링 (`style.css`)
- 검색창: 둥근 카드 박스 형태 + 입력창/버튼 정리
- 버튼: 전부 밝은 회색 톤으로 통일 (hover 효과 포함)
- 게시글: 카드 스타일로 구분, 제목 강조
- 상세/작성/수정 페이지도 통일된 UI 적용

---

## 🗄 DB 테이블 구조

```sql
CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## 🛠 실행 방법

```bash
# 가상환경 추천
python -m venv venv
venv\Scripts\activate

# 패키지 설치
pip install flask pymysql

# 실행
python app.py
```
-> 브라우저에서 http://127.0.0.1:5000 접속

## 📌 기타
- pymysql로 SQL 직접 작성하여 ORM 미사용
- 사용자 경험을 위한 검색 유지, 디자인 통일, 확인창 등 적용