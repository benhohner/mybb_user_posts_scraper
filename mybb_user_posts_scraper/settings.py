# -*- coding: utf-8 -*-

# Scrapy settings for mybb_user_posts_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mybb_user_posts_scraper'

SPIDER_MODULES = ['mybb_user_posts_scraper.spiders']
NEWSPIDER_MODULE = 'mybb_user_posts_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'mybb_user_posts_scraper (+GCatQuill)'
DOWNLOAD_DELAY = 0.25    # 250 ms of delay
