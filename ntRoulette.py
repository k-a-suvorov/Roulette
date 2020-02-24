#Import nessesary modules
try:
	import os
	import sys
	import time
	import random
	import datetime

	#Functions color-text dor windows-console

	from ctypes import *
	windll.Kernel32.GetStdHandle.restype = c_ulong
	h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))


	money = 100
	currency = "$"
	playGame = True
	bet = 25

	def color(c): #setconsoletextcolor
		windll.Kernel32.SetConsoleTextAttribute(h,c)

	def colorLine(c, s): #Win color text
		#os.system("cls")
		color(c)
		print("*" * (len(s) +2))
		print(" " + s)
		print("*" * (len(s) +2))

	colorLine(6, 'Рулетка. ver. 0.1\nCreated by Opsis ')
	time.sleep(2)
	os.system('cls')


	#Function start game
	def startGame():
		menuRoulette()


	#Function menu Roulette
	def menuRoulette():
		color(2)
		global money
		global bet
		print('Добро пожаловать на игру в Рулетку!')
		print(F'У тебя на счету: {money} {currency}')
		if (money <= 0):
			colorLine(12, 'Вы не можете играть у вас нет денег, прощайте')
		else:
			print(''' Обращаем внимание на то, что в игре можно сделать только одну ставку.
			Множественный выбор не допускается. Если вы сделаете ставку, но откажитесь крутить рулетку
			Вы будете вынуждены покинуть игру, Так же мы вычтем из вашей стартовой суммы деньги в размере вашей ставки
			На что хотите поставить?
			1 - Четное (Выигрыш 1:1)
			2 - Нечетное (Выигрыш 1:1)
			3 - Цвет - (Выигрыш 1:3)
			4 - Дюжина (Выигрыш 1:36)
			5 - Число (Выигрыш 1:36)
			6 - Zero (Выигрыш 1:36) 
			0 - Возврат в предыдущее меню ''')
			
			choice = int(input('>>> '))
			if (choice < 0 or choice > 6):
				print('Вы ошиблись, попробуйте еще раз')
				startGame()
			elif (choice == 0):	
				exitRoulette()
			elif (choice == 1):
				print('Вы ставите на Четное Ваша ставка,')
				getBet()
				evenRoulette()
			elif (choice == 2):
				print('Вы ставите на Нечетное Ваша ставка,')
				getBet()
				oddRoulette()
			elif (choice == 3):
				print('Вы ставите на Черное Ваша ставка,')
				getBet()
				colorRoulette()
			elif (choice == 4):
				print('Вы ставите на Дюжину Ваша ставка,')
				getBet()
				dozenRoulette()
			elif (choice == 5):
				print('Вы ставите на число Ваша ставка,')
				getBet()
				numberRoulette()
			elif (choice == 6):
				print('Вы ставите на Zero Ваша ставка,')
				getBet()
				zeroRoulette()
			

	#Function of user bet
	def getBet():
		color(2)
		global money
		userBet = int(input('Введите вашу ставку (ставка не ниже 10$): '))
		if (userBet < 10 or userBet < 0 or userBet > money):
			print('Ставка не принята, попробуйте еще раз.')
			menuRoulette()
		else:
			print('Ставка принята.')
			money = money - userBet
			print(F'Ваши деньги: {money} ')
		

	#MFunctions of game bets's Roulette
	def evenRoulette():
		color(14)
		global money
		userNumb = random.randint(0, 36)
		if (userNumb % 2 == 0):
			money = money + bet
			print('Вы выиграли желаете сыграть еще раз?')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette
		else:
			writeMoney()
			time.sleep(2)
			print('Удачи в следующий раз!')
			os.system('cls')
			menuRoulette()
			
	def oddRoulette():
		color(14)
		global money
		userNumb = random.randint(0, 36)
		if (userNumb % 2 != 0):
			money = money + bet
			print(F'Вы выиграли ваш приз: {money}, {currency}. Желаете сыграть еще раз?')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette
		else:
			print('Удачи в следующий раз!')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette()
		
			
	def colorRoulette():
		color(14)		
		global money
		userNumb = random.randint(0, 36)
		if (userNumb % 3 == 0):
			money = money + ( bet/ 5)
			print(F'Вы выиграли ваш приз: {money}, {currency}. Желаете сыграть еще раз?')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette
		else:
			print('Удачи в следующий раз!')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette()
			

	def dozenRoulette():
		color(14)
		global money
		dozenChoice = (int(input('Какую дюжину выбираете? \n1 = 1-12 \n2 = 13-24 \n3 = 25 - 36 \n 0 - выход')))
		if (dozenChoice < 0 and dozenChoice > 3):
			Print('Выберете нужную дюжину еще раз.')
			menuRoulette()
		elif (dozenChoice == 1):
			userNumb = random.randint(1, 12)
			if (userNumb >= 1 and userNumb <= 12):
				money = (money * bet) / 5
				print(F'Вы выиграли ваш приз: {money}, {currency}. Желаете сыграть еще раз?')
				writeMoney()
				time.sleep(2)
				os.system('cls')
				menuRoulette
			else:
				print('Удачи в следующий раз!')
				writeMoney()
				time.sleep(2)
				os.system('cls')
				menuRoulette()
		elif (dozenChoice == 2):
			userNumb = random.randint(13, 24)
			if (userNumb >= 13 and userNumb <= 24):
				money = (money * bet) / 5
				print(F'Вы выиграли ваш приз: {money}, {currency}. Желаете сыграть еще раз?')
				writeMoney()
				time.sleep(2)
				os.system('cls')
				menuRoulette
			else:
				print('Удачи в следующий раз!')
				writeMoney()
				time.sleep(2)
				os.system('cls')
				menuRoulette()
		elif (dozenChoice == 3):
			userNumb = random.randint(25, 36)
			if (userNumb >= 25 and userNumb <= 36):
				money = (money * bet) / 5
				print(F'Вы выиграли ваш приз: {money}, {currency}. Желаете сыграть еще раз?')
				writeMoney()
				time.sleep(2)
				os.system('cls')
				menuRoulette
			else:
				print('Удачи в следующий раз!')
				writeMoney()
				time.sleep(2)
				os.system('cls')
				menuRoulette()
		else:
			print('Удачи в следующий раз!')		
			time.sleep(2)
			os.system('cls')
			menuRoulette()
		
	def numberRoulette():
		color(14)
		global money
		userNumb = random.randint(0, 36)
		numbRoulette = random.randint(0, 36)
		if (numbRoulette == numbRoulette):
			print(F'Вы выиграли ваш приз: {money}, {currency}. Желаете сыграть еще раз?')
			money = money * bet
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette
		else:
			print('Удачи в следующий раз!')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette()

		
	def zeroRoulette():
		color(14)					
		global money
		userNumb = random.randint(0, 36)
		if (userNumb == 0):
			money = 2 * (money * bet)
			print(F'Вы выиграли ваш приз: {money}, {currency}. Желаете сыграть еще раз?')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette
		else:
			print('Удачи в следующий раз!')
			writeMoney()
			time.sleep(2)
			os.system('cls')
			menuRoulette()
		

	#exit from game
	def exitRoulette():
		color(12)
		print('До свидания! Приходите к нам еще!')
		playGame = False


	#function of read user money
	def writeMoney():
		global money
		f = open("money.dat", "w", encoding="utf-8")
		f.write(str(money))
		f.close()


	#Method of read user money 
	def readMoney():
		f = open("money.dat", "r", encoding="utf-8")
		moneyStatus = int(f.readline())
		f.close()
		
		return print(moneyStatus)

	startGame()
except ValueError:
    print("You have some mistake of userinput Value!")
except TypeError:
   print("You have some mistake of type Value!")
except SystemError:
	print("This is system mistake! Please don't panic! Relax!")
except FileNotFoundError:
   print("Thereis't file here!")
except FileExistsError:
   print("File or dyrectory allready exist!")
except ImportError:
	print("Some modules not loaded, please check your source code!")
except IOError:
	print('An error IO file!')
