import requests
import json
import datetime
import os
import sys
import time
from bs4 import BeautifulSoup


# 选择要抓取的房间
def SelectRoom():
    print("\n请输入序号以选择要抓取的房间:")
    print("1.灌水\t2.动漫\t3.游戏\t4.欧美")
    print("5.原神\t6.aph\t7.文野\t8.狂飙")
    print("9.星穹\t10.日娱\t11.历史\t12.乘风破浪的姐姐")

    number = input()

    if number == '1':
        print("\n已选择灌水专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 灌水主页的roomid
            Guanshui_roomid = '551e51f8fbe78e6c02be1d89'
            return Guanshui_roomid
        elif number == '2':
            # 灌水水区的subroomid
            Guanshui_subroomid = '57a75577a508c960d3cb7b3a'
            return Guanshui_subroomid

    elif number == '2':
        print("\n已选择动漫专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 动漫主页的roomid
            Dongman_roomid = '551e521afbe78e6c02be1d8a'
            return Dongman_roomid
        elif number == '2':
            # 动漫水区的subroomid
            Dongman_subroomid = '59702a3bfa1eb084c2d27c40'
            return Dongman_subroomid
    elif number == '3':
        print("\n已选择游戏专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 游戏主页的roomid
            Youxi_roomid = '55a8ba62fbe78e0577201b2e'
            return Youxi_roomid
        elif number == '2':
            # 游戏水区的subroomid
            Youxi_subroomid = '57cd3638d92cc5794ae3c3dd'
            return Youxi_subroomid
    elif number == '4':
        print("\n已选择欧美专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 欧美主页的roomid
            Oumei_roomid = '552b5aecfbe78e6853e442af'
            return Oumei_roomid
        elif number == '2':
            # 欧美水区的subroomid
            Oumei_subroomid = '5693462afbe78e2538159b61'
            return Oumei_subroomid
    elif number == '5':
        print("\n已选择原神专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 原神主页的roomid
            Yuanshen_roomid = '606589c2dc32c2eb0ec99955'
            return Yuanshen_roomid
        elif number == '2':
            # 原神水区的subroomid
            Yuanshen_subroomid = '606589c20de2d061ee2f9805'
            return Yuanshen_subroomid
    elif number == '6':
        print("\n已选择aph专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # aph主页的roomid
            aph_roomid = '5528ec8afbe78e4938139f65'
            return aph_roomid
        elif number == '2':
            # aph水区的subroomid
            aph_subroomid = '59ef4da6e3d24c4791231b2d'
            return aph_subroomid
    elif number == '7':
        print("\n已选择文野专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 文野主页的roomid
            Wenyi_roomid = '56b9d32afbe78e2d8eaed6ff'
            return Wenyi_roomid
        elif number == '2':
            # 文野水区的subroomid
            Wenyi_subroomid = '56bc8bfefbe78e50c60ab267'
            return Wenyi_subroomid
    elif number == '8':
        print("\n已选择狂飙专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 狂飙主页的roomid
            Kuangbiao_roomid = '63ec477f5fbd2b4494193921'
            return Kuangbiao_roomid
        elif number == '2':
            # 狂飙水区的subroomid
            Kuangbiao_subroomid = '63ec477f0de2d061eede7b72'
            return Kuangbiao_subroomid
    elif number == '9':
        print("\n已选择星穹专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 星穹主页的roomid
            Xingqiong_roomid = '6454a97fde30c142ef7e21f7'
            return Xingqiong_roomid
        elif number == '2':
            # 星穹水区的subroomid
            Xingqiong_subroomid = '6454a97fde30c142ef7e221c'
            return Xingqiong_subroomid
    elif number == '10':
        print("\n已选择日娱专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 日娱主页的roomid
            Riyu_roomid = '56cd2ce0fbe78e12938f115a'
            return Riyu_roomid
        elif number == '2':
            # 日娱水区的subroomid
            Riyu_subroomid = '56da5a9efbe78e3333cb2137'
            return Riyu_subroomid
    elif number == '11':
        print("\n已选择历史专区。")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 历史主页的roomid
            Lishi_roomid = '5523e9dcfbe78e51742b25a2'
            return Lishi_roomid
        elif number == '2':
            # 历史水区的subroomid
            Lishi_subroomid = '56ed72b2fbe78e533373777d'
            return Lishi_subroomid
    elif number == '12':
        print("\n已选择乘风破浪的姐姐专区")
        print("1.主页\t2.水区:")
        number = input()
        if number == '1':
            # 乘风破浪的姐姐主页的roomid
            Chengfeng_roomid = '5ee98c199075f3395ef6f1c7'
            return Chengfeng_roomid
        elif number == '2':
            # 乘风破浪的姐姐水区的subroomid
            Chengfeng_subroomid = '5ee98c194ead61ceda497545'
            return Chengfeng_subroomid

    print("\n不存在的专区，程序中止。")


def Login():
    print("\n请输入帐号绑定的手机号:")
    phone = input()
    print("\n请输入密码:")
    password = input()
    return 'http://www.mrpyq.com/api/account/login?phone=' + phone + '&password=' + password, phone, password


def getAccessToken(login_url, phone, password):
    """@return access_token"""
    # 模拟登录获取会话
    session = requests.Session()

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Host": "www.mrpyq.com",
        "Origin": "http://web.mrpyq.com",
        "Proxy-Connection": "keep-alive",
        "Referer": "http://web.mrpyq.com/",
    }
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"

    # 构造登录请求的表单数据
    login_data = {
        'phone': phone,  # 替换为你的手机号码
        'password': password  # 替换为你的登录密码
    }

    # 发送登录请求
    response = session.post(login_url, headers=headers, data=login_data)
    # 检查登录是否成功
    if response.status_code == 200:
        # print(response.json())
        token = response.json()["access_token"]
        return token
    else:
        print('登录失败')
        return None


def getKeywords():
    keywords = []
    # 用户输入关键词，以回车分隔，若监测到输入为空，则结束
    print("\n注意：关键词不要太长，否则可能会出现抓取不到的情况。最多输入200个关键词。")
    print("请输入要搜索关键词，以回车分隔。再按一次回车则结束关键词输入:")
    while True:
        keyword = input()
        if keyword == '':
            break
        else:
            keywords.append(keyword)
            if len(keywords) == 200:
                break
    return keywords


def getWatingTime():
    print("\n请输入抓取间隔时间(秒), 至少20秒:")
    # 为了保护服务器，硬性设置间隔至少20秒抓取一次，否则重新输入
    while True:
        t = input()
        if t.isdigit() and int(t) >= 20:
            return int(t)
        else:
            print("请重新输入抓取间隔时间(秒):")


def main():
    # 登录
    login_url, phone, password = Login()
    access_token = getAccessToken(login_url, phone, password)

    # 检查登录是否成功
    while access_token is None:
        print("\n登录失败，请重新登录。")
        login_url, phone, password = Login()
        access_token = getAccessToken(login_url, phone, password)
    print("\n登录成功。")

    keywords = getKeywords()
    waitingtime = getWatingTime()
    roomid = SelectRoom()
    # print(access_token)
    # 检查登录是否成功
    if access_token:
        t_a = 1
        t_b = 1
        while True:

            # url = 'http://www.mrpyq.com/api/feed/feeds_by_room?access_token= {tokennumber} &page=1&t=1688783232199&roomid=55a8ba62fbe78e0577201b2e'
            main = 'http://www.mrpyq.com/api/feed/feeds_by_room?'

        
            page = 1

            # 获取当前时间
            current_time = datetime.datetime.now()
            # 将时间格式化为所需的日期和时间格式
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            # 将格式化后的时间转换为时间戳
            t = int(
                time.mktime(time.strptime(formatted_time,
                                          "%Y-%m-%d %H:%M:%S"))) * 1000

            print("\n正在抓取中……请耐心等待……")
            # 要修改roomid/subroomid
            url = main + 'access_token=' + access_token + '&page=' + str(
                page) + '&t=' + str(t) + '&subroomid=' + roomid

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                # print(data)
                # Extract "name", "content", and "no" values
                names = []
                contents = []
                nos = []
                tamestamps = []

                items = data.get('items', [])
                # print(items)
                for item in items:
                    name = item.get('user', {}).get('name')
                    content = item.get('content')
                    no = item.get('no')
                    # {'create': 1688793477838}
                    timestamp = item.get('time', {}).get('create')

                    names.append(name)
                    contents.append(content)
                    nos.append(no)
                    tamestamps.append(timestamp)

                # Pair and output the values
                for name, content, no, timestamp in zip(
                        names, contents, nos, tamestamps):
                    print("Time:", timestamp)
                    print("Name:", name + " " + str(no))
                    print("Content:", content)
                    print("---")
            else:
                print('\n请求失败!')

            # 获取可执行文件所在的路径
            # pyinstaller 之后的 exe 文件所在地址，如果直接运行py文件则将exe_dir替换成current_dir = os.path.dirname(os.path.abspath(__file__))
            exe_dir = os.path.dirname(sys.executable)

            # 构建文件路径
            file_path = os.path.join(exe_dir, '所有帖子.txt')

            # 打开文件并进行操作
            with open(file_path, 'a', encoding='utf-8') as f:  # 使用uft-8编码格式
                # 逆序遍历
                for name, content, no, timestamp in zip(
                        names[::-1], contents[::-1], nos[::-1],
                        tamestamps[::-1]):
                    # 检查时间戳
                    if timestamp > t_a:
                        t_a = timestamp
                        timestamp = timestamp / 1000  # 将毫秒转换为秒
                        timestamp = datetime.datetime.fromtimestamp(timestamp)
                        f.write("Time:" + str(timestamp) + '\n')
                        f.write("Name:" + name + " " + str(no) + '\n')
                        if content != None:
                            f.write("Content:" + content + '\n')
                        f.write("---" + '\n')

            file_path = os.path.join(exe_dir, '关键词相关帖子.txt')

            # 打开文件并进行操作
            with open(file_path, 'a', encoding='utf-8') as f:
                # 逆序遍历
                for name, content, no, timestamp in zip(
                        names[::-1], contents[::-1], nos[::-1],
                        tamestamps[::-1]):

                    # 检查时间戳
                    if timestamp > t_b:
                        t_b = timestamp
                        timestamp = timestamp / 1000  # 将毫秒转换为秒
                        timestamp = datetime.datetime.fromtimestamp(timestamp)
                        # 如果name和content中包含keywords中的任意一个关键词，则写入txt文件
                        if any(keyword in name for keyword in keywords) or any(
                                keyword in content for keyword in keywords):
                            f.write("Time:" + str(timestamp) + '\n')
                            f.write("Name:" + name + " " + str(no) + '\n')
                            if content != None:
                                f.write("Content:" + content + '\n')
                            f.write("---" + '\n')

            print("\n抓取完成！等待" + str(waitingtime) + "秒后继续抓取……")
            print("按Ctrl+C可随时退出程序。")
            time.sleep(waitingtime)


if __name__ == '__main__':
    main()
