'''

scrapy shell https://quotes.toscrape.com/

response.css('title') =>[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]
response.css('title::text') => [<Selector xpath='descendant-or-self::title/text()' data='Quotes to Scrape'>]

response.css('title::text').get() #retorna apenas um elemento, pois só há um titulo
se usasse o gets receberia uma lista
'Quotes to Scrape'

quote = response.css('div.quote')[0]

In [11]: print(quote)
<Selector xpath="descendant-or-self::div[@class and contains(concat(' ', normalize-space(@class), ' '), ' quote ')]" data='<div class="quote" itemscope itemtype...'>

In [12]: quote.css('span.text::text')
Out[12]: [<Selector xpath="descendant-or-self::span[@class and contains(concat(' ', normalize-space(@class), ' '), ' text ')]/text()" data='“The world as we have created it is a...'>]

In [13]: quote.css('span.text::text').get()
Out[13]: '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'

In [14]: quote.css('small.author::text').get()
Out[14]: 'Albert Einstein'

In [16]: for quoteall in response.css('div.quote'):
    ...:     text = quoteall.css('span.text::text').get()
    ...:     autor = quoteall.css('small.author::text').get()
    ...:     print(text)
    ...:     print(autor)
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
Albert Einstein
“It is our choices, Harry, that show what we truly are, far more than our abilities.”
J.K. Rowling
“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”
Albert Einstein
“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”
Jane Austen
“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”
Marilyn Monroe
“Try not to become a man of success. Rather become a man of value.”
Albert Einstein
“It is better to be hated for what you are than to be loved for what you are not.”
André Gide
“I have not failed. I've just found 10,000 ways that won't work.”
Thomas A. Edison
“A woman is like a tea bag; you never know how strong it is until it's in hot water.”
Eleanor Roosevelt
“A day without sunshine is like, you know, night.”
Steve Martin

'''