import os
import strutils

proc readInput*(day: string): string =
    return readFile(joinPath("inputs", day)).strip

proc readInputLines*(day: string): seq[string] =
    return splitLines(readInput(day))
