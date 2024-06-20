#!/usr/bin/node

const args = process.argv;
const input = args[2].trim();
const toNumber = Number(input);

if (isNaN(toNumber)) {
  console.log('Not a Number');
} else {
  console.log('My number: ', toNumber);
}
