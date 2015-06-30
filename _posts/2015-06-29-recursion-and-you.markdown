---
layout: post
title:  "Recursion and You"
date:   2015-06-29 12:00:00
comments: True
categories: update stack recursion
---

Recently, I started working on a personal project to crawl TvTropes,
essentially a casual wiki for discussing pop culture, make a graph of
those works which reference each other, and then calculate the "impact
factor" of each work in the same way as Google judges the quality of a
website by the people that link to it.

I had this as my first attempt at crawling TvTropes.

    {% highlight python %}
    
    from bs4 import BeautifulSoup
    from sets import Set

    import requests
    import sys

    tvtropes = "http://tvtropes.org"

    ls = Set([])

    def addLinks(links):
      '''Add the links to the set we've crawled and return
        the new ones.'''
      new = Set([])
      for link in links:
        if link not in ls:
          ls.add(link)
          print(link)
          new.add(link)
      return new

    def crawl(url):
      '''Crawl a website in depth first order and print out every
          page we find in it's domain.'''
      if url not in ls:
        links = getLinks(url)
        cont = addLinks(links)
        print(len(ls))
        for link in cont:
          crawl(cont)

    def getLinks(url):
      '''Use BeautifulSoup to scrape the page and filter the links on it
          for certain things we know we don't want to crawl.'''
      r  = requests.get(tvtropes)
      data = r.text
      soup = BeautifulSoup(data)
      links = [link.get('href') for link in soup.find_all('a')]
      links = [link for link in links if 'mailto' not in link]
      links = [link for link in links if 'javascript' not in link]
      links = [link for link in links if '?action' not in link]
      links = [link for link in links if 'php' not in link or 'pmwiki.php' in link]
      links = [tvtropes + link if 'http' not in link else link for link in links]
      links = [link for link in links if tvtropes in link]
      return links

    if __name__ == "__main__":
      crawl(tvtropes)

    {% endhighlight %}

It was horribly broken of course, Python doesn't let you recurse
more than 1000 levels by default. This is actually a feature, since
such deep recursion is usually a bug outside of functional programming.
The reason I was running into it here was because I was essentially
trying to recursively walk a tree with a node for every page on TvTropes,
which has about a half million of them by my count. My initial workaround
was to just do `sys.setrecursionlimit(2000000)` and get rid of the limit. 
This wasn't the right thing to do and the crawler was missing substantial
numbers of pages.

The solution to my problem was to just use the scrapy library. It was
much faster than my code and wasn't missing pages. As a general rule,
if you have a need for some code that does X and you’re not trying to
learn more about X you should look for a library instead of rolling your
own. If you have to roll your own, then you should make it an open-source
project and give back to the community. The way scrapy "walks the tree"
if it has a queue of webpages to crawl that it pushes webpages onto and
pops them out of. This gets around the issue of limited stack space, by
allocating everything on the heap and is the efficient way if your language
does not automatically optimize tail recursion. Spoiler alert, Python doesn't.

In a language that does optimize tail calls, such as Haskell instead of
allocating more room on the stack every time we call a function, we can
check if the function call is the final expression in a method and choose
to reuse the stack space from the function that we're calling from. This
works because we know none of the data stored in that part of the stack
is needed anymore.

