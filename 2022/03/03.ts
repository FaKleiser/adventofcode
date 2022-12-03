import { group } from 'console';
import * as fs from 'fs';
let lines: string[] = fs.readFileSync('2022/03/03.txt','utf8').split("\n");

// example input:
// lines = `vJrwpWtwJgWrhcsFMMfFFhFp
// jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
// PmmdzqPrVvPwwTWBwg
// wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
// ttgJtRGJQctTZtZT
// CrZsJsPPZsGzwwsLwLmpwMDw`.split("\n");

const compartments = lines.map(rucksack => {
    return { 
        compOne: rucksack.slice(0,rucksack.length/2),
        compTwo: rucksack.slice(rucksack.length/2)
    }
})

const priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
let sum = compartments
    .map(rucksack => {
        for (const item of rucksack.compOne) {
            if (-1 != rucksack.compTwo.indexOf(item)) {
                return item;
            }
        }
        return "ERR - shouldn't happen as everything is packed twice";
    })
    .map(item => priorities.indexOf(item))
    .reduce((p,c) => p+c, 0);
console.log("Sum of priorities", sum)


// part2
const groups = [...Array(Math.ceil(lines.length / 3))].map(_ => lines.splice(0,3))
sum = groups
    .map(group => {
        for (const item of group[0]) {
            if (-1 != group[1].indexOf(item) && -1 != group[2].indexOf(item)) {
                return item;
            }
        }
        return "ERR - shouldn't happen as every group of three should have exactly one item in common";
    })
    .map(item => priorities.indexOf(item))
    .reduce((p,c) => p+c, 0);
console.log("Sum of bage reauth", sum)