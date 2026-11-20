# (container, gim name) -> list of jobs [x,y,w,h,text,opts]
B={'font':'bold','sx':0.5,'fill':[25,21,19,255],'outline':None,'bg':'rowmed'}
SPEC={
('UI/tex_op_ash.dat','image/UI_tmenu01.gim'):[
 [288,276,160,23,'시나리오 모드',dict(B,align='l',size=22)],
 [288,308,150,23,'프리 모드',dict(B,align='l',size=22)],
 [10,397,170,24,'미션 모드',dict(B,align='l',size=22)],
 [10,429,170,24,'병기 도감',dict(B,align='l',size=22)],
 [10,461,170,24,'세이브/로드',dict(B,align='l',size=22)],
 [224,397,156,22,'통신 대전',dict(B,align='l',size=22)],
 [224,429,156,22,'옵션',dict(B,align='l',size=22)],
 [224,461,156,22,'컨티뉴',dict(B,align='l',size=22)],
 [0,268,212,78,'이 게임은 픽션입니다.\n실재하는 인물·단체 등과는\n일절 관계가 없습니다.',dict(font='sans',size=19,spacing=8,sx=0.7)],
 [450,336,61,15,'이어서',dict(font='bold',bg=[219,217,216,255],fill=[255,255,255,255],outline=[150,140,135,255],size=14,align='c')],
 [450,352,46,15,'로드',dict(font='bold',bg=[219,217,216,255],fill=[255,255,255,255],outline=[150,140,135,255],size=14)],
 [450,368,60,15,'처음부터',dict(font='bold',bg=[219,217,216,255],fill=[255,255,255,255],outline=[150,140,135,255],size=14)],
 [450,384,46,15,'세이브',dict(font='bold',bg=[219,217,216,255],fill=[255,255,255,255],outline=[150,140,135,255],size=14)],
 [180,370,26,17,'삭제',dict(font='bold',size=15)],
 [190,488,98,18,'모드 선택',dict(font='bold',size=17,bg=[200,200,200,255],fill=[255,255,255,255],outline=[150,140,135,255])],
 [288,488,122,18,'미션 모드',dict(font='bold',size=17,bg=[200,200,200,255],fill=[255,255,255,255],outline=[150,140,135,255])],
],
}
W=dict(font='bold',bg='mode',fill=[255,255,255,255],outline=[40,40,40,255])
Y=dict(font='bold',bg='mode',fill=[220,200,40,255],outline=[60,50,10,255])
SPEC[('UI/tex_op_ash.dat','image/UI_tmenu02.gim')]=[
 [82,0,76,16,'전체 맵',dict(W,outline=None,size=14)],
 [82,19,76,17,'대도시',dict(W,outline=None,size=15,align='l')],
 [82,40,76,17,'소도시',dict(W,outline=None,size=15,align='l')],
 [82,61,76,17,'육군 기지',dict(W,outline=None,size=15,align='l')],
 [82,82,76,17,'공군 기지',dict(W,outline=None,size=15,align='l')],
 [82,103,76,17,'보급 기지',dict(W,outline=None,size=15,align='l')],
 [82,124,76,17,'미사일 기지',dict(W,outline=None,size=15,align='l')],
 [8,68,68,17,'선택 불가',dict(Y,bg='rowmed',thr=0,size=16)],
 [14,158,52,20,'B진영',dict(Y,size=17)],
 [94,150,56,20,'A진영',dict(Y,size=17)],
 [162,3,62,16,'플레이어',dict(Y,size=15,align='l')],
 [162,27,62,16,'생산 타입',dict(Y,size=15,align='l')],
 [162,51,62,16,'군자금',dict(Y,size=15,align='l')],
 [162,84,62,17,'동맹국 설정',dict(Y,size=15,align='l')],
 [224,64,90,28,'검색 중...',dict(W,bg='rowmed',thr=0,size=26,align='l')],
 [162,101,342,82,'메모리 스틱™의 빈 용량이 부족합니다.\n대전략 포터블의 데이터를 세이브하려면\n메모리 스틱™에\n320KB 이상의 빈 용량이 필요합니다.\n이대로 게임을 시작하시겠습니까?',dict(W,size=14,spacing=2,outline=[60,60,60,255])],
 [0,182,318,80,'메모리 스틱™을 찾을 수 없습니다.\n대전략 포터블의 데이터를 세이브하려면\n320KB 이상의 빈 용량이 있는\n메모리 스틱™이 필요합니다.\n이대로 게임을 시작하시겠습니까?',dict(W,size=14,spacing=2,outline=[60,60,60,255])],
 [316,182,96,40,'대전 상대\n대기 중...',dict(W,size=18,spacing=3)],
 [415,182,74,19,'준비 완료',dict(W,size=17)],
 [415,204,74,19,'전투 준비',dict(W,size=17)],
 [356,292,48,17,'불참가',dict(W,size=15,outline=[80,80,80,255])],
 [334,314,76,17,'진영 설정',dict(W,size=15)],
 [411,314,92,17,'참전국 선택',dict(W,size=15)],
 [334,334,76,18,'통신 대전',dict(W,size=15)],
 [106,408,66,18,'동맹국 설정',dict(W,size=15)],
 [474,399,34,16,'색적',dict(W,outline=None,size=14)],
 [474,417,36,16,'없음',dict(W,outline=None,size=14)],
 [420,440,84,16,'턴 수 설정',dict(W,size=15)],
 [294,456,64,17,'초기 생산',dict(W,outline=None,size=15)],
 [0,455,182,16,'세이브 데이터를 로드하겠습니까?',dict(W,size=14,outline=[60,60,60,255])],
 [0,471,120,14,'삭제를 중지하겠습니까?',dict(W,size=14,outline=[60,60,60,255])],
 [120,471,220,14,'삭제를 중지했습니다. 다시 시도하겠습니까?',dict(W,size=14,outline=[60,60,60,255])],
 [464,0,42,17,'군자금',dict(W,size=14)],
 [466,18,36,16,'있음',dict(W,outline=None,size=14)],[478,34,22,16,'낮',dict(W,outline=None,size=14)],
 [388,383,76,18,'전장 선택',dict(W,size=15)],
 [188,401,100,20,'참가국 설정',dict(W,size=16)],
 [288,401,82,20,'게임 설정',dict(W,size=16)],
 [190,423,66,17,'플레이어',dict(W,fill=[20,20,20,255],outline=None,size=14)],
 [256,423,64,17,'생산 타입',dict(W,fill=[20,20,20,255],outline=None,size=14)],
 [334,423,20,17,'밤',dict(W,outline=None,size=14)],
 [480,354,32,15,'낮밤',dict(W,outline=None,size=13)],
]
TT=dict(font='bold',maxk=1,bg='mode',fill=[255,255,255,255],outline=[40,60,70,255])
GG=dict(font='bold',bg=[255,255,255,0],fill=[235,254,235,255],outline=[78,180,158,255])
PN=dict(font='bold',bg='outside',fill=[255,255,255,255],outline=[30,60,80,255])
SPEC[('UI/tex_op_ash.dat','image/UI_tmenu03.gim')]=[
 [346,148,158,19,'시나리오 전황',dict(TT,size=19,align='l')],
 [346,169,76,18,'진영 선택',dict(TT,size=18)],
 [422,169,70,18,'수도 공방',dict(TT,size=18)],
 [210,170,101,18,'폭발의 대가',dict(TT,size=18)],
 [202,191,80,19,'불협화음',dict(TT,size=19)],
 [312,190,162,19,'카운터어택',dict(TT,size=19)],
 [0,200,48,17,'고도',dict(TT,size=17)],
 [48,200,80,17,'열도 침공',dict(TT,size=17)],
 [130,210,78,18,'민족 단결',dict(TT,size=18)],
 [286,208,152,18,'등 뒤의 일격',dict(TT,size=18)],
 [0,220,100,18,'복수의 잔향',dict(TT,size=18)],
 [212,227,178,18,'서남서로 침로를 잡아라',dict(TT,size=18)],
 [390,227,80,18,'열도 진감',dict(TT,size=18)],
 [0,240,148,18,'라이라이 붉은 거인',dict(TT,size=18)],
 [150,248,140,18,'전화 속의 평화도시',dict(TT,size=18)],
 [290,248,100,18,'내해의 싸움',dict(TT,size=18)],
 [390,248,100,18,'열사와 초연',dict(TT,size=18)],
 [0,265,200,19,'벚꽃 춤 -열도 탈환Ⅰ-',dict(TT,size=19)],
 [200,265,192,19,'벚꽃 춤 -열도 탈환Ⅱ-',dict(TT,size=19)],
 [392,265,98,19,'태양의 송곳니',dict(TT,size=19)],
 [0,286,120,19,'심야의 조우전',dict(TT,size=19)],
 [120,286,90,19,'모래먼지의 묘표',dict(TT,size=19)],
 [210,286,115,19,'반격의 봉화',dict(TT,size=19)],
 [325,286,123,19,'반도 상륙 작전',dict(TT,size=19)],
 [0,307,158,19,'동쪽 매 작전 발동Ⅰ',dict(TT,size=19)],
 [158,307,155,19,'동쪽 매 작전 발동Ⅱ',dict(TT,size=19)],
 [313,307,100,19,'수도 탈환Ⅰ',dict(TT,size=19)],
 [413,307,99,19,'수도 탈환Ⅱ',dict(TT,size=19)],
 [0,327,225,19,'열하 종언의 시작',dict(TT,size=19)],
 [225,327,74,19,'북쪽의 맹우',dict(TT,size=19)],
 [299,327,127,19,'개미와 거인들',dict(TT,size=19)],
 [426,327,72,19,'북쪽의 선풍',dict(TT,size=19)],
 [0,347,118,19,'한 줌의 영원',dict(TT,size=19)],
 [118,347,244,19,'멸망의 주문 -독재의 결말-',dict(TT,size=19)],
 [212,210,56,16,'C공화국',dict(GG,size=16)],
 [439,209,56,15,'A합중국',dict(GG,size=15)],
 [150,230,43,14,'K민국',dict(GG,size=14)],
 [449,288,41,15,'혼성군',dict(GG,size=15)],
 [363,349,55,14,'N인민국',dict(GG,size=14)],
 [420,349,55,14,'R공화국',dict(GG,size=14)],
 [480,55,28,16,'J국',dict(GG,size=15)],
 [4,57,34,16,'목적',dict(PN,size=15,align='l')],
 [4,103,64,16,'승리 조건',dict(PN,size=15,align='l')],
 [4,164,76,16,'지급 군자금',dict(PN,size=15,align='l')],
]
OP=dict(font='bold',bg='mode',fill=[240,248,255,255],outline=[90,130,175,255])
SPEC[('UI/tex_op_ash.dat','image/UI_tmenu04.gim')]=[
 [338,271,88,19,'옵션',dict(OP,size=16)],
 [436,272,23,17,'함',dict(OP,size=15)],
 [459,272,48,17,'안 함',dict(OP,size=15)],
 [206,305,27,16,'빠름',dict(OP,size=14)],
 [278,305,72,16,'전투 애니',dict(OP,size=14)],
 [351,305,57,16,'가이드',dict(OP,size=14)],
 [408,305,78,16,'헥스 테두리',dict(OP,size=14)],
 [196,322,57,17,'이동 속도',dict(OP,size=14)],
 [254,322,72,17,'수입 확인',dict(OP,size=14)],
 [327,322,76,17,'보급 확인',dict(OP,size=14)],
 [406,322,30,17,'느림',dict(OP,size=14)],
]
def lab(x,y,w,h,t,m='p',**k):
    o=dict(font=('pixel' if h<=13 else 'bold'),fill=[255,255,255,255],outline=[30,30,30,255],size=h if h>13 else 12,align='l')
    if m=='p': o.update(font='pixel',size=12,fit=False,ow=1,ix={'bg':240,'fill':255,'outline':97})
    elif m=='x': o=dict(auto=True,align=k.get('align','c'))
    if m=='x': o.update(k); return [x,y,w,h,t,o]
    elif m=='g': o.update(bg='outside')
    o.update(k)
    return [x,y,w,h,t,o]
