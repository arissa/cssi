html='''
<!DOCTYPE html>
<html>
<title>Hello!</title>
<a href="http://www.google.com/">Google</a>
<a href="http://www.yahoo.com/">Yahoo</a>
'''

def get_links(html):
	links=[]
	end = -1

	while True:
		start = html.find('href="', end + 1)
		if start == -1:
			break
		end = html.find('"',start + 6)
		link = html[start+6:end]
		print link
		links.append(link)

	return links
print get_links(html)