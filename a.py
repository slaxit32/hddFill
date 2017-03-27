import os, string
import ctypes
import platform
import sys

def fill(path,n):
	f= open(path,"a+")
	try:
		for i in range(n):
			f.write("|")
	except Exception as e:
		raise e
	f.close()

def fillFinal(path):
	print("\nAlmost Complete..... Wait")
	f= open(path,"a+")
	try:
		while(1):
			f.write("|")
	except IOError:
		print()

	print("Finish")
	print("Free space now ",get_free_space_byte(path)," bytes")
	f.close()

def get_free_space_mb(dirname):
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024

def get_free_space_byte(dirname):
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize



available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
print(available_drives)

partion="Z:"
fileName="fill.file"
fileNameAndPath=partion+"\\"+fileName

freeSpaceInMB=get_free_space_mb(partion)

if(freeSpaceInMB<1024):

	print("Free space in ",partion," ",freeSpaceInMB," MB")

	devideTo=10
	sizeInByte=freeSpaceInMB*1024*1024
	onePartSize=sizeInByte/devideTo
	onePartSizeMB=onePartSize/1024/1024

	tempSize=onePartSizeMB
	for i in range(devideTo):
		print("Filling partion ",(i+1)*devideTo,"% ",format(tempSize, '.5f')," Mb of ",format(freeSpaceInMB, '.5f')," Mb")
		fill(fileNameAndPath,int(onePartSize))
		tempSize+=onePartSizeMB;

	fillFinal(fileNameAndPath)

	try:
		os.remove(fileNameAndPath)
		print("Fill file removed")
	except Exception as e:
		raise e
	

else:

	print("Free space in ",partion," ",freeSpaceInMB/1024," GB (",freeSpaceInMB," MB)")

	devideTo=100
	sizeInByte=freeSpaceInMB*1024*1024
	onePartSize=sizeInByte/devideTo
	onePartSizeMB=onePartSize/1024/1024

	tempSize=onePartSizeMB
	for i in range(devideTo):
		print("Filling partion ",i+1,"% ",format(tempSize, '.5f')," Mb of ",format(freeSpaceInMB, '.5f')," Mb")
		fill(fileNameAndPath,int(onePartSize))
		tempSize+=onePartSizeMB;

	fillFinal(fileNameAndPath)

	try:
		os.remove(fileNameAndPath)
		print("Fill file removed")
	except Exception as e:
		raise e





