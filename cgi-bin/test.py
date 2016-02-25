#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi
import cgitb
from os import listdir
from dateutil.parser import parse
import datetime

cgitb.enable()

files = listdir('../articles')


article_list = []
for f in files:
	if '.html' in f:
		file = open('../articles' + '/' + f, mode='r')
		content = file.readlines()
		current_article = {}
		current_article['href'] = f
		current_article['title'] = 'deftitle'
		current_article['subtitle'] = 'defsubtitle'
		current_article['datetime'] = datetime.datetime.now()
		for line in content:
			if 'article-title' in line:
				start = line.find('article-title') + len('article-title') + 2
				end = line.find('</h1>')
				title = str(line[start:end])
				current_article['title'] = title
			elif 'datetime' in line:
				start = line.find('datetime') + len('datetime') + 2
				end = line.find('\">', start)
				dt = parse(line[start:end])
				current_article['datetime'] = dt
			elif 'subtitle' in line:
				start = line.find('subtitle') + len('subtitle') + 2
				end = line.find('</h2>')
				subtitle = str(line[start:end])
				current_article['subtitle'] = subtitle
		article_list.append(current_article)
		# print '<li><a href=../articles/' + str(f) + '>' + title + '</a><br/><time>' + str(dt) + '</time><br/><p>' + str(subtitle) + '</p></li>'
		# print '<hr/>'

sorted_list = sorted(article_list, key=lambda k: k['datetime'], reverse=True)
print 'Content-type: text/html\n\n'
print '<link rel="stylesheet" type="text/css" href="../stylesheets/style-inner.css" />'
print '<h1 class="article-title">Articles</h1>'
print '<ul id="article-list">'
for a in sorted_list:
	print '<li><a href=../articles/' + str(a['href']) + '>' + str(a['title']) + '</a><br/><time>' + str(a['datetime']) + '</time><br/><p>' + a['subtitle'] + '</p></li>'
	print '<hr/>'
print '</ul>'