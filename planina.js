const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    //output: process.stdout
});

rl.on('line', (line) => {
    var nums = line.split(' ');
    var a = parseInt(nums[0]);
    var result = Math.pow(Math.pow(2,a) + 1,2);
    console.log(result)
});