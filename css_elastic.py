#coding: utf-8
import sys
lines = int(sys.argv[1])
columns = int(sys.argv[2])
column_width = 0.0
line_height = 0.0


column_width = 100.0/columns
line_height = 100.0/lines


for c in xrange(columns):
	for l in xrange(lines):
		print ".layout-cell-%d-%d{postion: absolute;margin: 0%% ;padding: 0%%;left: %f%%;right: %f%%;top: %f%%;bottom: %f%%}" %(c,l,c * column_width ,(c + 1) * column_width, l * line_height, (l + 1) * line_height)
#		print ".layout-cell-%d-%d-full-line{postion: absolute;margin: 0%% ;padding: 0%% ;left: %f%%;right: 0%%;top: %f%%;bottom: %f%%}" %(c,l,column_width * (c + 1) ,l * line_height, (l + 1) * line_height)
#		print ".layout-cell-%d-%d-full-column{postion: absolute;margin: 0%%;padding: 0%%;left: %f%%;right: %f%%;top: %f%%;bottom: 0%%}" %(c,l,c * column_width ,(c + 1) * column_width, l)
		
		for dc in range(columns):
			for dl in range(lines):
				if l <= dl and c <= dc:
					print ".layout-cell-%d-%d-until-%d-%d{position: absolute;margin: 0%%;padding: 0%%;left: %f%%;right: %f%%;top: %f%%;bottom: %f%%;min-width: 1px}" %(c,l,dc,dl,c * column_width ,(dc + 1) * column_width,l * line_height, (dl + 1) * line_height)
					print ".layout-cell-%d-%d-reverse-until-%d-%d{position: absolute;margin: 0%%;padding: 0%%;left: %f%%;right: %f%%;top: %f%%;bottom: %f%%;min-width: 1px}" %(c,l,columns - dc,lines - dl,c * column_width ,(dc + 1) * column_width,l * line_height, (dl + 1) * line_height)
					print ".layout-cell-%d-%d-size-%d-%d{position: absolute;margin: 0%%;padding: 0%%;left: %f%%;top: %f%%;width: %f%%;height: %f%%;min-width: 1px}" %(c,l,columns - dc,lines - dl,c * column_width ,l * line_height, column_width,line_height)

	
		
