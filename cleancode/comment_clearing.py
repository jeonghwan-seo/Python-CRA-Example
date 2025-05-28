# Copyright (C) emilybache, Inc. All right reserved.
# https://github.com/emilybache/GildedRose-Refactoring-Kata

# History
# ----------------------------
# 230910 : 판매 기한 조건 추가
# 230101 : 새로운 아이템 추가
# 220104 : 신규 코드 작성

class GildedRose(object):

    # 생성자
    def __init__(self, items):
        self.items = items

    # 가격 업데이트 함수
    def update_quality(self):
        # for 문을 돌면서  items 배열의 각 item 들 가격을 업데이트한다.
        for item in self.items:
            # 만약 Aged Brie, Backstage Pass 가 아닌 다른 아이템이라면
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                # if
                # 가격이 매겨져 있을 경우, 가격을 1 낮춘다. (단, Sulfuras 제외)
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            # end if
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1

                    # 콘서트 티켓은 판매기한이 0에 수렴할수록 가격이 증가한다.
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1  # 판매기한 <= 10일 + 최대가격은 50
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1  # 판매기한 <= 5일 + 최대가격은 50

                # end if
            # end else

            #=========================== 버그 발생 방지 =============================
            # Sulfuras 가 아닌 아이템들은 판매기한이 1씩 줄여주고 그 이후 코드들을 실행해야한다.
            # by inho.choi
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            #=======================================================================

            # 판매기한 음수일 경우 처리
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                # end if
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                # end else
                # if item.name == "Sufuras, Hand of Ragnaros":
                #     item.quality = item.quality + 1

class Item:
    # 생성자
    def __init__(self, name, sell_in, quality):
        self.name = name  # 이름
        self.sell_in = sell_in  # 판매 기한
        self.quality = quality  # 가격

    # 이름, 판매 기한, 가격을 출력 한다.
    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
