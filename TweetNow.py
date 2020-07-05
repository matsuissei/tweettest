from requests_oauthlib import OAuth1Session
from http import HTTPStatus
from datetime import datetime

def post_tweet(body):
    # 認証処理
    twitter = OAuth1Session(
       "VrUPoKTmpGOsvVHUhmP2glmtj","ggWDIgzaGVrJwwuMDnETY6fg1bMEhFXlZ0jzuLIc4UFXjxAwFN","1279071919942189056-eSXDnD37q34QltSnsDnEf3BVF3Bplk","35IusNFUK6KNmedj3hFEpjCueY4LWoRrHlhpvZM3Kv40X"
    )
    # ツイート処理
    res = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params={"status": body})
    print(res)

    # エラー処理
    if res.status_code == HTTPStatus.OK:
        print("Successfuly posted")
    else:
        print(f"Failed: {res.status_code}")

def main():
    # body = "テスト投稿2"
    now = datetime.now()
    post_tweet(now)


if __name__ == '__main__':
    main()