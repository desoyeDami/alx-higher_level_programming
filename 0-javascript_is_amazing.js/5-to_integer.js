#!/usr/bin/node

const args = process.argv;
const toNumber = Number(args[2]);

if (isNaN(toNumber)) {
  console.log('Not a Number');
} else {
  console.log('My number: ', toNumber);
}
