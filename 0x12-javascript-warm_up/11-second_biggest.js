#!/usr/bin/node
/* A script that prints the second biggest number in arguments */

const args = process.argv;

if (args.length <= 3) {
	console.log('0')
} else
{
	let second = parseInt(args[2]);
	let highest = parseInt(args[3]);
	for (let i = 2; i < args.length; i++) {
		const current = parseInt(args[1]);
		if (current > highest) {
			second = highest;
			highest = current;}
		else if (current > second && current < highest) {
			second = current;
		}
	}
	console.log(second);
}
