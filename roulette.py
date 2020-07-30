#!/usr/bin/env python 3

import random
import numpy as np
from tqdm import trange


DEPOSIT = 1000
BET = 100
TARGET = 3000
NUM_SIMS = 100000
CASHBACK = 0.07


def roulette_bet(deposit,bet,target):
	balance = deposit
	while balance < target and balance > 0:
		spin_bet = min(bet,balance)
		balance += random.choices([-spin_bet, spin_bet*35], weights=(36,1))[0]
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
	print(f'EV for this simulation is: {simulation.mean():.2f}')
	print(f'Max win: {simulation.max()}   Max loss: {simulation.min():.1f}')
	# print(roulette_bet(DEPOSIT, BET, TARGET))

if __name__ == '__main__':
	main()
