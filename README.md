# Happy Health Care Program

간단한 설명

Happy Health Care Program는 개인/소규모 기관의 건강 관리 보조를 목표로 하는 파이썬 기반 프로젝트입니다. 이 저장소는 간단한 스크립트와 DB 초기화 스크립트, 도커 설정을 포함하며 로컬 환경에서 빠르게 테스트하고 확장할 수 있도록 되어 있습니다.

주요 목적
- 건강 관련 데이터(예: 체중, 혈압 등) 간단 저장 및 조회
- 로컬/경량 DB 초기화 스크립트를 통해 빠른 시작 제공
- 필요 시 도커 컴포즈로 서비스 실행 지원

주요 파일
- `health_manager.py` : 메인 실행 스크립트(데이터 입출력 및 관리 로직)
- `init_health.sql` : 데이터베이스 초기화 스크립트
- `docker-compose.yaml` : (선택) 관련 서비스(예: DB)를 도커로 띄우기 위한 설정
- `requirements.txt` : 파이썬 의존성 목록
- `setup.py` : 패키지 메타데이터 및 설치 설정
- `Makefile` : 자주 쓰는 명령(예: 테스트, 빌드)이 정의되어 있을 수 있음

설치 및 실행 (로컬)
1. 가상환경 생성 및 활성화

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. DB 초기화 (예: SQLite 또는 다른 DB를 사용하는 경우)

```bash
# 예: sqlite3 사용 시
sqlite3 health.db < init_health.sql
```

3. 스크립트 실행

```bash
python health_manager.py
```

도커로 실행

```bash
docker-compose up --build
```

기여 및 라이선스
- 간단한 버그 리포트나 개선 제안은 이 저장소의 Issue로 남겨 주세요.
- 기본 라이선스: MIT (원하시면 변경하세요)

연락처
- 저장소: https://github.com/woxihuannuli-coder/happy_health_care_program
