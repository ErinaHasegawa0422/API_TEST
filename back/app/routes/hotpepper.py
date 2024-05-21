# routes/hotpepper.py

from fastapi import APIRouter, HTTPException 
from dotenv import load_dotenv
import requests
import os

load_dotenv(os.path.join(os.path.abspath(os.curdir), ".env"))
API_KEY = os.getenv("HOT_PEPPER_API_KEY")

# ルーティング
router = APIRouter()

# ホットペッパーAPIのエンドポイント
HOTPEPPER_URL = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
OUTPUT_FORMAT = "json"
RESPONSE_TARGET = "shop"

# 練馬駅の緯度と経度
LATITUDE = "35.735657"
LONGITUDE = "139.651259"
RANGE = "3" # 検索範囲を指定（1:300m, 2:500m, 3:1000m, 4:2000m, 5:3000m）

@router.get("/hotpepper")
def get_hotpepper_data():
    # パラメータの設定
    params = {
        "key": API_KEY,
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "range": RANGE, # 検索範囲の指定
        "format": OUTPUT_FORMAT,

    }
    
    try:
        # APIリクエストの実行
        response = requests.get(HOTPEPPER_URL, params=params)
        response.raise_for_status()

    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"APIリクエストに失敗しました: {e}")

    data = response.json()

    # データのバリデーション
    if "results" not in data or RESPONSE_TARGET not in data["results"]:
        raise HTTPException(status_code=500, detail="APIからの応答が不正です")

    # データを返す
    return data