lines = File.readlines("input.txt")
haystack = lines.each_with_object({}) { |line, hash| hash[line.to_i] = 1 }

puts "Part 1 Solution"
haystack.keys.each do |key|
  needle = 2020 - key
  if haystack[needle]
    puts "#{key} * #{needle} = #{key * needle}"
    break
  end
end

puts "Part 2 Solution"
haystack.keys.each do |key|
  needle_sum = 2020 - key
  haystack.keys.each do |key2|
    needle = needle_sum - key2
    next if needle < 0
    if haystack[needle]
      puts "#{key} * #{key2} * #{needle} = #{key * key2 * needle}"
      exit(0)
    end
  end
end
