#!/usr/bin/node

const args = process.argv;
const numArgs = args.length - 2;

if (numArgs > 1) {
  console.log('Arguments found');
} else if (numArgs === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
