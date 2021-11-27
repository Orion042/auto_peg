#!/usr/bin/env python
import ffmpeg
import math
import sys
import os, os.path

print("=======webpを画像に戻す=======")
while True:
	print(".webp --> .jpg : 1")
	print(".webp --> .png : 2")
	print(".png ---> .jpg : 3")
	print("その他         : 4")
	print("終了           : 5")
	print("==============================")
	user=int(input("番号を入力 : "))
	if user==5:break
	if user==1:
		print("開始番号 --> 1")
		tt=len([name for name in os.listdir(".") if os.path.isfile(name)])
		print("終了番号 --> " + str(tt))
		ch = input("この条件で実行 [Y/N] ")
		if (ch=='Y')|(ch=='y')|(ch=='YES')|(ch=='yes')|(ch=='Yes'):
			n=1
			e=tt
		elif (ch=='N')|(ch=='No')|(ch=='n')|(ch=='no'):
			n=int(input("開始番号を入力:"))
			e=int(input("終了番号を入力:"))
		else:
			print("入力エラー")
			sys.exit()
				
		p=int(math.log10(e)+1)
		#p=int(input("最高桁数を入力:"))
		for i in range(n,e+1):
			i=str(i)
			i=str(i).zfill(p)
			(
				ffmpeg
				.input('{}.webp'.format(i))
				.output('{}.jpg'.format(i))
				.run()
			)
		#mm=len([name for name in os.listdir(".") if os.path.isfile(name)])
		#if(mm==tt*2):	
		break
	if user==2:
		print("開始番号 --> 1")
		tt=len([name for name in os.listdir(".") if os.path.isfile(name)])
		print("終了番号 --> " + str(tt))
		ch = input("この条件で実行 [Y/N] ")
		if (ch=='Y')|(ch=='y')|(ch=='YES')|(ch=='yes')|(ch=='Yes'):
			n=1
			e=tt
		elif (ch=='N')|(ch=='No')|(ch=='n')|(ch=='no'):
			n=int(input("開始番号を入力:"))
			e=int(input("終了番号を入力:"))
		else:
			print("入力エラー")
			sys.exit()
				
		p=int(math.log10(e)+1)
		#p=int(input("最高桁数を入力:"))
		for i in range(n,e+1):
			i=str(i)
			i=str(i).zfill(p)
			(
				ffmpeg
				.input('{}.webp'.format(i))
				.output('{}.png'.format(i))
				.run()
			)
		#mm=len([name for name in os.listdir(".") if os.path.isfile(name)])
		#if(mm==tt*2):	
		break
	if user==3:
		print("開始番号 --> 1")
		tt=len([name for name in os.listdir(".") if os.path.isfile(name)])
		print("終了番号 --> " + str(tt))
		ch = input("この条件で実行 [Y/N] ")
		if (ch=='Y')|(ch=='y')|(ch=='YES')|(ch=='yes')|(ch=='Yes'):
			n=1
			e=tt
		elif (ch=='N')|(ch=='No')|(ch=='n')|(ch=='no'):
			n=int(input("開始番号を入力:"))
			e=int(input("終了番号を入力:"))
		else:
			print("入力エラー")
			sys.exit()
				
		p=int(math.log10(e)+1)
		#p=int(input("最高桁数を入力:"))
		for i in range(n,e+1):
			i=str(i)
			i=str(i).zfill(p)
			(
				ffmpeg
				.input('{}.png'.format(i))
				.output('{}.jpg'.format(i))
				.run()
			)
		#mm=len([name for name in os.listdir(".") if os.path.isfile(name)])
		#if(mm==tt*2):	
		break
	if user==4:
		print("==============================")
		print(".jpg.webp --> .jpg : 1")
		print("その他の拡張子変更 : 2")
		print("拡張子2つある場合 (例 xx.webp.jpgなど) : 3")
		x=int(input("番号を入力 : "))
		print("==============================")
		if x==1:
			print("開始番号 --> 1")
			tt=len([name for name in os.listdir(".") if os.path.isfile(name)])
			print("終了番号 --> " + str(tt))
			ch = input("この条件で実行 [Y/N] ")
			if (ch=='Y')|(ch=='y')|(ch=='YES')|(ch=='yes')|(ch=='Yes'):
				n=1
				e=tt
			elif (ch=='N')|(ch=='No')|(ch=='n')|(ch=='no'):
				n=int(input("開始番号を入力:"))
				e=int(input("終了番号を入力:"))
			else:
				print("入力エラー")
				sys.exit()
				
			p=int(math.log10(e)+1)
			#p=int(input("最高桁数を入力:"))
			for i in range(n,e+1):
				i=str(i)
				i=str(i).zfill(p)
				(
					ffmpeg
					.input('{}.jpg.webp'.format(i))
					.output('{}.jpg'.format(i))
					.run()
				)
			#mm=len([name for name in os.listdir(".") if os.path.isfile(name)])
			#if(mm==tt*2):	
			break
		if x==2:
			a=str(input("元の拡張子 : "))
			b=str(input("変更後拡張子 : "))
			print("開始番号 --> 1")
			tt=len([name for name in os.listdir(".") if os.path.isfile(name)])
			print("終了番号 --> " + str(tt))
			ch = input("この条件で実行 [Y/N] ")
			if (ch=='Y')|(ch=='y')|(ch=='YES')|(ch=='yes')|(ch=='Yes'):
				n=1
				e=tt
			elif (ch=='N')|(ch=='No')|(ch=='n')|(ch=='no'):
				n=int(input("開始番号を入力:"))
				e=int(input("終了番号を入力:"))
			else:
				print("入力エラー")
				sys.exit()
			p=int(math.log10(e)+1)
			for i in range(n,e+1):
				i=str(i)
				i=str(i).zfill(p)
				(
					ffmpeg
					.input('{0}.{1}'.format(i,a))
					.output('{0}.{1}'.format(i,b))
					.run()
				)
			break
		if x==3:
			a=str(input("1つ目の拡張子 :"))
			b=str(input("2つ目の拡張子 :"))
			c=str(input("変換後の拡張子 :"))
			print("開始番号 --> 1")
			tt=len([name for name in os.listdir(".") if os.path.isfile(name)])
			print("終了番号 --> " + str(tt))
			ch = input("この条件で実行 [Y/N] ")
			if (ch=='Y')|(ch=='y')|(ch=='YES')|(ch=='yes')|(ch=='Yes'):
				n=1
				e=tt
			elif (ch=='N')|(ch=='No')|(ch=='n')|(ch=='no'):
				n=int(input("開始番号を入力:"))
				e=int(input("終了番号を入力:"))
			else:
				print("入力エラー")
				sys.exit()
			p=int(math.log10(e)+1)
			#p=int(input("最高桁数を入力:"))
			for i in range(n,e+1):
				i=str(i)
				i=str(i).zfill(p)
				(
					ffmpeg
					.input('{0}.{1}.{2}'.format(i,a,b))
					.output('{0}.{1}'.format(i,c))
					.run()
				)
			break
