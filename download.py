"""
This sample is published as part of the blog article at www.toptal.com/blog.

Visit www.toptal.com/blog and subscribe to our newsletter to read great posts
"""

import logging
import os
import requests

logger = logging.getLogger(__name__)

types = {'image/jpeg', 'image/png'}


def get_links(client_id):
    """Get all of the links and return them in a list."""
    headers = {'Authorization': 'Client-ID {}'.format(client_id)}
    resp = requests.get(
        'https://api.imgur.com/3/gallery/random/random/', headers=headers)
    data = resp.json()
    return [item['link']
            for item in data['data']
            if ('type' in item) and (item['type'] in types)]


def download_link(directory, link):
    """GET link and store in directory."""
    download_path = os.path.join(directory, os.path.basename(link))
    resp = requests.get(link)
    with open(download_path, 'wb') as f:
        f.write(resp.content)
    logger.info('Downloaded %s', link)


def setup_download_dir():
    """"Create images directory if it doesn't exist and return it's path."""
    cur_dir = os.path.dirname(os.path.realpath(__file__))
    download_dir = os.path.join(cur_dir, 'images')
    if os.path.exists(download_dir):
        os.rmdir(download_dir)
    os.makedirs(download_dir)
    return download_dir
