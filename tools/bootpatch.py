import os,re,sys
T={'大戦略ポータブル':'대전략 포터블','シナリオ名：%s'+chr(10)+'出現マップ数：%d'+chr(10)+'クリアミッション数：%d'+chr(10)+'生産可能ユニット数：%d':'시나리오명：%s'+chr(10)+'등장 맵 수：%d'+chr(10)+'클리어 미션 수：%d'+chr(10)+'생산 가능 유닛 수：%d','大戦略ポータブルセーブデータ':'대전략 포터블 세이브 데이터','新規作成データ':'신규 작성 데이터',
'暴発の代償':'폭발의 대가','首都攻防':'수도 공방','カウンターアタック':'카운터어택','不協和音':'불협화음','孤　島':'고　도','列島侵攻':'열도 침공',
'背後からの一刺し':'등 뒤의 일격','民族団結':'민족 단결','復讐の残響':'복수의 잔향','西南西に針路をとれ':'서남서로 침로를',
'ライライ赤い巨人':'라이라이 붉은거인','戦火の平和都市':'전화속 평화도시','列島震撼':'열도 진감','内海の戦い':'내해의 싸움',
'桜　舞　　－列島奪還Ⅰ－':'벚꽃 춤－열도 탈환Ⅰ－','桜　舞　　－列島奪還Ⅱ－':'벚꽃 춤－열도 탈환Ⅱ－','熱砂と硝煙':'열사와 초연',
'深夜の遭遇戦':'심야의 조우전','砂塵の墓標':'사진의 묘표','反撃の狼煙':'반격의 봉화','半島上陸作戦':'반도 상륙작전','太陽の牙':'태양의 엄니',
'東の鷹作戦発動Ⅰ':'동쪽 매 작전Ⅰ','東の鷹作戦発動Ⅱ':'동쪽 매 작전Ⅱ','首都奪還Ⅰ':'수도 탈환Ⅰ','首都奪還Ⅱ':'수도 탈환Ⅱ',
'熱　河　　終焉の始まり':'열하　종언의 시작','北の盟友':'북쪽의 맹우','蟻と巨人たち':'개미와 거인','北の旋風':'북쪽의 선풍',
'一握りの永遠':'한줌의 영원','滅びの呪文　－独裁の結末－':'멸망의 주문－독재의 결말－'}
def patch(b):
    b=bytearray(b); base=0x98500; seg=bytes(b[base:0x98a40])
    for m in re.finditer(rb'[^\x00]+',seg):
        try: t=m.group().decode('utf8')
        except: continue
        if t not in T: continue
        st=base+m.start(); end=st+len(m.group())
        room=end
        while b[room]==0 and room<len(b): room+=1
        room=room-st-1
        ko=T[t].encode('utf8')
        if len(ko)>room: ko=T[t].replace(' ','').encode('utf8')
        if len(ko)>room:
            print('too long %s %d>%d'%(T[t],len(ko),room)); continue
        b[st:st+room]=ko+b'\0'*(room-len(ko))
    t='大戦略ポータブル'.encode('utf8')
    if b[0x98574:0x98574+len(t)]==t:
        ko='대전략 포터블'.encode('utf8'); b[0x98574:0x98574+len(t)+1]=ko+b'\0'*(len(t)+1-len(ko))
    return bytes(b)
def build(W):
    b=patch(open(W('work','ext','PSP_GAME','SYSDIR','BOOT.BIN'),'rb').read())
    import struct
    sf=bytearray(open(W('work','ext','PSP_GAME','PARAM.SFO'),'rb').read())
    kt,dt,n=struct.unpack_from('<III',sf,8)
    for i in range(n):
        ko,fmt,ln,mx,do=struct.unpack_from('<HHIII',sf,20+16*i)
        if sf[kt+ko:kt+ko+6]==b'TITLE\0':
            t='대전략 포터블'.encode('utf8')+b'\0'
            sf[dt+do:dt+do+mx]=t+b'\0'*(mx-len(t)); struct.pack_into('<I',sf,20+16*i+4,len(t))
    return {'PSP_GAME/SYSDIR/BOOT.BIN':b,'PSP_GAME/SYSDIR/EBOOT.BIN':b,'PSP_GAME/PARAM.SFO':bytes(sf)}
if __name__=='__main__':
    patch(open(sys.argv[1],'rb').read()); print('ok')
