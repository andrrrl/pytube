#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import re
from lxml.html import parse

try:
    import urllib2
except ImportError:
    import urllib as urllib2


class YTSearch():

    # default player MPV
    #PLAYER = 'mpv'
    PLAYER = 'castpytube.sh'

    # set default option to "start at zero time" just to avoid empty option list
    #PLAYER_OPTIONS = '--start=00'
    PLAYER_OPTIONS = ''

    def __init__(self):

		# modo de uso: python pytube.py | python pytube.py "mi búsqueda" [opciones
		# nativas de reporductor]

		if len(sys.argv) < 2:
			search = raw_input('Buscar en youtube: ')
		else:
			search = sys.argv[1]
			if len(sys.argv) == 3:
				player_options = sys.argv[2]

		print "Buscando videos de \"%s\"..." % search
		print "[Usando TOR]"
		search = re.sub(' ', '+', search)

		opener = urllib2.build_opener()
		opener.addheaders = [
		    ('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
		url = opener.open('https://www.youtube.com/results?search_query=' + search)
		html = parse(url).getroot()

		# Listar resultado de búsqueda
		i = 1
		links = []
		for link in html.cssselect('[rel=spf-prefetch]'):
			links.append(link.get('href'))
			print "%d - %s (youtube.com%s)" % (i, link.text_content(), link.get('href'))
			i += 1

		select = raw_input('Elegite un vídeo: ')

		watch = subprocess.Popen(
		    [self.PLAYER, 'https://www.youtube.com' + links[int(select) - 1], '-']
        )

		print 'Cargando video, esperá un choca...'
		
if __name__ == '__main__':
	YTSearch()
