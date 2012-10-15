#!/usr/bin/python2
# -*- coding: utf-8 -*-

###########################################################
print ""
import sys
if len(sys.argv) != 2:
     print "Ça prend un url de video.telequebec.tv!"
     print "Par exemple:"
     print "    http://video.telequebec.tv/video/12256/episode-4"
     print ""
     exit()
     
url = sys.argv[1]
print "url:",url

###########################################################
# Lit le code source de l'url et trouve le vidéo .flv
import urllib2
xml = urllib2.urlopen(url).read()
ind1 = int(xml.find("rtmp"))
ind2 = int(xml.find(".flv"))
video = xml[ind1:ind2 + len('.flv')]

###########################################################
# Crée le nom du fichier de sortie à partir du 
# fichier xml et de l'url
tag = "<h2 class=\"categoryTitle\">"
ind1 = int(xml.find(tag))
ind2 = int(xml.find("</h2>"))
nom = xml[ind1+len(tag):ind2].replace(" ","_")    # titre de l'émission
nom += "_" + url.split("/")[-1].replace("-","_")  # épisode
nom += ".flv"

###########################################################
# Appelle rtmpdump
import subprocess
cmd = "rtmpdump"
cmd += " -r \"%s\""%video
cmd += " -o %s"%nom
cmd += " -W http://video.telequebec.tv/content/flash/lecteur_av_stq.swf"
cmd += " -p %s"%url

subprocess.call(cmd, shell=True)
     
###########################################################