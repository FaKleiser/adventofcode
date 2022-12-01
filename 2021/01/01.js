// run in browser console and setup input=`...` from problem input
input.split("\n").reduce((cnt, val, idx, input) => {
    if (1*val < (1*input[idx+1] || 0)) { return cnt + 1; }
    return cnt;
}, 0)
