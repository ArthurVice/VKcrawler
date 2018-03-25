# VK crawler

A Python crawler uses VK API to crawling fan page's public posts, comments, and likes.

## How does it work?

Using **VK API**

## Requirement

**VK** module is a must

Please make sure that you have already install module **VK**.

If not, you can use **pip** to install:
```
pip install vk
```

## How to use?

**VK crawler** require **one** parameter(by now):

1. **Domain**: The page name you want to crawl.

And **Three** additional parameters(Set by default in main.py):

1. **Count**: Count of post you will crawl. Default is **100**. Seems to be **100** is max.
2. **Filter**: Determines what types of records on the wall you need to get. Default is **all**.
3. **Extended**: The response will return additional fields profiles and groups containing information about users and communities. Default: 1.
```
Third parameter is useless by now. Specified for future occurrences.

### Example usage

```
python main.py
>>>Enter a page name:

```

## About token

This crawler use **app_id**, **user_login**, **user_password** , to get the token.

Replace **app_id**, **user_login**, **user_password** to use your own app setting.
