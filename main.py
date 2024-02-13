from multiprocessing.dummy import Pool
from id_list_cursor import *
from join_function import *


if __name__ == "__main__":

    now_page_url = "https://www.xiaohongshu.com/web_api/sns/v3/page/notes?page_size=6&sort=time&page_id=5be6c322568677000137198d&cursor=&sid="
    has_more = True
    epoch = 0
    count = 0
    headers = get_headers()

    pool = Pool(4)

    while has_more:
        html_string = get_html(now_page_url, headers)
        list_url, cursor, has_more = get_id_and_cursor_value(html_string)
        count += (len(list_url))
        pool.map(get_and_write, list_url)

        print(f"当前第{epoch}轮，爬取{len(list_url)}，共爬取{count}")

        if has_more:
            now_page_url = "https://www.xiaohongshu.com/web_api/sns/v3/page/notes?page_size=6&sort=time&page_id=5be6c322568677000137198d&cursor=%s&sid=" % cursor
            print(f"当前cursor:{cursor}")
        else:
            pool.close()  # 关闭进程池
            break
