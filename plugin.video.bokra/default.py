# -*- coding: utf8 -*-
import urllib,urllib2,re,xbmcplugin,xbmcgui
import xbmc, xbmcgui, xbmcplugin, xbmcaddon
from httplib import HTTP
from urlparse import urlparse
import StringIO
import urllib2,urllib
import re
import httplib
import time
import xbmcgui


__settings__ = xbmcaddon.Addon(id='plugin.video.bokra')
__icon__ = __settings__.getAddonInfo('icon')
__fanart__ = __settings__.getAddonInfo('fanart')
__language__ = __settings__.getLocalizedString
_thisPlugin = int(sys.argv[1])
_pluginName = (sys.argv[0])



def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except httplib.IncompleteRead, e:
            return e.partial

    return inner
httplib.HTTPResponse.read = patch_http_response_read(httplib.HTTPResponse.read)


def CATEGORIES():
	#xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%('WARNING','This addon is completely FREE DO NOT buy any products from http://tvtoyz.com/', 16000, 'http://upload.wikimedia.org/wikipedia/he/b/b1/Bokra.net_logo.jpg'))
	addDir('مسلسلات رمضان 2013','http://www.bokra.net/VideoCategory/125/مسلسلات_رمضان_2013.html',6,'http://images.bokra.net/bokra//28-11-2010/4shobek.jpg')
	addDir('مسلسلات عربية','http://www.bokra.net/VideoCategory/98/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA_%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9.html',1,'http://images.bokra.net/bokra//28-11-2010/4shobek.jpg')
	addDir('مسلسلات متنوعة','http://www.bokra.net/VideoCategory/43/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA.html',1,'http://images.bokra.net/bokra//28-11-2010/4shobek.jpg')
	addDir('افلام عربية','http://www.bokra.net/VideoCategory/100/أفلام_عربية.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir(' افلام فلسطينية','http://www.bokra.net/VideoCategory/18/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D9%81%D9%84%D8%B3%D8%B7%D9%8A%D9%86%D9%8A%D8%A9.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('افلام وثائقيه','http://www.bokra.net/VideoCategory/23/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D9%88%D8%AB%D8%A7%D8%A6%D9%82%D9%8A%D8%A9.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('افلام قديمة','http://www.bokra.net/VideoCategory/51/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D9%82%D8%AF%D9%8A%D9%85%D8%A9.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('افلام دينية','http://www.bokra.net/VideoCategory/24/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D8%AF%D9%8A%D9%86%D9%8A%D8%A9.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('مسرحيات','http://www.bokra.net/VideoCategory/44/%D9%85%D8%B3%D8%B1%D8%AD%D9%8A%D8%A7%D8%AA.html',4,'http://images.bokra.net/bokra/25.10.2011/msr7//DSCF0480.jpg')
	addDir('كليبات وحفلات','http://www.bokra.net/VideoCategory/118/%D9%83%D9%84%D9%8A%D8%A8%D8%A7%D8%AA_%D9%88%D8%AD%D9%81%D9%84%D8%A7%D8%AA.html',4,'http://images.bokra.net/new/402839.jpg')
	addDir('برامج تلفزيونية','http://www.bokra.net/VideoCategory/39/%D8%A8%D8%B1%D8%A7%D9%85%D8%AC_%D8%AA%D9%84%D9%81%D8%B2%D9%8A%D9%88%D9%86.html',1,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('افلام اطفال ','http://www.bokra.net/VideoCategory/57/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D8%A7%D8%B7%D9%81%D8%A7%D9%84.html',4,'http://images.bokra.net/bokra/15.8.2012/kods//1231.JPG')
	addDir('بكرا TV','http://www.bokra.net/VideoCategory/113/%D8%A8%D9%83%D8%B1%D8%A7_TV.html',1,'http://www.bokra.net/images//logobokra.png')
	addDir('مسلسلات كرتون','http://www.bokra.net/VideoCategory/56/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA_%D9%83%D8%B1%D8%AA%D9%88%D9%86.html',1,'http://images.bokra.net/bokra//16-10-2011/0WeddingCartoon1.jpg')
	addDir('مسلسلات اجنبية','http://www.bokra.net/VideoCategory/93/%D9%85%D8%B3%D9%84%D8%B3%D9%84%D8%A7%D8%AA_%D8%A7%D8%AC%D9%86%D8%A8%D9%8A%D8%A9.html',1,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('مسلسلات تركية','http://www.bokra.net/VideoCategory/27/مسلسلات_تركية_.html',1,'http://images.bokra.net/bokra//28-11-2010/4shobek.jpg')
	addDir('افلام تركية','http://www.bokra.net/VideoCategory/48/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D8%AA%D8%B1%D9%83%D9%8A%D8%A9.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('افلام اجنبية','http://www.bokra.net/VideoCategory/46/%D8%A7%D9%81%D9%84%D8%A7%D9%85_%D8%A7%D8%AC%D9%86%D8%A8%D9%8A%D8%A9.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	addDir('منوعات','http://www.bokra.net/VideoCategory/45/%D9%85%D9%86%D9%88%D8%B9%D8%A7%D8%AA_+.html',4,'http://images.bokra.net/bokra//25-11-2012/0777777.jpg')
	
	
	
def retrive_max_page(url):
    try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		url_ch=(re.compile('<span class="curpage">1</span>(.+?)</div>').findall(link))
		url_ch=str(url_ch)
		url_ch=(url_ch.split('>'))
		page_list=[]
		for items in  url_ch  :
			mystring=items.split('.') 
			for elements in mystring:
				if 'html' in elements:
					elements=str(elements)
					elements=elements.replace('html/', '')
					elements=elements.replace('"', '')
					elements=elements.strip()
					page_list.append(elements)
		
		
			return max(page_list)
    except Exception:
        return 1

def checkURL(url):
    p = urlparse(url)
    h = HTTP(p[1])
    h.putrequest('HEAD', p[2])
    h.endheaders()
    if h.getreply()[0] == 200: return 1
    else: return 0

	
def index(url):
	try:
		counter=0
		orig=url
		kurl=url
		maxvalue=int(retrive_max_page(kurl))+14
		final_items=[]
		for counter in range(0,int(maxvalue)):
			
			kurl=orig+'/'+str(counter)
			req = urllib2.Request(kurl)
			req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
			response = urllib2.urlopen(req)
			link=response.read()
			response.close()
			
			url_ch=(re.compile('<div class="pic"><a href="(.+?)" onClick="(.+?);"><img class="lazy" data-original="(.+?)" width="(.+?)" title="').findall(link))
			if len(str(url_ch))<3:
				url_ch=(re.compile('<div class="pic"><a href="(.+?)" onClick="javascript:(.+?);"><img class="lazy" data-original="(.+?)" width="139" height="96"').findall(link))
			
			for items in url_ch:
			   
				for elements in items:
					
					for i in items:
						url= items[0].strip()
						name= items[1].replace("pageTracker._trackPageview('/VideoAlbum/","")
						name=name.replace("html","")
						name=name.replace(".')","")
						name=name.rsplit("/",1)
						name = name[1].strip() 
						
						image= items[2].strip()
						if image not in final_items:
							final_items.append(name)
							final_items.append(url)
							final_items.append(image)
			for items in final_items:
			#print elements
				if final_items.__len__()>0:
					
					name=final_items.pop(0)
					
				if final_items.__len__()>0:
					
					url=final_items.pop(0)
					
				if final_items.__len__()>0:
					
					image=final_items.pop(0)
					addDir(name,url,2,image)
					
	except Exception:
		print "Film series Exception occured"

def indexRamadanSeries(url):
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    matchSerie = re.compile(' <div class="items">(.+?)<div class="bigBanner">', re.DOTALL).findall(link)
    for items in matchSerie:
        
        myTarget=str( items).split('<div class="item">')
        for itr in myTarget:
            mySecTarget=str( itr).split('/></a></div>')
            mytempPath= mySecTarget[0] 
            if 'spacer8' not in str(mytempPath):
                mypath=str(mytempPath).replace('<div class="pic"><a href="', 'del').replace('onClick="javascript: pageTracker._trackPageview(', 'del').replace(');"><img class="lazy" data-original="',"del").replace('title="','del')
                mypath=str(mypath).split('del')
                finalImage=str( mypath[3]).split('" width=')[0]
                finalName=str( mypath[4]).replace('"', '').strip()
                finalImage=str(finalImage).strip()
                finalUrl=str( mypath[1]).replace('"', '').strip()
                addDir(finalName,finalUrl,2,finalImage)

def indexMySeries(url):
    
	try:
	
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		matchSerie = re.compile(' <div class="items">(.+?)<div class="bigBanner">', re.DOTALL).findall(link)
		for items in matchSerie:
			myPath=str( items).split('<div class="item">')
			for reg in  myPath:
				myP= str(myPath[1]).split('<div class="spacer3"></div>')
				myFinalPath= str(myP[0]).split('/></a></div')[0]
				mypath=str(myFinalPath).replace('<div class="pic"><a href="', 'del').replace('onClick="javascript: pageTracker._trackPageview(', 'del').replace(');"><img class="lazy" data-original="',"del").replace('title="','del')
				mypath=str(mypath).split('del')
				finalImage=str( mypath[3]).split('" width=')[0]
				finalName=str( mypath[4]).replace('"', '').strip()
				finalImage=str(finalImage).strip()
				finalUrl=str( mypath[1]).replace('"', '').strip()
				addLink(finalName,finalUrl,3,finalImage)
	except:
		pass
			
			
			
				
def indexNewSeries(url):
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = urllib2.urlopen(req)
    link=response.read()
    response.close()
    
    matchSerie = re.compile(' <div class="video_box">(.+?)<div class="spacer_videobox"></div>', re.DOTALL).findall(link)
    for item in matchSerie:
        myTempTarget=str(item).split('</div>')
        tempAll= str(myTempTarget[2]).replace('<div class ="textarea">', '').strip()
       
        mypath=str(tempAll).replace('onClick="javascript: pageTracker._trackPageview(', 'del').replace(';" title="', 'del').replace('">  <div class="title">',"del")
        mypath=str(mypath).split('del')
        myName=str( mypath[2]).strip()
       
        myUrl=str( mypath[0]).replace('<a href="', '').replace('"', '').strip()
        print myName 
        addLink(myName,myUrl,3,'')
		
def index_films(url):
	try:
		counter=0
		orig=url
		kurl=url
		final_items=[]
		maxvalue=int(retrive_max_page(kurl))+12
		print "this is max  "+str(maxvalue)
		for counter in range(0,int(maxvalue)):
		   
			kurl=orig+'/'+str(counter)
		 
			req = urllib2.Request(kurl)
			req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
			response = urllib2.urlopen(req)
			link=response.read()
			
			response.close()
			
			url_ch=(re.compile('<div class="pic"><a href="(.+?)" onClick="javascript:(.+?);"><img class="lazy" data-original="(.+?)" width="139" height="96"').findall(link))
			
			
			for items in url_ch:
			   
				for elements in items:
					
					for i in items:
						url= items[0].strip()
						name= items[1].replace("pageTracker._trackPageview('/VideoAlbum/","")
						name=name.replace("html","")
						name=name.replace(".')","")
						name=name.rsplit("/",1)
						name = name[1].strip()  
						image= items[2].strip()
						if image not in final_items:
							final_items.append(name)
							final_items.append(url)
							final_items.append(image)
			for items in final_items:
			#print elements
				if final_items.__len__()>0:
					
					name=final_items.pop(0)
					
				if final_items.__len__()>0:
					
					url=final_items.pop(0)
					
				if final_items.__len__()>0:
					
					image=final_items.pop(0)
					addLink(name,url,5,image)
	except Exception:
		print "Film Exception occured"

			
def listSeries(url):
	
	counter=0
	final_items=[]
	kurl=url
	maxvalue=int(retrive_max_page(kurl))+5
	pointer=False
	
	print "THIS IS PAGENR" +str(maxvalue)
	
        for counter in range(1,int(maxvalue)):
			test_url=kurl+'/'+str(counter)
            
			req = urllib2.Request(test_url)
			req.add_header('Host', 'www.bokra.net')
			req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
			req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36')
			req.add_header('Accept-Encoding', 'gzip,deflate,sdch')
			req.add_header('Accept-Language', 'sv-SE,sv;q=0.8,en-US;q=0.6,en;q=0.4')
			req.add_header('Cookie', '__gads=ID=caaace40ba968885:T=1384540808:S=ALNI_MaJHS-I3T2KjuJwJrFhK-WSSHuOLg; PHPSESSID=o5557ubn6glmber62cpcs0vde4; __utma=1.2064279049.1384540807.1384689773.1384693281.3; __utmb=1.8.10.1384693281; __utmc=1; __utmz=1.1384540807.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); noadvtday=0; __atuvc=5%7C47')
			response = urllib2.urlopen(req)
			link=response.read()
           
			response.close()
            
			url_ch=(re.compile('<div class="pic"><a href="(.+?)" onClick="javascript:(.+?);"><img class="lazy" data-original="(.+?)" width="').findall(link))
			if len(str(url_ch))<3:
				url_ch=(re.compile('<div class="pic"><a href="(.+?)" onClick="javascript:(.+?);"><img src="(.+?)" width="147" height="107').findall(link))
			
     
			for items in url_ch:
				for elements in items:
                    
					for i in items:
						url= items[0].strip()
						name= items[1].replace("pageTracker._trackPageview('/VideoAlbum/","")
						name=name.replace("html","")
						name=name.replace(".')","")
						name=name.rsplit("/",1)
						name = name[1].strip()  
						image= items[2].strip()
						if url not in final_items:
							if 'اعلان' not in name:
								
								final_items.append(name)
								final_items.append(url)
								final_items.append(image)
								pointer=True
			
			
				addLink(name,url,3,image)
			return pointer
				

def VideoLinks(name,url):
    
    try:
		url=(url.split("/"))
	
		serie_num=re.findall(r'\d+', url[5])
		serie_num=str(serie_num)
	
		serie_num=serie_num[0]
		serie_num=str(serie_num)
		serie_num=(serie_num.replace("['", ""))
		serie_num=(serie_num.replace("']", ""))
		final_url=str(url[0]+"//"+url[2]+"/"+url[3]+"/"+url[4]+"/"+url[5]+"/"+serie_num).replace('[','')
	

		temp_url=final_url
		
		req = urllib2.Request(final_url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		req.add_header('Referer', 'http://bokra.net/?ref='+str(final_url))
		response = urllib2.urlopen(req)
		link=response.read()
		
		response.close()
		
		url_ch=(re.compile('<iframe class="video_frame" src="(.+?)" width="385" height="230" scrolling="No"></iframe>').findall(link))
		if len(str(url_ch))<3:
				url_ch=(re.compile('<iframe class="video_frame" src="(.+?)" width="360" height="260" scrolling="No"></iframe>').findall(link))
			
		
		url_image=(re.compile('<link rel="image_src" href="(.+?)" / >').findall(link))
		url_ch=str(url_ch)
		url_ch= url_ch.replace("['", "")
		url_ch= url_ch.replace("']", "")
		url_ch= url_ch.strip()
		url_ch= url_ch.replace(" ", "")
		
		
		
		if "GetVideoPlayer&ID=" in str(url_ch):
			req = urllib2.Request(url_ch)
			req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
			req.add_header('Referer', 'http://bokra.net/?ref='+str(url_ch))
			response = urllib2.urlopen(req)
			link=response.read()
			#print "LINK " +link
			response.close()
			url_ch=(re.compile("'file': '(.+?)',").findall(link))
			url_ch=str(url_ch)
			url_ch= url_ch.replace("['", "")
			url_ch= url_ch.replace("']", "")
			url_ch= url_ch.replace("http://www.youtube.com/watch?v=","").strip()
			playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url_ch
			listItem = xbmcgui.ListItem(path=str(playback_url))
			xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)
		else:
		
        
			req = urllib2.Request(url_ch)
			req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
			req.add_header('Referer', 'http://bokra.net/?ref='+str(url_ch))
			response = urllib2.urlopen(req)
			link=response.read()
			#print "LINK " +link
			response.close()
			url_ch=(re.compile('video_id=(.+?)&cid=').findall(link))
			url_ch=str(url_ch)
			url_ch= url_ch.replace("['", "")
			url_ch= url_ch.replace("']", "")
			url_ch= url_ch.strip()
			
			
			final_url="http://front.drubit.com/generalXML.php?autostart=0&videoid="+url_ch+"&ref="+str(temp_url)
			
			
			req = urllib2.Request(final_url)
			req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
			req.add_header('Referer', 'http://bokra.net/?ref='+str(final_url))
			response = urllib2.urlopen(req)
			link=response.read()
			response.close()
			url_ch=(re.compile('<file>(.+?)vtraffid').findall(link))
			url_ch=str(url_ch)
			url_ch= url_ch.replace("['", "")
			url_ch= url_ch.replace("']", "")
			url_ch=url_ch.replace("?","")
			url_ch= url_ch.strip()
			
			
			#print "This is video file"+url_ch
			url_image=str(url_image).replace("['", "")
			url_image=url_image.replace("']", "").strip()
			#print url_image
			listItem = xbmcgui.ListItem(path=str(url_ch))
			xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)
			
    except IndexError:
        VideoLinks(name,url)
		
def VideoLinks_Films(name,url):
	#print "Before editing "+str(url)
	
	temp_url=url
	
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	req.add_header('Referer', 'http://bokra.net/?ref='+str(url))
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	url_ch=(re.compile('<iframe class="video_frame" src="(.+?)" width="385" height="230" scrolling="No"></iframe>').findall(link))
	url_image=(re.compile('<link rel="image_src" href="(.+?)" / >').findall(link))
	url_ch=str(url_ch)
	url_ch= url_ch.replace("['", "")
	url_ch= url_ch.replace("']", "")
	url_ch= url_ch.strip()
	url_ch= url_ch.replace(" ", "")
	
	if "GetVideoPlayer&ID=" in str(url_ch):
		req = urllib2.Request(url_ch)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		req.add_header('Referer', 'http://bokra.net/?ref='+str(url_ch))
		response = urllib2.urlopen(req)
		link=response.read()
		#print "LINK " +link
		response.close()
		url_ch=(re.compile("'file': '(.+?)',").findall(link))
		url_ch=str(url_ch)
		url_ch= url_ch.replace("['", "")
		url_ch= url_ch.replace("']", "")
		url_ch= url_ch.replace("http://www.youtube.com/watch?v=","").strip()
		playback_url = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % url_ch
		listItem = xbmcgui.ListItem(path=str(playback_url))
		xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)

	else:
	
	
		req = urllib2.Request(url_ch)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		req.add_header('Referer', 'http://bokra.net/?ref='+str(url_ch))
		response = urllib2.urlopen(req)
		link=response.read()
		#print "LINK " +link
		response.close()
		url_ch=(re.compile('video_id=(.+?)&cid=').findall(link))
		url_ch=str(url_ch)
		url_ch= url_ch.replace("['", "")
		url_ch= url_ch.replace("']", "")
		url_ch= url_ch.strip()

		
		final_url="http://front.drubit.com/generalXML.php?autostart=0&videoid="+url_ch+"&ref="+str(temp_url)

		
		req = urllib2.Request(final_url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		req.add_header('Referer', 'http://bokra.net/?ref='+str(final_url))
		response = urllib2.urlopen(req)
		link=response.read()
		response.close()
		url_ch=(re.compile('<file>(.+?)vtraffid').findall(link))
		url_ch=str(url_ch)
		url_ch= url_ch.replace("['", "")
		url_ch= url_ch.replace("']", "")
		url_ch=url_ch.replace("?","")
		url_ch= url_ch.strip()
		url_image=str(url_image).replace("['", "")
		url_image=url_image.replace("']", "").strip()
		
		listItem = xbmcgui.ListItem(path=str(url_ch))
		xbmcplugin.setResolvedUrl(_thisPlugin, True, listItem)


                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param



def addLink(name,url,mode,iconimage):
    u=_pluginName+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    ok=True
    liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    liz.setInfo( type="Video", infoLabels={ "Title": name } )
    liz.setProperty("IsPlayable","true");
    ok=xbmcplugin.addDirectoryItem(handle=_thisPlugin,url=u,listitem=liz,isFolder=False)
    return ok
	


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

              
params=get_params()
url=None
name=None
mode=None


	
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        index(url)
	
elif mode==2:
		print ""+url
		if listSeries(url)==False:
			indexNewSeries(url)
			
elif mode==3:
	print ""+url
	VideoLinks(name,url)
elif mode==4:
	print ""+url
	index_films(url)

elif mode==5:
	print ""+url
	VideoLinks_Films(name,url)
elif mode==6:
	print ""+url
	indexRamadanSeries(url)
	

xbmcplugin.endOfDirectory(int(sys.argv[1]))
