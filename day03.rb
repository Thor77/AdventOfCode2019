require 'set'

Point = Struct.new(:x, :y)

wires = File.readlines('inputs/03').map { |l| l.rstrip.split(',') }

coords = wires.map do |wire|
  x = 0
  y = 0
  wire_coords = []
  wire.each do |instruction|
    length = instruction[1..].to_i
    case instruction[0]
    when 'R'
      path = length.times.map { |i| Point.new(x + i + 1, y) }
      x += length
    when 'L'
      path = length.times.map { |i| Point.new(x - i - 1, y) }
      x -= length
    when 'U'
      path = length.times.map { |i| Point.new(x, y + i + 1) }
      y += length
    when 'D'
      path = length.times.map { |i| Point.new(x, y - i - 1) }
      y -= length
    end
    wire_coords.concat(path)
  end
  wire_coords
end

intersections = coords[0].to_set & coords[1].to_set

distances = intersections.map { |i| i.x.abs + i.y.abs }
puts "Part 1: #{distances.min}"

latencies = intersections.map { |i| coords[0].index(i) + coords[1].index(i) + 2 }
puts "Part 2: #{latencies.min}"
