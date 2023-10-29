def file_size(file_info):
	name, type, size= file_info
	return("{:.2f} KB/s".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


EXPECTED OUTPUT:

17.46 KB/s
0.48 KB/s
1.21 KB/s
