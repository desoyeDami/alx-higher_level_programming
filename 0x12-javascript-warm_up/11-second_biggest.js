#!/usr/bin/node

const args = Number(process.argv);

if (isNaN(args[2]) || args.length === 3) {
  console.log(0);
} else {
  const array = args.map(Number);
  array.slice(2, args.length);
  array.sort((a, b) => a - b);
  console.log(array[array.length - 2]);
}
