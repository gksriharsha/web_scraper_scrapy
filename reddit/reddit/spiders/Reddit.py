import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'

    start_urls = [
            'https://www.reddit.com/r/funny',
            ]

    def parse(self, response, **kwargs):
        for post in response.css('._1oQyIsiPHYt6nx7VOmd1sz'):
            try:
                awards = len(post.css('._2OYwDdghtXEuTF67C95YLY'))
            except:
                awards = 0
            yield {
                'title': post.css('._eYtD2XCVieq6emjKBH3m::text').get(),
                'score': post.css('._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo::text').get(),
                'awards': awards,
                'comments':post.css('.FHCV02u6Cp2zYL0fhQPsO::text').get().strip(' comments'),
                'user':post.css('_2tbHP6ZydRpjI44J3syuqC').get(),
                'recent': post.css('._2VF2J19pUIMSLJFky-7PEI::text').get()
                }