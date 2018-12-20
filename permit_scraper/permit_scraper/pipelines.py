# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .spiders import PermitDB

class PermitScraperPipeline(object):

    def __init__(self):
        self.session = PermitDB.get_session()

    def process_item(self, item, spider):
        try:
            self.session.bulk_save_objects(spider)
            self.session.commit()

        except MySQLdb.Error as e:
            print ("Error %d: %s" % (e.args[0], e.args[1]))
        return item
