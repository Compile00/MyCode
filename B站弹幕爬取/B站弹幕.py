import requests
import json
import re
from wordcloud import WordCloud


# 用BV号得到cid号
def get_cid(bv):
    bv = bv.strip('BV1')
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp'
    res = requests.get(url)
    res_text = res.text
    res_dict = json.loads(res_text)
    cid = res_dict['data'][0]['cid']
    return cid


# https://www.bilibili.com/video/BV1mM4y1K7gC?share_source=copy_web

# 用cid号获取弹幕
def get_bullet_chat(cid):
    url = f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}'
    res = requests.get(url)
    res.xml = res.content.decode('utf-8')
    patt = re.compile('<d.*?>(.*?)</d>')
    bullet_list = patt.findall(res.xml)
    return bullet_list

def save_txt(cid):
    danmu_list = get_bullet_chat(cid)  # 获得弹幕列表
    print("保存中......")
    with open("弹幕生成.txt", 'w', encoding='utf-8') as f:
        for line in danmu_list:
            f.write(line + '\n')
    print("保存成功！文件已保存到当前工作目录下。")
    # print("*" * separator_len) # separator = '*'*60

# 生成词云
def wold_could(bullent):
    bullent = str(bullent)  # 因为获取的弹幕是list，但是词云得是str类型
    wold_could_png = WordCloud(font_path='msyh.ttc').generate(bullent)
    wold_could_png.to_file('弹幕.png')


if __name__ == '__main__':
    bv = 'BV1CP4y147NU'
    cid = get_cid(bv)
    save_txt(cid)
    bullent = get_bullet_chat(cid)
    wold_could(bullent)
