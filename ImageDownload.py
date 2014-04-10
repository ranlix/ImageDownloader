# -*- coding: utf-8 -*-

import os
import sys
import re
import urllib

url_addr = sys.argv[1]
save_path = sys.argv[2]
# url_addr = r"http://www.douban.com/"
# save_path = r"C:\Users\naril\Desktop\new"
html = urllib.urlopen(url_addr).read()


class Get_Picture(object):
    def __init__(self, html_content):
        self.html_content = html_content

    def get_image_list(self):
        """Get all the image url from the website url,
        and return a list to save it."""
        image_list = []
        # print self.html_content
        pattern = r'<img.*?src="(.*\..{3})"/?>?'  # match the image with re
        match_result = re.findall(pattern, self.html_content)
        # print match_result
        for i in match_result:
            # url = url_addr + i  # ganerate the absolute address of picture
            image_list.append(i)
        # print image_list
        self.image_list = image_list
        return self.image_list

    def downloader(self):
        """Download all the images into some dir"""
        for each_url in self.image_list:
            filename = each_url.split("/")[-1]
            savedfile = os.path.join(save_path, filename)
            try:
                urllib.urlretrieve(each_url, savedfile)
            except:
                pass
        print "Downloading completed!"


def run():
    a = Get_Picture(html)
    a.get_image_list()
    a.downloader()

if __name__ == '__main__':
    run()
