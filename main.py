import os

from client import Client


# TODO: こういうメソッド(他にも全件数取得とかも)はどこに実装するのがいいんだろう？
def get_max_page(response):
    return response.json["total_count"] // response.json["per_page"] + 1

def main():
    ESA_ACCESS_TOKEN = os.environ.get("ESA_ACCESS_TOKEN")
    ESA_TEAM_NAME = os.environ.get("ESA_TEAM_NAME")

    client = Client(access_token=ESA_ACCESS_TOKEN,
                    current_team=ESA_TEAM_NAME)

    # res1 = client.posts() # 単なるリクエスト
    res2 = client.posts(params={"page": 16}) # ページ指定
    max_page = get_max_page(res2)

    print(max_page)

if __name__ == "__main__":
    main()
