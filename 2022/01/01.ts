import * as fs from 'fs';
const deers = fs.readFileSync('2022/01/01.txt','utf8').split("\n\n");

let maxCals = 0;
for (const deer of deers) {
    const cals = deer.split("\n")
        .map(x => +x)
        .reduce((sum, cal) => sum + cal, 0);
    if (cals > maxCals) {
        maxCals = cals;
    }

}

console.log("Max Cals", maxCals);

let allCals: number[] = [];
for (const deer of deers) {
    const cals = deer.split("\n")
        .map(x => +x)
        .reduce((sum, cal) => sum + cal, 0);
    allCals.push(cals);
}
allCals.sort((a,b) => b-a);
console.log('Top 3', allCals[0]+allCals[1]+allCals[2]);