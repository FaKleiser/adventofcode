import * as fs from 'fs';
let lines: string[] = fs.readFileSync('2022/06/06.txt','utf8').split("\n");

// example input:
// lines = `bvwbjplbgvbhsrlpgdmjqwftvncz
// nppdvjthqldpwncqszvftbrmjlhg
// nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
// zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`.split("\n");


const findMarker = (line, len) => {
    for (let offset = 0; offset < line.length - len; offset++) {
        const chars: string[] = line.slice(offset, offset+len).split("");
        if ([...new Set(chars)].length == len) {
            return offset + len;
        }
    }
}

// part1
for (let line of lines) {
    console.log('First marker found at', findMarker(line, 4));
}

// part 2

// new example input:
// lines = `mjqjpqmgbljsphdztnvjfqwrcgsmlb
// bvwbjplbgvbhsrlpgdmjqwftvncz
// nppdvjthqldpwncqszvftbrmjlhg
// nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
// zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw`.split("\n");

for (let line of lines) {
    console.log('Message marker found at', findMarker(line, 14));
}