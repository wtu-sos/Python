# coding=utf-8
# 根据自己的需要修改过后的文件转移脚本 大部分与原功能相同，
# 加入脚本回调，文件过滤
# 原文链接 http://www.cnblogs.com/sld666666/archive/2011/01/05/1926282.html
import os 
import os.path 
import shutil 
import time,  datetime
Debug_File_Path = "E:/temp/Debug"
Target_File_Path = "E:/temp/workPath"
CallBackScript = "E:/temp/t.py"

NeedCopyFile = ["1.txt", "2.txt", "ZPlus.exe", "ZPlus.pdb"]

def copyFiles(sourceDir,  targetDir): 
	if sourceDir.find(".svn") > 0: 
		return 
	for file in os.listdir(sourceDir): 
			sourceFile = os.path.join(sourceDir,  file) 
			targetFile = os.path.join(targetDir,  file) 
			if os.path.isfile(sourceFile): 
				if (file in NeedCopyFile): 
					print ("find file need copy")
					if not os.path.exists(targetDir):  
						os.makedirs(targetDir)  
					if  os.path.exists(targetFile):  
						os.remove(targetFile)

					open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
			if os.path.isdir(sourceFile): 
				First_Directory = False 
				copyFiles(sourceFile, targetFile)

def removeFileInFirstDir(targetDir): 
	for file in os.listdir(targetDir): 
		targetFile = os.path.join(targetDir,  file) 
		if os.path.isfile(targetFile): 
			os.remove(targetFile)

def writeVersionInfo(targetDir): 
	temp = "Revison:" + getCurTime()
	with open(targetDir, 'at', encoding='utf8') as f: 
		f.write(temp) # or print(hex, file=f) f.close()
		f.close()

def getCurTime(): 
    nowTime = time.localtime() 
    year = str(nowTime.tm_year) 
    month = str(nowTime.tm_mon) 
    if len(month) < 2: 
        month = '0' + month 
    day =  str(nowTime.tm_yday) 
    if len(day) < 2: 
        day = '0' + day 
    return (year + '-' + month + '-' + day)

def main():
	if  __name__ =="__main__": 
		print ("Start(S) or Quilt(Q) \n") 
		flag = True 
		while (flag): 
			answer = input() 
			if  'Q' == answer or answer == 'q': 
				flag = False 
			elif 'S'== answer or answer == 's' : 
				#formatTime = getCurTime() 
				#targetFoldername = "Build " + formatTime + "-01" 
				#Target_File_Path += targetFoldername

				copyFiles(Debug_File_Path,   Target_File_Path) 
				#removeFileInFirstDir(Target_File_Path) 
				#coverFiles(Release_File_Path,  Target_File_Path) 
				#moveFileto(Firebird_File_Path,  Target_File_Path) 
				#moveFileto(AssistantGui_File_Path,  Target_File_Path) 
				writeVersionInfo(Target_File_Path+"/ReadMe.txt") 
				print ("all sucess") 
				os.system(CallBackScript)
			else: 
				print ("not the correct command")
main()
