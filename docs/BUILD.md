# 직접 빌드하기

필요한 것: Python 3.11 이상, `pip install pillow numpy scipy pycdlib capstone websocket-client`, 원본 ISO(README 해시와 일치), 글꼴(`FONT_CREDITS.md`), 번역 대본.

1. 원본 ISO를 프로젝트 루트에 `Daisenryaku Portable (Japan) (v1.03).iso` 이름으로 둡니다.
2. 파일 추출: `python tools/extract.py "Daisenryaku Portable (Japan) (v1.03).iso" work/ext`
3. USRDIR의 LZSS 압축 파일을 `work/dec/` 에 풉니다(`tools/lzss.py` 의 `decompress`, 경로의 `/` 는 `__` 로 바꾼 이름).
4. 번역 대본을 `work/trans/` 에 둡니다. `ja_list.json`(번호→원문)과 `ko_*.json`(번호 또는 원문→번역) 형식입니다. 대본은 저장소에 없습니다.
5. 빌드: `python tools/build.py` → `Daisenryaku Portable (Korean).iso` 생성 (원본 ISO는 수정하지 않음)
6. 배포 파일: `xdelta3 -0 -e -s "Daisenryaku Portable (Japan) (v1.03).iso" "Daisenryaku Portable (Korean).iso" DaisenryakuPortable_KO_v1.0.xdelta`

## 확인용 도구
- `tools/emu.py` — PPSSPP 디버거(WebSocket)로 실행·버튼 입력·화면 캡처 (`PPSSPP_EXE` 환경 변수로 실행 파일 지정)
- `tools/imgprev.py`, `tools/imgdet.py` — 그림 글자 미리보기·원본 글자 영역 검출 (`IMG_PREVIEW_DIR` 에 저장)
- `tools/scan.py` — 실행 파일·데이터에서 게임 문자 코드 문자열 찾기
