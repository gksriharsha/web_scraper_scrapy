import scrapy


class TwitterSpider(scrapy.Spider):
    name = 'twitter'

    start_urls = [
            'https://twitter.com/search?q=%23comedy&src=typed_query&f=top',
            ]

    def parse(self, response, **kwargs):
        for tweet in response.css('.css-1dbjc4n'):
            try:
                awards = len(tweet.css(''))
            except:
                awards = 0
            yield {
                'tweet': tweet.css('._eYtD2XCVieq6emjKBH3m::text').get(),
                're-tweets': tweet.css('._1rZYMD_4xY3gRcSS3p8ODO._3a2ZHWaih05DgAOtvu6cIo::text').get(),
                'comments':tweet.css('.r-qvutc0::text').get(),
                'user':tweet.css('_2tbHP6ZydRpjI44J3syuqC').get(),
                'recent': tweet.css('._2VF2J19pUIMSLJFky-7PEI::text').get()
                }