#!/usr/bin/env python 3

import random
import numpy as np


DEPOSIT = 1000
BET = 100
TARGET = 3000
NUM_SIMS = 100000
CASHBACK = 0.07


def roulette_bet(deposit,bet,target):
	outcomes =[-bet, bet*35]
	balance = deposit
	while (bet <= balance) and (balance <target) and balance >0:
		balance += random.choices(outcomes, weights=(36,1))[0]
		if bet > balance:
			bet = balance
		#print(balance)
	return balance -deposit


def simulate(deposit, bet, target,num_sims, cashback):
	results =[]
	for i in range(num_sims):
		result= roulette_bet(deposit, bet, target)
		if result < 0:
			results.append(result*(1-cashback))
		else:
			results.append(result)
	return results


def main():
	simulation = np.array(simulate(DEPOSIT, BET, TARGET, NUM_SIMS, CASHBACK))
	print(f'EV for this simulation is: {simulation.mean()}')

if __name__ == '__main__':
	main()
