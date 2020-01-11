const readline = require('readline')
const rl = readline.createInterface({
    input: process.stdin,
    //output: process.stdout
});

rl.on('line', (line) => {
    var n = line.split(' ');
    //console.log("n = "+ n);

        var r = parseInt(n[0]);
        var e = parseInt(n[1]);
        var c = parseInt(n[2]);
        if (!(n.length < 3)){
            if (r > e - c) {
                console.log("do not advertise");
            }
            else if (r < e - c) {
                console.log("advertise");
            } else {
                console.log("does not matter");
            }
        }
});