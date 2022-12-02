import * as fs from 'fs';
let matches = fs.readFileSync('2022/02/02.txt','utf8').split("\n");
// example input:
// matches = ["A Y", "B X", "C Z"];

const scores = {
    "A X": 1+3, "A Y": 2+6, "A Z": 3+0,
    "B X": 1+0, "B Y": 2+3, "B Z": 3+6,
    "C X": 1+6, "C Y": 2+0, "C Z": 3+3,
}

let score = 0;
for (let match of matches) {
    score += scores[match];
}
console.log("Score Round 1", score);

score = 0;
const endOfGameMapping = {
    "A X": "A Z", "A Y": "A X", "A Z": "A Y",
    "B X": "B X", "B Y": "B Y", "B Z": "B Z",
    "C X": "C Y", "C Y": "C Z", "C Z": "C X",
}
for (let match of matches) {
    score += scores[endOfGameMapping[match]];
}
console.log("Score Round 2", score);