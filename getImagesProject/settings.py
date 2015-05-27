# -*- coding: utf-8 -*-

# Scrapy settings for getImagesProject project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'getImagesProject'

SPIDER_MODULES = ['getImagesProject.spiders']
NEWSPIDER_MODULE = 'getImagesProject.spiders'
IMAGES_STORE = '/home/keeda/new/'
ITEM_PIPELINES = {'getImagesProject.pipelines.GetimagesprojectPipeline': 1}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'getImagesProject (+http://www.yourdomain.com)'
