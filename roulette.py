#!/usr/bin/env python 3

import random
import numpy as np
from tqdm import trange
from multiprocessing import Process, Pool


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


def simulate_one_deposit(deposit, bet, target, cashback):
		result = roulette_bet(deposit, bet, target)
		if  result < 0:
			return result*(1-cashback)
		else:
			return result

def simulate(num_sims):
	return [simulate_one_deposit(DEPOSIT,BET, TARGET, CASHBACK) for _ in range(num_sims)]

def main():
	data = Pool().map(simulate,[NUM_SIMS]*8)
	simulation =np.array(data)
	print(f'EV for this simulation is: {simulation.mean():.2f}')
	print(f'Max win: {simulation.max()}   Max loss: {simulation.min():.1f}')

if __name__ == '__main__':
	main()
