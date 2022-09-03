import sys
import heapq


def parse_data_from_file(filename):
	data = None
	with open(filename, 'r') as f:
		n = int(f.readline().strip())
		tasks = list(map(int, f.readline().strip().split(' ')))
		calling_sequence = list(f.readline().strip())
		data = (tasks, calling_sequence)
	return data

def sequence(tasks, calling_sequence):
	tasks = sorted(tasks, reverse=True)
	jack_tasks = []
	sequence, jack_hour, jill_hour = '', 0, 0
	for c in calling_sequence:
		if c == 'J':
			task = tasks.pop()
			heapq.heappush(jack_tasks, -task)
			jack_hour += task
			sequence += str(task)
		elif c == 'j':
			task = -heapq.heappop(jack_tasks)
			jill_hour += task
			sequence += str(task)
	print(sequence)
	print(f'Jack will work for {jack_hour} hours')
	print(f'Jill will work for {jill_hour} hours')


def main():
	sys.stdout = open('task3_output.txt', 'w')
	tasks, calling_sequence = parse_data_from_file('task3_input.txt')
	sequence(tasks, calling_sequence)


if __name__ == '__main__':
	main()