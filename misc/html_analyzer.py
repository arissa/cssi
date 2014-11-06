f = open('google.html', 'r')
contents = f.read()
f.close()

end = -1

counts = {}

while True:
	start = contents.find('<', end + 1)
	if start == -1: 
		break

	end = contents.find('>', start + 1)
	tag = contents[start:end + 1]

	space = tag.find(' ')

	if space == -1:
		tag_name = tag[1:-1] #takes off first and last char
	else:
		tag_name = tag[1:space]
	if '/' in tag_name:
		continue #jumps back to top of while loop

	print tag_name

	if tag_name not in counts:
		counts[tag_name] = 1
	else:
		counts[tag_name] += 1

print counts