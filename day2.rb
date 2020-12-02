lines = File.read("day2input.txt").split("\n")

count = 0
lines.each do |line|
  line =~ /(\d+)-(\d+) (\w): (\w+)/
  min, max, char, password = $1.to_i, $2.to_i, $3, $4
  charcount = password.scan(/#{char}/).count
  count += 1 if charcount >= min && charcount <= max
end
puts count

count = 0
lines.each do |line|
  line =~ /(\d+)-(\d+) (\w): (\w+)/
  pos1, pos2, char, password = $1.to_i - 1, $2.to_i - 1, $3, $4

  count += 1 if (password[pos1] == char) ^ (password[pos2] == char)
end
puts count
