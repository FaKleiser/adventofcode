crabs=temp1.innerText.split(',').map(n => 1*n)
bestFuel=Infinity;
bestPost=NaN
for (pos=Math.min(...crabs); pos <= Math.max(...crabs); pos++) {
  fuel = crabs.reduce((fuel, crab) => fuel + Math.abs(crab-pos), 0)
  if (fuel < bestFuel) {
    bestFuel = fuel; bestPos = pos;
  }
}
bestFuel



// part 2: using Gauss summation
bestFuel=Infinity;
bestPost=NaN
for (pos=Math.min(...crabs); pos <= Math.max(...crabs); pos++) {
  fuel = crabs.reduce((fuel, crab) => {
    steps=Math.abs(crab-pos)
    return fuel + steps*(steps+1)/2
  }, 0)
  if (fuel < bestFuel) {
    bestFuel = fuel; bestPos = pos;
  }
}
bestFuel
