#!/usr/bin/env python3

from article_models import ArticleInfo
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

app = FastAPI(title="Merketfy API",
              description="Here's our API to handle Web App data", version="1.0")


@app.on_event('startup')
async def connect_redis():
    pass


@app.on_event('shutdown')
async def disconnect_redis():
    pass


@app.post("/api/markets", summary="Information in all markets for a given Article",
          description="Endpoint that takes Article Information given by user in order to"
                      "see the Market fluent around it")
async def get_article_markets(article_info: ArticleInfo):
    """
        Endpoint that retrieves the entire info of an Article at Markets
        :param article_info: Class that represent the correct structure for Article Search on Markets
        :return: Output for Article Information
    """

    return JSONResponse("")


@app.post("/api/market/filtered", summary="Information in certain markets for a given Article",
          description="Endpoint that takes Article Information given by user in order to"
                      "see the Market fluent around it")
async def get_article_markets(article_info: ArticleInfo):
    """
        Endpoint that retrieves the entire info of an Article at Filtered Markets
        :param article_info: Class that represent the correct structure for Article Search on certain Markets
        :return: Output for Article Information
    """

    return JSONResponse("")


if __name__ == "__main__":
    uvicorn.run("merketfy_API:app", host="127.0.0.1", port=5000, log_level="info")
