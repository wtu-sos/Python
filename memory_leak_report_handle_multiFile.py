# coding=utf-8
# 默认打印出前10
#起始序列
beginIndex = 1
#结束序列
endIndex = 10

result = list()
export_memleak_txt = "leak_export.txt"			# 输出文件目录
source_leak_file = "memory_leak_report.txt"			# 处理的文件目录
flag_str = "---------- Block"						# 特征子串

# 读取排序
def get_data():
	line_num = 0
	for line in open(source_leak_file):
		line_num += 1
		if line.find(flag_str) > -1:
			lst = line.split(" ")
			result.append((line_num,long(lst[5])))
	result.sort(key=lambda x:x[1],reverse=True)


# 打印特定序列
def print_result(begin = 1, end = 1):
	index = 0
	for item in result:
		index += 1
		if index < begin:
			continue

		if end != 0 and begin > end:
			break

		print ("key: %d, value: %d " % item)
		begin = begin + 1
	
# 输出特定序列
def text_out(begin = 1, end = 1):
	output = open(export_memleak_txt, 'w')
	index = 0
	for item in result:
		index += 1
		if index < begin:
			continue

		if end != 0 and begin > end:
			break
		begin += 1
		line_num = 0;
		bWriteHeadLine = False
		for line in open(source_leak_file):
			line_num += 1
			if line_num == item[0]:
				bWriteHeadLine = True
				output.write("\n")
				output.write(line)
			elif (bWriteHeadLine and line_num > item[0]):
				if line.find(flag_str) > -1:
					output.write("\n")
					bWriteHeadLine = False
					break
				else: 
					output.write(line)

	output.close()

def run(begin = 1, end = 10):
	get_data()
	print_result(begin, end)
	text_out(begin, end)

run(beginIndex, endIndex)
