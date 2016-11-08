#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import redis

ONE_WEEK_IN_SECONDS = 7 * 86400
VOTE_SCORE = 432
pool = redis.ConnectionPool(host='192.168.1.10', port=6379)
client = redis.Redis(connection_pool=pool)


def post_article(conn, user, title, link):
    article_id = str(conn.incr('article:'))
    voted = 'voted:' + article_id
    conn.sadd(voted, user)
    conn.expire(voted, ONE_WEEK_IN_SECONDS)
    now = time.time()
    article = 'article:' + article_id
    conn.hmset(article, {
        'title': title,
        'link': link,
        'poster': user,
        'time': now,
        'votes': 1,
    })
    conn.zadd('score:', article, now + VOTE_SCORE)
    conn.zadd('time:', article, now)
    return article_id


def article_vote(conn, user, article):
    cutoff = time.time() - ONE_WEEK_IN_SECONDS
    if conn.zscore('time:', article) < cutoff:
        return

    article_id = article.partition(':')[-1]
    if conn.sadd('voted:' + article_id, user):
        conn.zincrby('score:', article, VOTE_SCORE)
        conn.hincrby(article, 'votes', 1)


# post_article(client, "renhuan", "my home", "http://www.baidu.com")
article_vote(client, "renhuan", "my home")
