import requests
import os
import re

def main():
    print('input Qiita access token')
    access_token = input('>>> ')

    print('input Qiita user name')
    user_name = input('>>> ')

    params = {'page': 1,'per_page': 100,'query': 'user:{}'.format(user_name)}
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    api = "https://qiita.com/api/v2/items"

    req = requests.get(api, params=params, headers=headers)

    res = req.json()
    user = res[0]["user"]

    print('user_id: {}, items_count: {} \n'.format(user["id"], user["items_count"]))

    items_count = user["items_count"]
    cnt = 1
    article_list = list()

    for i in res:
        print('{}, {}'.format(cnt, i["title"]))
        article_list.append({"title": i["title"], "url": i["url"]+".md"})
        cnt += 1

    if items_count <= 100:
        # print(article_list)
        save_article(article_list)
        return

    time = int(user["items_count"] / 100)

    for t in range(time):
        params = {'page': t+2,'per_page': 100,'query': 'user:{}'.format(user_name)}
        req = requests.get(api, params=params, headers=headers)

        res = req.json()

        for i in res:
            print('{}, {}'.format(cnt, i["title"]))
            article_list.append({"title": i["title"], "url": i["url"]+".md"})
            cnt += 1

    # print(article_list)
    save_article(article_list)

def save_article(article_list):
    os.makedirs('./md', exist_ok=True)

    for i in article_list:
        req = requests.get(i["url"])
        title = re.sub(r'[\\/:*?"<>|]+','',i["title"])

        RED = '\033[31m'
        CYAN = '\033[36m'
        END = '\033[0m'

        try:
            with open(f'./md/{title}.md', 'w', encoding='UTF-8', errors="ignore") as f:
                f.write(req.text)
        except:
            print(RED+f'title: {title}, url: {i["url"]} が保存できませんでした。'+END)

    print(CYAN+'All done!'+END)

if __name__ == "__main__":
    main()