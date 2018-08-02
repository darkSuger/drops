#!/usr/bin/python
# coding:utf-8

import requests


test_url = 'http://movie.douban.com/top250/'


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data


def main():
    handle = download_page(test_url)
    print(handle)


main()
