# 대전략 포터블 (PSP) 비공식 한글패치

PSP 일본판 **大戦略ポータブル (대전략 포터블, ULJM-05068, v1.03)** 비공식 한국어 패치입니다. 이 저장소에는 제작 도구와 기술 문서만 있고, 패치 파일(xdelta)은 [Releases](../../releases)에서 받을 수 있습니다. 게임 원본·일본어 원문·번역 대본은 포함하지 않습니다.

## 적용 방법

1. 아래 해시와 일치하는 **원본 `.iso`** 를 준비합니다. (CSO·CHD 등으로 변환한 이미지에는 적용할 수 없습니다.)
   - PowerShell: `Get-FileHash -Algorithm MD5 -LiteralPath '.\Daisenryaku Portable (Japan) (v1.03).iso'`
2. xdeltaUI 같은 도구로 원본 `.iso` 에 `DaisenryakuPortable_KO_v1.0.2.xdelta` 를 적용합니다. (Patch = xdelta, Source File = 원본 ISO, Output File = 새 파일명)
   - 명령줄: `xdelta3 -d -s "Daisenryaku Portable (Japan) (v1.03).iso" DaisenryakuPortable_KO_v1.0.2.xdelta "Daisenryaku Portable (Korean).iso"`
3. 만들어진 ISO를 PPSSPP 또는 커스텀 펌웨어(PSP·PS Vita Adrenaline 등)에서 실행합니다.

| 항목 | 값 |
| --- | --- |
| 원본 ISO 크기 | 138,772,480 바이트 |
| 원본 ISO MD5 | `0fd15a8dc14b1e6a65a75008377230d0` |
| 원본 ISO SHA-256 | `10805fc55a0508f2b8a15ab6cf991831413805111f4c56e99c21492ecc6dc2ad` |
| xdelta SHA-256 | `db45bc8c3d8f522ad36066e82a82ac3057efdc3ebbb4a023223ddc220ecbace2` |
| 결과 ISO 크기 | 138,772,480 바이트 |
| 결과 ISO SHA-256 | `bfc3d846f59e248c885cda84206e1dd358efec1e049ec440496ed1da2712c0a4` |

## 주의
- 암호화되지 않은 수정 실행 파일(BOOT.BIN)을 EBOOT.BIN 자리에도 넣었기 때문에 **PPSSPP·커스텀 펌웨어 전용**입니다. 정품 펌웨어에서는 부팅되지 않습니다.
- v1.03 원본 전용입니다.
- 원본에서 만든 **상태저장(세이브 스테이트)** 은 불러오지 마세요. 일반 세이브 데이터는 그대로 쓸 수 있습니다.
- xdelta는 2차 압축을 쓰지 않은 형식입니다(약 1MB).

## 한글화 내용
- 게임 문자열 887항목(유닛 이름·설명, 지형, 무기, 메뉴, 확인창, 시나리오·미션 설명, 승리 조건 등) 전체 직접 번역 (기계 번역 사용하지 않음)
- 게임 글꼴에 한글 560자 추가 (갈무리11 기반 도트 글꼴)
- 실행 파일 문자열 36개: 세이브 데이터 제목·설명, 시나리오 이름 32개
- 그림 글자 19장·라벨 464개: 메뉴 제목, 전황·부대표·유닛 정보 창, 버튼 안내, 대화상자, 결과 화면 등
  - 타이틀 로고 옆에 「대전략 포터블」 한글 자막
  - 원본과 비슷한 글꼴(나눔스퀘어네오·서울한강체)을 쓰고, 작은 글씨는 갈무리 글꼴로 선명하게 그렸습니다.

## 그대로 둔 것
- 타이틀 로고 그림(옆에 한글 자막을 입힘), 「press start button」·저작권 표기
- 「turn」·「MAP」·「Units」 같은 영문 장식 글자

## 검증 범위
PPSSPP에서 세이브 불러오기, 모드 선택, 전장 맵, 전황·부대표·유닛 상세·지형 정보, 맵 메뉴, 이동·공격·점령 메뉴, 공격 대상 선택, 세이브 화면을 실제로 확인했습니다. 그림 글자는 원본 글자 영역을 벗어나는지 전수 검사했습니다. 미션 선택·결과 화면과 일부 유닛(항공기 추력 등) 정보, 실기 PSP는 확인하지 못했습니다. 문제를 발견하면 Issues로 알려 주세요.

## 문서
- [CHANGELOG.md](CHANGELOG.md) — 변경 기록
- [docs/TECHNICAL.md](docs/TECHNICAL.md) — 파일 형식과 한글화 방법
- [docs/BUILD.md](docs/BUILD.md) — 직접 빌드하는 방법
- [docs/TRANSLATION_GUIDE.md](docs/TRANSLATION_GUIDE.md) — 번역 지침
- [docs/FONT_CREDITS.md](docs/FONT_CREDITS.md) — 글꼴
- [RIGHTS.md](RIGHTS.md) — 권리 및 외부 자료
