import scrapy, urlparse
from scrapy.http import Request
from mybb_user_posts_scraper.items import Post, Author

class UserPostsSpider(scrapy.Spider):
    name = 'user_posts'
    allowed_domains = ['mydomain'] # domain of forums
    start_urls = ['mydomain.com/search.php?action=results&sid=da9aca997388a656f77fdf4fbf2add06&sortby=dateline&order=desc&uid=&page=%s' % page for page in xrange(1,12)] #url of search page and replace xrange with number of pages
    
    def parse(self, response):
        posts = response.css('a[href*="?pid"]::attr(href)').extract()
        
        for post in posts:
            split_url = urlparse.urlparse(response.url)
            yield Request(url="%s://%s/%s" % (split_url[0], split_url[1], post), callback=self.parse_post)
    
    def parse_post(self, response):
        post = Post()
        pid = urlparse.parse_qs(urlparse.urlparse(response.url)[4])['pid'][0]
        post['post_id'] = int(pid)
        post['title'] = response.css('#post_' + pid + ' table td > .smalltext:nth-child(2) strong::text').extract()[0]
        post['link'] = response.url + '#pid_' +pid
        post['text'] = response.css('#pid_' + pid).extract()[0]
        post['date_posted'] = response.css('#post_' + pid + ' td[class*=trow] > .smalltext:first-child::text').extract()[0]
        
        return post
