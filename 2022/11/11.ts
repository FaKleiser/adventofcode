import * as fs from 'fs';
const content: string = fs.readFileSync('2022/11/11.txt','utf8');

let monkeyParser = /Monkey (?<monkey>\d):\s+Starting items: (?<start>.+)\n\s*Operation: (?<op>.+)\n\s*Test: divisible by (?<test>\d+)\n\s*If true:.*(?<throwTrue>\d+)\n\s*If false:.*(?<throwFalse>\d+)/g

class Monkey {
    private numInspections = 0;
    constructor(
        private monkey: string,
        private bag: number[],
        private inspect: (worryLevel: number) => number,
        private test: (worryLevel: number) => number
    ) {}

    public catch(item: number) {
        this.bag.push(item);
    }

    public hasItems(): boolean {
        return this.bag.length > 0;
    }
    public inspectAndThrow(): {item: number, to: number} {
        this.numInspections++;
        let worryLevel = this.bag.shift();
        worryLevel = this.inspect(worryLevel);
        // part 1:
        // worryLevel = Math.floor(worryLevel / 3);
        // part 2: (we only care about low numbers, so take this modulo the least common multiple of worryLevel test of all monkeys)
        worryLevel = Math.floor(worryLevel) % (2*3*5*7*11*13*17*19);
        return {
            item: worryLevel,
            to: this.test(worryLevel),
        }
    }
    public toString() {
        return `Monkey ${this.monkey}: ${this.bag.join(',')} (inspected ${this.numInspections})`;
    }
}


const monkeys: Monkey[] = [];
const matches = content.matchAll(monkeyParser);
for (let match of matches) {
    monkeys.push(new Monkey(
        match.groups.monkey,
        match.groups.start.split(',').map(n => new Number(n).valueOf()),
        (old: number) => eval(match.groups.op.split('=')[1]),
        (worryLevel: number) => {
            if (worryLevel % new Number(match.groups.test).valueOf() == 0) {
                return new Number(match.groups.throwTrue).valueOf();
            }
            return new Number(match.groups.throwFalse).valueOf();
        }
    ));
}

// part 1: 20 rounds, part 2: 10000 rounds
for (let round = 1; round <= 10000; round++) {
    for (const monkey of monkeys) {
        while (monkey.hasItems()) {
            const target = monkey.inspectAndThrow();
            monkeys[target.to].catch(target.item);
            // console.log(`Item with worry level ${target.item} is thrown to monkey ${target.to}`)
        }
    }
    if (round % 1000 == 0 || round == 1 || round == 20) {
        console.log(`Round ${round}`);
        monkeys.map(m => console.log(m.toString()));
    }
}