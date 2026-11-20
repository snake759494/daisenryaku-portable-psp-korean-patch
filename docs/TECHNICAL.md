# 기술 문서

## 디스크 구성
- `PSP_GAME/SYSDIR/BOOT.BIN` — 암호화되지 않은 실행 파일. 세이브 제목·시나리오 이름 등 UTF-8 문자열이 들어 있습니다(`tools/bootpatch.py`). 수정본을 `EBOOT.BIN` 자리에도 넣습니다.
- `PSP_GAME/PARAM.SFO` — 게임 제목.
- `PSP_GAME/USRDIR/` — 게임 데이터. 대부분 LZSS로 압축되어 있습니다(`tools/lzss.py`).

## 문자열 (`STRING/string_ash.dat`)
- 섹션 표 → 섹션마다 항목 표가 있는 구조이고, 각 문자열은 16비트 글자 코드 배열입니다(`tools/strfile.py`).
- 글자 코드는 게임 글꼴의 칸 번호입니다. 0x80–0xBF는 반각, 0x1FF는 줄바꿈입니다. 일본어 문자표는 `tools/jtable.py`.
- 번역하면서 쓰는 한글 글자를 모아, 원문에서 쓰지 않는 글꼴 칸에 배정합니다(`tools/kfont.py`, 결과 `work/out/cmap.json`).

## 글꼴 (`STRING/font_ash.dat`)
- 512×512 8비트 인덱스 GIM(스위즐) 한 장에 모든 글자가 격자로 들어 있습니다(`tools/gim.py`, `tools/gimfile.py`).
- 빈 칸에 갈무리11로 그린 한글 560자를 넣었습니다. 원본 글자와 같은 팔레트 단계(그림자 포함)를 씁니다.

## 그림 글자
- 메뉴·창 그림은 여러 GIM을 묶은 컨테이너 파일입니다(`tools/cont.py`). 대부분 8비트 인덱스(idx8) 텍스처입니다.
- `tools/imgspec.py` 에 텍스처별로 「영역(x, y, 폭, 높이), 한국어 문구, 스타일」을 적어 두면 `tools/imgtool.py` 가 원본 글자를 지우고 한글을 그립니다(`tools/extras.py` 에서 호출).
- 게임은 각 라벨의 일부 영역만 화면에 잘라 쓰기 때문에, 원본 글자의 잉크 영역을 벗어나면 옆 라벨에 잔재가 보입니다. 원본 글자 영역을 자동 검출해(`tools/imgdet.py`) 그 안에 맞도록 크기를 고르고, 넘치면 작은 갈무리 글꼴로 바꿉니다.

## ISO 재구성
- `tools/isobuild.py` 가 원본 ISO를 복사한 뒤 바뀐 파일만 같은 자리(또는 빈 영역)에 다시 써서 디렉터리 레코드를 고칩니다. 결과 ISO 크기는 원본과 같습니다.
