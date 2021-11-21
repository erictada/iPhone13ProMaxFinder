# This Python file uses the following encoding: utf-8

import os

def check_availability_base(s, model, shop):
    PRODUCT_RED = s.split('スターライト')[0]
    check_color_base(model, PRODUCT_RED, '(PRODUCT)RED', shop)

    starlight = (s.split('スターライト')[1]).split('ミッドナイト')[0]
    check_color_base(model, starlight, 'Starlight', shop)

    midnight = (s.split('ミッドナイト')[1]).split('ブルー')[0]
    check_color_base(model, midnight, 'Midnight', shop)

    blue = (s.split('ブルー')[1]).split('ピンク')[0]
    check_color_base(model, blue, 'Blue', shop)

    pink = s.split('ピンク')[1]
    check_color_base(model, pink, 'Pink', shop)

def check_color_base(model, s, color, shop):
    storage = ['128 GB', '256 GB', '512 GB']
    index = 0
    for i in range(len(s)):
        if s[i] == '予':
            index += 1
        elif s[i] == '有':
            print('{:<30s}{:<30s}{:<30s}{:<30s}'.format(model,color,storage[index],shop))
            index += 1

def check_availability_pro(s, model, shop):
    graphite = s.split('ゴールド')[0]
    check_color_pro(model, graphite, 'Graphite', shop)

    gold = (s.split('ゴールド')[1]).split('シルバー')[0]
    check_color_pro(model, gold, 'Gold', shop)

    silver = (s.split('シルバー')[1]).split('シエラブルー')[0]
    check_color_pro(model, silver, 'Silver', shop)

    blue = s.split('シエラブルー')[1]
    check_color_pro(model, blue, 'Sierra Blue', shop)


def check_color_pro(model, s, color, shop):
    storage = ['128 GB', '256 GB', '512 GB', '1 TB']
    index = 0
    for i in range(len(s)):
        if s[i] == '予':
            index += 1
        elif s[i] == '有':
            print('{:<30s}{:<30s}{:<30s}{:<30s}'.format(model,color,storage[index],shop))
            index += 1
            

#Clear screen
os.system('clear')

#Create list of shops:
shop_name = []
shop_name.append('有楽町店')
shop_name.append('池袋本店')
shop_name.append('赤坂見附駅店')
shop_name.append('新宿西口店')
shop_name.append('ビックロ 新宿東口店')
shop_name.append('新宿東口駅前店')
shop_name.append('渋谷東口店別館')
shop_name.append('AKIBA')
shop_name.append('立川店')
shop_name.append('JR八王子駅店')
shop_name.append('京王調布店')
shop_name.append('町田店')
shop_name.append('ラゾーナ川崎店')
shop_name.append('横浜西口店')
shop_name.append('新横浜店')
shop_name.append('イトーヨーカドーたまプラーザ店')
shop_name.append('藤沢店')
shop_name.append('相模大野駅店')
shop_name.append('柏店')
shop_name.append('船橋東武店')
shop_name.append('大宮西口そごう店')
shop_name.append('高崎東口店')
shop_name.append('水戸駅店')

#Shop nums to find URL
shop_num = ['14','7','117','16','116','111','8','121','12','114','122','124','38','5','104','126','37','108','35','123','34','127','91','115']

import time

#Download pages for each shop
import urllib.request

#Query user for which models to search
search_iPhone13_Mini = True if (input('Search for: iPhone 13 Mini? (Y or N) ')).lower() == 'y' else False
search_iPhone13 = True if (input('Search for: iPhone 13? (Y or N) ')).lower() == 'y' else False
search_iPhone13_Pro = True if (input('Search for: iPhone 13 Pro? (Y or N) ')).lower() == 'y' else False
search_iPhone13_Pro_Max = True if (input('Search for: iPhone 13 Pro Max? (Y or N) ')).lower() == 'y' else False

if not search_iPhone13_Mini and not search_iPhone13 and not search_iPhone13_Pro and not search_iPhone13_Pro_Max:
    print("Go look for a Xiaomi then!")
    quit()

finish = 0
while finish == 0:

    #Print time
    print("")
    print("-------------------------------------------------------------------------")
    print("Time as of search start: {}".format(time.ctime()))
    print("")

    #Print header
    print('{:<30s}{:<30s}{:<30s}{:<30s}'.format("Model","Color","Storage","Shop"))
    print("")

    for i in range(len(shop_num)):
        
            
        top_url = 'https://www.biccamera.com/bc/c/service/iphone_online/shopstock/index.jsp'
        shop_url = 'https://www.biccamera.com/bc/c/service/iphone_online/shopstock/shop.jsp?shop_num=' + shop_num[i]

        dummy = urllib.request.urlopen(shop_url)
        dummy.close()

        fp = urllib.request.urlopen(shop_url)
        mybytes = fp.read()

        try:
            mystr = mybytes.decode("shift_jis")
        except BaseException:
            fp.close()
            time.sleep(60)

            fp = urllib.request.urlopen(shop_url)
            mybytes = fp.read()
            mystr = mybytes.decode("shift_jis")


        fp.close()

        #Extract Rakuten Mobile info
        bef_str = '<h3 class="rakuten_inner_ttl">iPhone 13 mini　在庫状況</h3>'
        aft_str = '<li>在庫表示は目安です。</li>'

        rakuten_mobile = (mystr.split(bef_str))[1].split(aft_str)[0]

        #Check availability for each model

        #iPhone 13 Mini
        if search_iPhone13_Mini:
            aft_str = '<h3 class="楽天モバイル_inner_ttl">iPhone 13 在庫状況</h3>'
            iPhone13_mini = rakuten_mobile.split(aft_str)[0]
            check_availability_base(iPhone13_mini, 'iPhone13 mini', shop_name[i])

        #iPhone 13
        if search_iPhone13:
            bef_str = '<h3 class="楽天モバイル_inner_ttl">iPhone 13 在庫状況</h3>'
            aft_str = '<h3 class="楽天モバイル_inner_ttl">iPhone 13 Pro 在庫状況</h3>'
            iPhone13 = (rakuten_mobile.split(bef_str))[1].split(aft_str)[0]
            check_availability_base(iPhone13, 'iPhone13', shop_name[i])

        #iPhone 13 Pro
        if search_iPhone13_Pro:
            bef_str = '<h3 class="楽天モバイル_inner_ttl">iPhone 13 Pro 在庫状況</h3>'
            aft_str = '<h3 class="楽天モバイル_inner_ttl">iPhone 13 Pro Max 在庫状況</h3>'
            iPhone13_Pro = (rakuten_mobile.split(bef_str))[1].split(aft_str)[0]
            check_availability_pro(iPhone13_Pro, 'iPhone13 Pro', shop_name[i])

        #iPhone 13 Pro Max
        if search_iPhone13_Pro_Max:
            bef_str = '<h3 class="楽天モバイル_inner_ttl">iPhone 13 Pro Max 在庫状況</h3>'
            iPhone13_Pro_Max = rakuten_mobile.split(bef_str)[1]
            check_availability_pro(iPhone13_Pro_Max, 'iPhone13 Pro Max', shop_name[i])



