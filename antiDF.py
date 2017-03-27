import os, string
import ctypes
import platform
import sys

os.system('cls')

print("\n\n-------------------------------------------------------------------------------------")

print("Anti Forensics Fill Hard Drive by Dilusha")

print("-------------------------------------------------------------------------------------")

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

	print("Finish\n")
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

def lessThanGB(de):

	print("\nStarting to fill partition : "+partion)

	print("\nFree space in ",partion," ",freeSpaceInMB," MB\n")

	devideTo=de
	sizeInByte=freeSpaceInMB*1024*1024
	onePartSize=sizeInByte/devideTo
	onePartSizeMB=onePartSize/1024/1024

	tempSize=onePartSizeMB
	for i in range(devideTo):
		print("Filling partion ",(i+1)*devideTo,"% ",format(tempSize, '.5f')," Mb of ",format(freeSpaceInMB, '.5f')," Mb")
		fill(fileNameAndPath,int(onePartSize))
		tempSize+=onePartSizeMB;
	
def moreThanGB(de):

	print("\nStarting to fill partition : "+partion)

	print("\nFree space in ",partion," ",freeSpaceInMB/1024," GB (",freeSpaceInMB," MB)\n")

	devideTo=de
	sizeInByte=freeSpaceInMB*1024*1024
	onePartSize=sizeInByte/devideTo
	onePartSizeMB=onePartSize/1024/1024

	tempSize=onePartSizeMB
	for i in range(devideTo):
		print("Filling partion ",i+1,"% ",format(tempSize, '.5f')," Mb of ",format(freeSpaceInMB, '.5f')," Mb")
		fill(fileNameAndPath,int(onePartSize))
		tempSize+=onePartSizeMB;


def delete():
	try:
		os.remove(fileNameAndPath)
		print("Fill file removed")
	except Exception as e:
		raise e






available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
#print(available_drives)

noOfDrives=len(available_drives)

if(noOfDrives==0):
	print("No partition detected")

else:


	print("\nEnter the assosiated number to fill the partition\n")


	for i in range(noOfDrives):
		print(str(i+1)+": "+available_drives[i])

	print("")
		
	
	try:
		t1=int(input())

		if(t1>0 and t1<=noOfDrives):
			partion=available_drives[t1-1]
			fileName="fill.file"
			fileNameAndPath=partion+"\\"+fileName

			freeSpaceInMB=get_free_space_mb(partion)

			if(freeSpaceInMB<1024):

				lessThanGB(10)
				fillFinal(fileNameAndPath)
				#delete()
				
			else:

				moreThanGB(100)
				fillFinal(fileNameAndPath)
				#delete()

		else:
			print("Enter drive number between 1 and "+str(noOfDrives))


	except ValueError:
		print("Enter drive number between 1 and "+str(noOfDrives))



print("-------------------------------------------------------------------------------------")













