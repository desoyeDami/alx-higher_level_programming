#!/usr/bin/node

const args = Number(process.argv);

if (isNaN(args[2]) || args.length === 3) {
  console.log(0);
} else {
  console.log('Yes');
}
