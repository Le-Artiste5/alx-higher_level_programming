#!/usr/bin/node
/* This prints out the first argument */
const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
