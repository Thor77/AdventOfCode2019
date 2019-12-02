import utils
import sequtils
import strutils
import math

proc calculateFuel(mass: int): int =
    return (mass / 3).floor.toInt - 2

proc part1(input: seq[int]): int =
    return input.map(calculateFuel).sum

proc part2(input: seq[int]): int =
    var total = 0
    for mass in input:
        var currentFuel = calculateFuel(mass)
        var totalFuel = currentFuel
        while true:
            currentFuel = calculateFuel(currentFuel)
            if currentFuel <= 0:
                break
            else:
                totalFuel += currentFuel
        total += totalFuel
    return total


if isMainModule:
    let input = readInputLines("01").map(parseInt)
    echo part1(input)
    echo part2(input)