X='x';G='g'
SPEC[('UI/tex_ui_ash.dat','image/UI_uniphs.gim')]=[
 lab(122,4,24,12,'대수'),lab(122,17,24,12,'연료'),lab(122,30,24,12,'탄수'),lab(122,43,32,12,'경험치'),
 lab(122,62,50,12,'병기 타입'),lab(122,75,24,12,'색적'),lab(122,88,32,12,'회피율'),lab(122,101,32,12,'이동력'),
 lab(122,114,24,12,'사정'),lab(122,127,24,12,'화력'),lab(122,140,44,12,'지형 효과'),lab(122,153,24,12,'수입'),
 lab(122,176,34,13,'수납수'),lab(122,189,24,13,'시야'),lab(122,202,56,13,'소비 이동력'),
 lab(72,184,40,12,'보급·공',X,gstart=2),lab(72,196,40,12,'생산·공',X,gstart=2),lab(122,233,44,13,'헬기 착륙'),
 [3,235,53,12,'진영 건물',dict(font='pixel',size=12,fit=False,ix={'bg':240,'fill':255,'ramp':True})],[69,235,40,12,'수입',dict(font='pixel',size=12,fit=False,ix={'bg':240,'fill':255,'ramp':True})],
 lab(2,250,56,15,'점령 내구도'),lab(2,274,56,15,'파괴 내구도'),
 lab(216,134,54,15,'공군 기지',X),lab(214,150,54,15,'보급 기지',X),lab(214,166,40,15,'탑재수',X),
 lab(214,184,40,12,'수리·육',X,gstart=2),lab(254,184,22,12,'헬기',X,gstart=2),lab(214,196,40,12,'보급·육',X,gstart=2),lab(214,208,40,12,'생산·육',X,gstart=2),
 lab(214,220,40,12,'수납·공',X,gstart=2),lab(214,232,40,12,'수납·육',X,gstart=2,bgidx=0),lab(214,244,56,12,'탄두 미사일',X,gstart=2,dy=1),
 lab(400,2,52,12,'건물 특성',align='c'),
 lab(464,28,38,15,'사령부',X),lab(464,44,38,15,'대도시',X),lab(464,60,38,15,'소도시',X),
 lab(478,76,30,12,'불가',X,gstart=2),lab(464,88,22,12,'가능',X,gstart=2),lab(486,88,26,12,'위성',X,gstart=2),lab(464,100,24,12,'수리',X,gstart=2),lab(488,100,24,12,'대지',X,gstart=2),
 lab(464,112,46,12,'수리·공',X,gstart=2),
 lab(484,124,28,12,'보급',X,gstart=2),lab(484,136,28,12,'색적',X,gstart=2),lab(484,148,28,12,'수납',X,gstart=2),lab(484,160,28,12,'대지',X,gstart=2),lab(484,172,28,12,'탄미',X,gstart=2),lab(484,184,28,12,'고공',X,gstart=2),
 lab(354,108,48,17,'군자금',X),lab(410,108,52,17,'육군 기지',X),
 lab(330,156,40,15,'명중률',align='c'),lab(419,156,58,15,'공격 특성',align='c'),lab(414,192,66,15,'유닛 특성',align='c'),
 lab(304,208,86,15,'탑재 중인 유닛',align='c'),lab(410,270,44,15,'수납수'),
 lab(488,258,24,12,'헬기',X,gstart=2),lab(488,270,24,12,'보급',X,gstart=2),
 lab(304,310,52,15,'파괴·수복',X),
 lab(310,328,76,16,'군자금 수입',G),lab(310,352,90,16,'지형 상세 정보',G),
 lab(292,370,58,14,'메가 헥스',X),lab(352,370,48,14,'미사일 발사',X),lab(400,370,46,14,'점령·회복',X),lab(448,370,40,14,'스텔스',X),
 lab(451,382,43,12,'건물 파괴',X,bgidx=225),[450,393,46,12,'1기 탑재',dict(font='pixel9',size=10,fit=False,ow=1,align='c',noexpand=True,ix={'bg':225,'fill':255,'outline':13})],[450,405,46,1,' ',dict(font='pixel9',size=10,fit=False,ow=0,noexpand=True,nofit=True,ix={'bg':225,'fill':225})],lab(412,410,42,14,'2기 탑재',X),lab(464,424,36,14,'수송',X),
 lab(6,381,96,19,'수납 중인 부대',G),lab(230,381,92,19,'탑재 중인 부대',G),lab(6,406,90,16,'부대 상세 정보',G),
 lab(0,426,100,16,'참가국 변경',G,align='c'),lab(104,426,96,16,'게임 종료',G,align='c'),[213,427,48,13,'총수입',dict(font='pixel',size=12,fit=False,ix={'bg':240,'fill':255,'ramp':True})],
 lab(330,426,124,15,'전장 맵 변경',G,align='c'),lab(330,442,120,15,'미션 선택',G,align='c'),
]
OC=dict(font='bold',bg=[0,0,0,0],fill=[255,255,255,255],outline=[50,50,50,255],align='r',size=13)
SPEC[('UI/tex_ui_ash.dat','image/UI_occup.gim')]=[
 [150,1,75,14,'사령부',OC],[150,17,75,14,'대도시',OC],[150,33,75,14,'소도시',OC],[150,49,75,14,'육군 기지',OC],
 [150,65,75,14,'공군 기지',OC],[150,81,75,14,'보급 기지',OC],[150,97,75,14,'미사일 기지',OC],
 [0,106,56,14,'점령 내구도',dict(OC,align='c',size=12,font='pixel')],[56,107,58,13,'파괴 내구도',dict(OC,align='c',size=12,font='pixel')],
]
SY=dict(font='pixel',bg=[0,0,0,0],fill=[8,12,20,255],outline=None,size=12)
SPEC[('UI/tex_ui_ash.dat','image/UI_sys.gim')]=[
 [184,0,55,12,'전투 애니',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [240,0,21,12,'있음',dict(uni=True,gen=True,dx=1,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [296,0,53,12,'가이드',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [352,0,56,12,'게임 종료',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [408,0,24,12,'빠름',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [432,0,60,12,'보급 확인',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [184,12,48,12,'이동 속도',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [232,12,21,12,'없음',dict(uni=True,gen=True,dx=1,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [256,12,24,12,'느림',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [280,12,27,12,'안 함',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [307,12,26,12,'함',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [336,12,60,12,'수입 확인',dict(uni=True,gen=True,fillidx=39,gi=2,noexpand=True,bgidx=24)],
 [399,12,40,12,'시스템',dict(uni=True,gen=True,fillidx=255,gi=2,noexpand=True,bgidx=24)],
]
SPEC[('UI/tex_ui_ash.dat','image/prdctanm.gim')]=[
 [0,0,132,32,'생산 페이즈',dict(font='heavy',restrict=False,bg=[0,0,0,0],fill=[252,249,198,255],outline=[252,249,198,60],ow=2,size=24,dy=0)],
]
H=dict(font='bold',bg=[0,0,0,255],fill=[255,255,255,0],outline=None,size=14)
HP=dict(H,font='pixel',size=12)
OR=dict(auto=True)
def row(y,h,items,st): return [[i[0],y,i[1],h,i[2],(i[3] if len(i)>3 else st)] for i in items]
U=dict(uni=True)
SPEC[('UI/tex_ui_ash.dat','image/UI_share.gim')]=(
 row(403,15,[(0,44,'파괴'),(238,44,'공격'),(282,44,'점령'),(326,44,'수납'),(370,44,'탑재'),(414,44,'이동'),(458,44,'합류')],U)+
 row(418,15,[(44,44,'회복'),(88,44,'수복'),(132,44,'미사일'),(176,52,'대기',dict(uni=True,dx=9)),(228,68,'취소'),(296,44,'해산'),(340,44,'부대표'),(384,66,'옵션'),(450,43,'세이브')],U)+
 row(436,15,[(0,73,'페이즈 종료'),(104,56,'탑재 부대'),(160,54,'수납 부대'),(214,46,'위성'),(262,44,'철수')],U)+
 row(389,15,[(22,52,'보급 기지'),(172,40,'사령부'),(244,40,'대도시'),(316,40,'소도시'),(376,52,'육군 기지'),(448,52,'공군 기지')],U)+
 row(373,16,[(1,32,'안 함'),(33,32,'함'),(66,72,'수입 확인'),(200,70,'이동 속도',dict(uni=True,ty=374,clr=[(200,369,270,373)])),(329,67,'헥스 테두리'),(397,70,'보급 확인'),(467,32,'느림')],U)+
 row(356,17,[(0,70,'전투 애니'),(104,71,'가이드'),(174,28,'빠름'),(232,27,'있음'),(260,68,'게임 종료',dict(uni=True,ty=361))],dict(uni=True,ty=358))+
 [[87,389,42,14,'부대 상세',OR],[153,376,42,15,'전투 개시',OR],[326,436,62,15,'착륙 지점 선택',OR],[404,436,64,15,'부대 상세 정보',OR],[484,436,22,15,'해제',OR],
  [17,453,62,11,'지형 상세 정보',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[95,453,59,11,'게임으로',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[169,453,21,11,'결정',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[207,453,38,11,'전환',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],
  [263,453,40,11,'수리하기',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[318,454,24,10,'종료',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[358,453,21,11,'등록',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[403,451,46,11,'취소',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[465,451,22,11,'확정',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],
  [27,468,55,12,'현재 위치',dict(auto=True,font='pixel9',size=10)],[108,467,51,11,'생산국 변경',dict(font='pixel9',size=10,fit=False,ow=1,ix={'bg':254,'fill':255,'outline':6})],[314,468,62,11,'공격 대상 선택',dict(HP,font='pixel9',size=10,noexpand=True)],[394,468,72,15,'최단 루트 설정',OR],
  [0,484,62,15,'합류 대상 선택',OR],[484,357,28,15,'없음',dict(uni=True,ty=358)],[373,339,42,13,'위성 사진',OR],[78,403,66,15,'미사일 기지',U],[16,423,20,10,'발진',dict(font='pixel9',size=10,fit=False,ow=0,noexpand=True,nofit=True,ix={'bg':6,'fill':255})],[160,468,57,15,'점령 내구도',dict(HP,noexpand=True)],[217,468,56,15,'파괴 내구도',dict(HP,noexpand=True,dy=-2)],
  [410,192,90,26,'위성 사진',dict(H,size=24)],[274,273,112,26,'현재 위치',dict(H,size=24)],[288,305,58,13,'커서 이동',OR],
 ])
RH=dict(font='serif',ix={'bg':255,'fill':254,'outline':205},ow=2,align='c')
RS=dict(font='bold',bg='edge',fill=[138,193,199,255],outline=None,size=13)
SPEC[('UI/tex_ui_ash.dat','image/UI_res02.gim')]=[
 [232,272,160,30,'사령부 제압',dict(RH,size=26)],[232,303,160,30,'적 부대 전멸',dict(RH,size=26)],
 [196,334,230,31,'미사일 기지 제압',dict(RH,size=26)],[88,366,208,31,'제한 턴 달성',dict(RH,size=26)],
 [326,366,186,31,'동맹 부대 전멸',dict(RH,size=26)],[16,398,214,32,'동맹 사령부 함락',dict(RH,size=26)],
 [230,398,254,32,'와일드 기스 전멸',dict(RH,size=26)],[11,430,231,32,'미사일 기지 함락',dict(RH,size=26)],
 [260,430,212,32,'제한 턴 초과',dict(RH,size=26)],
 [392,272,38,14,'세이브',RS],[392,286,100,14,'다른 데이터 삭제',RS],
 [164,462,154,14,'이 전투를 기록하겠습니까?',dict(uni=True,gal=('Galmuri9.ttf',10),ty=462,fillidx=241,align='c')],[319,462,180,14,'실행할 처리를 선택해 주십시오.',dict(font='pixel',size=12,fit=False,ix={'bg':225,'fill':255})],
 [480,122,26,14,'뒤로',dict(font='pixel',size=12,fit=False,align='c',ix={'bg':80,'fill':255})],
 [1,272,30,12,'대수',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],[1,285,30,12,'연료',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],[1,298,30,12,'탄수',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],
 [1,318,30,12,'색적',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],[1,331,32,12,'회피율',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],[1,344,32,12,'이동력',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],
 [1,357,30,12,'사정',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],[1,370,30,12,'화력',dict(RS,font='pixel',size=12,align='l',bg='rowmed',thr=100,outline=[20,29,38,255])],
]
KN=dict(font='bold',ix={'bg':225,'fill':255,'ramp':True},size=13,pad=2)
KD=dict(font='bold',ix={'bg':251,'fill':244,'outline':108},size=12)
SPEC[('UI/tex_sh_ash.dat','image/UI_kyo01c.gim')]=[
 [0,137,30,14,'종료',KN],[30,137,59,14,'진영 선택',KN],[89,137,59,14,'작전 개시',KN],[148,137,58,14,'다음으로',KN],[206,137,42,14,'아니오',KN],
 [29,151,30,15,'결정',KN],[59,151,29,15,'전황',KN],[88,151,44,15,'국명',KN],[132,151,30,15,'뒤로',KN],[161,151,27,15,'예',KN],
 [0,166,216,12,'로드를 중지했습니다. 다시 시도하겠습니까?',dict(KN,font='pixel',size=12,pad=0)],[0,178,216,12,'세이브를 중지했습니다. 다시 시도하겠습니까?',dict(KN,font='pixel',size=12,pad=0)],
 [0,190,134,12,'로드를 중지하겠습니까?',dict(KN,font='pixel',size=12,pad=0)],
 [52,106,31,14,'뒤로',KN],[106,106,60,14,'변경 확인',KN],
 [166,106,27,14,'예',KD],[188,152,38,14,'아니오',KD],
 [134,189,54,14,None],
]
CN=dict(font='bold',bg=[255,255,255,0],fill=[255,255,255,255],outline=None,shadow=[67,67,67,160],size=14)
SPEC[('UI/tex_sh_ash.dat','image/UI_kyo02c.gim')]=[
 [10,2,64,17,'A합중국',CN],[90,2,64,17,'C공화국',CN],[180,2,40,17,'J국',CN],
 [18,26,52,17,'K민국',CN],[100,26,52,17,'혼성군',CN],[172,26,58,17,'N인민국',CN],
 [10,50,64,17,'R공화국',CN],[84,50,78,17,'와일드 기스',CN],
 [0,96,124,12,'삭제를 중지하겠습니까?',dict(KN,size=12)],[0,108,212,12,'삭제를 중지했습니다. 재시도하겠습니까?',dict(KN,size=12)],
]
SPEC[('UI/tex_sh_ash.dat','image/loadanm.gim')]=[
 [3,0,123,32,'로딩 중...',dict(font='bold',bg=[69,254,188,0],fill=[255,255,255,255],outline=[66,253,188,70],ow=2,size=20,align='l',restrict=False)],
]
MS=dict(font='heavy',bg='outside',fill=[252,249,198,255],outline=[56,64,59,204],ow=1)
SPEC[('UI/tex_ui_ash.dat','image/mission.gim')]=[
 [128,10,224,54,'작전 개시',dict(MS,size=46,ow=2)],
 [110,201,270,26,'BLUE 진영 행동 개시',dict(MS,font='bold',size=22)],
 [110,273,270,26,'RED 진영 행동 개시',dict(MS,font='bold',size=22)],
 [110,343,270,26,'GREEN 진영 행동 개시',dict(MS,font='bold',size=22)],
 [100,416,280,26,'YELLOW 진영 행동 개시',dict(MS,font='bold',size=22)],
 [449,128,30,22,'잔여',dict(MS,font='bold',size=15,bg='edge')],
 [0,447,70,26,'턴',dict(MS,font='bold',size=20,bg='edge',fill=[25,22,31,204],outline=None)],
]
XF=dict(font='serif',xfer=True,ow=2,inner=4)
RB=dict(font='serif',bg='edge',fill=[131,209,237,255],outline=[50,80,100,255],ow=1,size=20)
SPEC[('UI/tex_ui_ash.dat','image/UI_res01.gim')]=[
 [0,272,320,76,'작전 실패',dict(XF,size=64)],
 [320,272,160,76,'작전',dict(XF,size=64)],[0,348,160,80,'성공',dict(XF,size=64)],
 [160,348,160,80,'승리',dict(XF,size=64)],[320,348,160,80,'패배',dict(XF,size=64)],
 [0,432,70,32,'진영',dict(RB,size=22)],
 [72,432,48,24,'획득',RB],[120,432,50,24,'승격',RB],
 [170,432,170,24,'전장 맵 추가',RB],[340,432,152,24,'미션 입수',RB],
 [72,456,50,24,'병기',RB],
]
GB=dict(font='pixel',size=12,fit=False,ow=1,align='l',ix={'bg':{'norm':168,'grid':172,'pre':171,'period':8,'phase':124},'fill':255,'outline':0})
SL=dict(font='pixel',bg='rowmed',thr=0,fill=[255,255,255,255],outline=[30,30,30,255],size=12,align='l')
SPEC[('UI/tex_ui_ash.dat','image/UI_resrep.gim')]=[
 [138,217,118,24,'격파·점령 수',dict(XF,size=20,ow=1,inner=2,xfer_bg=217)],[256,221,108,24,'생존 부대 수',dict(XF,size=20,ow=1,inner=2,xfer_bg=217)],
 [280,194,98,25,'종합 평가',dict(XF,size=22,ow=1,inner=2,xfer_bg=254)],[383,194,104,25,'전과 보고',dict(XF,size=22,ow=1,inner=2,xfer_bg=254)],
 [383,221,106,24,'작전 턴',dict(XF,size=20,ow=1,inner=2,xfer_bg=217)],
 [185,174,30,12,'연료',dict(font='pixel',size=12,fit=False,ow=1,align='l',ix={'bg':{'norm':170,'grid':171,'period':8,'phase':171},'fill':255,'outline':0})],[185,187,30,13,'탄수',dict(font='pixel',size=12,fit=False,ow=1,align='l',ix={'bg':{'norm':170,'grid':171,'period':8,'phase':171},'fill':255,'outline':0})],[185,201,40,13,'경험치',dict(font='pixel',size=12,fit=False,ow=1,align='l',ix={'bg':{'norm':170,'grid':171,'period':8,'phase':171},'fill':255,'outline':0})],
 [328,140,48,12,'지형 효과',GB],[328,154,26,12,'수입',GB],
]
CP=dict(font='bold',bg='edge',fill=[255,255,255,255],outline=[30,30,30,255],size=13)
CPP=dict(CP,font='pixel',size=12)
SPEC[('UI/tex_ui_ash.dat','image/UI_cpupop.gim')]=[
 [330,9,44,16,'부대 수',CP],[286,25,62,17,'전과 예상',CP],[280,48,46,15,'부대표',CP],
 [247,68,72,14,'행동 페이즈',CPP],[319,68,70,14,'생산 페이즈',CPP],
 [247,84,54,14,'대전 상대',CPP],[301,84,51,14,'행동 중...',CPP],[352,84,36,14,'사용료:',CPP],
 [388,77,72,14,'진영 사고 중...',CPP],[460,77,42,14,'군자금:',CPP],
 [247,100,91,14,'해제할 수 없습니다',CPP],[388,92,108,14,'군자금이 부족합니다',CPP],[336,105,130,11,'이대로 괜찮겠습니까?',dict(font='pixel',size=12,fit=False,ix={'bg':225,'fill':255,'ramp':True})],
 [247,116,109,14,'부대 수가 최대입니다',CPP],[356,116,110,14,'수납처가 가득 찼습니다',CPP],
 [117,87,28,13,'화력',CPP],[146,87,36,13,'명중률',CPP],[183,87,26,13,'탄수',CPP],[211,87,36,13,'회피율',CPP],
 [319,197,30,14,'연료',dict(font='pixel',size=12,fit=False,ow=1,align='c',ix={'bg':{'norm':212,'grid':212,'gridval':150,'period':8,'phase':200},'fill':255,'outline':35})],[319,214,30,14,'대수',dict(font='pixel',size=12,fit=False,ow=1,align='c',ix={'bg':{'norm':212,'grid':212,'gridval':150,'period':8,'phase':200},'fill':255,'outline':35})],
]
SPEC[('UI/tex_ui_ash.dat','image/UI_prdct.gim')]=[
 [279,9,74,15,'점령 건물 수 :',dict(CP,align='l')],[279,24,74,15,'전력 부대 수 :',dict(CP,align='l')],[279,38,52,15,'군자금 :',dict(CP,align='l')],
 [456,17,50,16,'승리 조건',CP],[481,48,25,12,'가격',dict(font='pixel',size=12,fit=False,ow=1,align='l',ix={'bg':0,'fill':255,'outline':13})],[340,83,46,18,'전황',CP],
 [170,108,54,14,'최대 수납 수',CPP],[225,108,36,14,'적 진영',CPP],[266,106,66,18,'병기 생산',dict(CP,size=15)],
 [466,103,40,12,'지배율',dict(CPP,font='pixel9',size=10)],
 [482,60,30,10,'K민국',dict(CPP,font='pixel9',size=10)],[482,70,30,10,'혼성군',dict(CPP,font='pixel9',size=10)],[468,116,44,11,'A합중국',dict(CPP,font='pixel9',size=10)],
 [154,144,92,17,'이월 유닛',dict(font='sans',size=13,fit=False,ow=1,align='c',gstart=1,ix={'bg':0,'fill':255,'outline':13})],[249,144,92,17,'이월 유닛',dict(font='sans',size=13,fit=False,ow=1,align='c',gstart=1,ix={'bg':103,'fill':1,'outline':67})],[345,144,71,17,'수납 유닛',dict(font='sans',size=13,fit=False,ow=1,align='c',gstart=1,ix={'bg':0,'fill':255,'outline':13})],[419,144,68,17,'수납 유닛',dict(font='sans',size=13,fit=False,ow=1,align='c',gstart=1,ix={'bg':103,'fill':1,'outline':67})],
 [58,152,74,17,'유닛 생산',dict(font='sans',size=13,fit=False,ow=1,align='c',gstart=1,ix={'bg':0,'fill':255,'outline':13})],[138,167,74,16,'유닛 생산',dict(font='sans',size=13,fit=False,ow=1,align='c',gstart=1,ix={'bg':103,'fill':1,'outline':67})],
 [58,174,50,13,'R공화국',CPP],[217,168,50,14,'A합중국',CPP],[272,168,50,14,'C공화국',CPP],[337,168,25,14,'J국',CPP],[386,168,36,14,'K민국',CPP],[433,168,49,14,'N인민국',CPP],
 [50,188,54,10,'생산 턴',dict(CPP,font='pixel9',size=10,align='l')],[145,185,34,13,'작전명',dict(CPP,gstart=1)],[181,185,36,13,'부대 수',dict(CPP,gstart=1)],
 [51,198,45,11,'R공화국',dict(CPP,font='pixel9',size=10,align='l',dy=1)],[106,198,39,10,'C공화국',dict(CPP,font='pixel9',size=10)],[144,198,38,10,'N인민국',dict(CPP,font='pixel9',size=10)],
 [347,203,46,10,'와일드기스',dict(CPP,font='pixel9',size=10)],[489,0,22,10,'J국',dict(CPP,font='pixel9',size=10)],
 [277,181,70,13,'점령 건물 수',dict(CPP,align='l')],[347,181,60,13,'총 건물 수',dict(CPP,align='l')],[408,181,76,13,'중립 건물 수',CPP],
]
WT=dict(font='pixel',ix={'bg':239,'fill':255,'ramp':True},size=12)
WL=dict(font='pixel',ix={'bg':12,'fill':246,'ramp':True},size=12,align='r')
def split(x0,x1,y,h,words,st):
    n=sum(c for _,c in words); out=[]; x=x0
    for t,c in words:
        w=round((x1-x0)*c/n); out.append([x,y,w,h,t,st]); x+=w
    return out
SPEC[('UI/tex_wib.ofs','book_image/UI_wib01.gim')]=(
 split(50,290,53,14,[('전투기',3),('전투공격기',5),('공격기',3),('폭격기',3),('정찰기',3)],WT)+
 split(288,498,65,14,[('공격 헬기',4),('수송 헬기',4),('주력 전차',4),('자주포',3)],WT)+
 split(16,282,69,14,[('보병',2),('전투차',3),('병원 수송차',5),('전차 구축차',5),('대공 차량',4)],WT)+
 split(16,272,84,14,[('수송 차량',4),('보급차',3),('전투 공병',4),('대지 미사일 차량',8)],WT)+
 split(278,502,83,14,[('자주 로켓포',7),('대공 미사일 차량',8),('보병',2)],WT)+
 split(17,241,101,14,[('일본',2),('미국',4),('러시아',3),('중국',2),('독일',3),('한국',2)],WT)+
 split(241,347,111,13,[('북한',3),('불명',2),('전체',2)],WT)+
 [[334,96,66,15,'병기 타입',dict(WT,font='bold',size=13)],[454,96,34,15,'국명',dict(WT,font='bold',size=13)],
  [264,96,68,14,'카테고리:',WL],[402,96,50,14,'병기명:',WL],[400,112,42,14,'전장:',WL],
  [66,124,44,14,'전폭:',WL],[134,124,70,14,'탄체 직경:',WL],[258,134,44,14,'전고:',WL],[352,134,46,14,'중량:',WL],[422,134,72,14,'최고 속도:',WL],
  [40,138,70,14,'항속 거리:',WL],[134,138,70,14,'탑재 연료:',WL],[206,148,96,14,'최대 상승 고도:',WL],[352,148,46,12,'추력:',WL],[448,148,46,12,'출력:',WL],
  [26,152,84,14,'메인 로터:',WL],[160,152,44,14,'주포:',WL],[232,162,70,14,'최대 사정:',WL]])
