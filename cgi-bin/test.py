#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi
import cgitb
from os import listdir

cgitb.enable()

files = listdir("../articles")

print 'Content-type: text/html\n\n'

print '<link rel="stylesheet" type="text/css" href="../stylesheets/style-inner.css" />'

print '<H1 class="article-title">How to run Python scripts in cPanel</H1>'
print '<ul>'
for f in files:
	if '.html' in f:
		print '<li><a href=../articles/' + str(f) + '>' + str(f) + '</a></li>'
print '</ul>'