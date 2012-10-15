#!/usr/bin/python2
# -*- coding: utf-8 -*-

###########################################################
# Ce script effectue automatiquement les opérations
# décrites ici: store-it.appspot.com/tou/tou.html

###########################################################
print ""
import sys
if len(sys.argv) != 2:
     print "Ça prend un url de Tou.tv!"
     print "Par exemple:"
     print "    http://www.tou.tv/les-appendices/S05E03"
     print ""
     exit()
     
url = sys.argv[1]
print "url Tou.tv:",url

###########################################################
# Lit le code source de l'url et trouve idMedia
import urllib2
source_str = urllib2.urlopen(url).read()
ind = int(source_str.find("idMedia"))
id = source_str[ind:-1].split(":")[1].split(",")[0].replace("\"","")
if len(id) > 0: print "Trouvé idMedia:",id
else: 
     print "Ne semble pas avoir trouvé idMedia!"
     print ""
     exit()

###########################################################
# Récupère le liens 
url2 = "http://release.theplatform.com/content.select?pid=%s"%id
print ""
print url2

xml = urllib2.urlopen(url2).read()

ind1 = int(xml.find("rtmp"))
ind2 = int(xml.find(".mp4"))

# unescape converts entity references back to the corresponding characters
# http://wiki.python.org/moin/EscapingXml
from xml.sax.saxutils import unescape 
target = unescape(xml[ind1:ind2 + len('.mp4')])

print ""
if len(target) > 0: print "Trouvé la source:\n\n",target
else: 
     print "Ne semble pas avoir trouvé la source!"
     print ""
     exit()
print ""
     
###########################################################
# Crée le nom du fichier téléchargé à partir de l'url
ss = url.split("/")
nom = ss[-2] + '_' + ss[-1] + '.flv'

###########################################################
# Appelle une version légèrement modifiée du script
# trouvé ici: http://store-it.appspot.com/tou/tou.html
import subprocess
cmd = "sh rtmp_script.sh \"%s\" %s" %(target, nom)
subprocess.call(cmd, shell=True)

###########################################################