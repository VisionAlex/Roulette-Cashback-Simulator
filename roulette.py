#!/usr/bin/env python 3

import random
import numpy as np
from tqdm import trange


DEPOSIT = 1000
BET = 80
TARGET = 3000
NUM_SIMS = 100000
CASHBACK = 0.07


def roulette_bet(deposit,bet,target):
	balance = deposit
	def check(bet):
		if bet > balance:
			bet = balance
		if bet < balance and BET <= balance:
			bet = BET
		return bet
	while bet <= balance and balance < target and balance > 0:
		bet =check(bet)
		balance += random.choices([-bet, bet*35], weights=(36,1))[0]
		bet = check(bet)
	return balance -deposit


def simulate(deposit, bet, target,num_sims, cashback):
	results =[]
	for i in trange(num_sims):
		result= roulette_bet(deposit, bet, target)
		if result < 0:
			results.append(result*(1-cashback))
		else:
			results.append(result)
	return results


def main():
	simulation = np.array(simulate(DEPOSIT, BET, TARGET, NUM_SIMS, CASHBACK))
	print(f'EV for this simulation is: {simulation.mean()}')
	#roulette_bet(DEPOSIT, BET, TARGET)

if __name__ == '__main__':
	main()
