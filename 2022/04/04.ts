import { group } from 'console';
import * as fs from 'fs';
let lines: string[] = fs.readFileSync('2022/04/04.txt','utf8').split("\n");

// example input:
// lines = `2-4,6-8
// 2-3,4-5
// 5-7,7-9
// 2-8,3-7
// 6-6,4-6
// 2-6,4-8`.split("\n");

const assignments = lines.map(line => {
    return line.split(",").map(elf => elf.split('-').map(str => Number(str)))
})


// part1
const contains = (elf1: number[], elf2: number[]) => {
    if (elf1[0] <= elf2[0] && elf1[1] >= elf2[1]) {
        return 1;
    }
    if (elf2[0] <= elf1[0] && elf2[1] >= elf1[1]) {
        return 1;
    }
    return 0;
}

let count = 0;
for (const assignment of assignments) {
    count += contains(assignment[0], assignment[1]);
}
console.log("Count of contained", count)


// part2
const overlaps = (elf1: number[], elf2: number[]) => {
    if (elf1[0] > elf2[1] || elf1[1] < elf2[0]) {
        return 0;
    }
    return 1;
}

count = 0;
for (const assignment of assignments) {
    count += overlaps(assignment[0], assignment[1]);
}
console.log("Count of overlapping", count)