from database_handler import *
from note_user_info import *
from xhs_spider.webpage_scraper import *
from utils import *
import re
import os


def get_and_write(url):

    # 得到网页信息
    headers = get_headers()
    html = get_html(url, headers).replace(" ", "")
    random_sleep()

    # 抽取结构化信息
    data_dic = {"url": url}
    user_string = ""
    note_string = ""
    try:
        print(url)
        user_string = re.findall('"user":{.*?}', html)[1]
        note_string = re.findall('<script>window.__INITIAL_STATE__={(.*)}', html)[0]
        data_dic.update(get_user_info(user_string))
        data_dic.update(get_note_info(note_string))
        # 存入数据库
        db = init_database()
        save_to_database(db, data_dic, url)
    except:
        error_path = "./错误路径html/"
        if not os.path.exists(error_path):
            os.mkdir(error_path)
        txt_name = url.split("/")[-1]
        with open(error_path+txt_name+".txt", "a", encoding="utf-8") as file:
            file.writelines(user_string)
            file.writelines(note_string)


