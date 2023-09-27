f=open("test.txt","w") #write 모드로 열면 파일이 초기화된다.
f.write("hello world!\n")
f.close
f=open("test.txt","a") #add 모드, 파일 내용 유지 및 추가.
f.write("\n")
f.write("abcde")
f.close