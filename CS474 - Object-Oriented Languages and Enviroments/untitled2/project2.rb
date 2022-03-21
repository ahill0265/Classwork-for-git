# frozen_string_literal: true

# calling relevant files (well, one of them is, at least)
require_relative 'operations'
require_relative 'parser'

file = File.open('pc_input.txt')
a = IO.readlines(file)
$current_line = 0
register = RegisterOperation.new
cutoff = 0

# calculate - reads the current line of the file
# adjusts registers as instructed and advances to next line of input file
def calculate(a, register)
  string = a[$current_line].split(' ')
  puts a[$current_line]

  if string[1] == '?'
    $current_line = string[2].to_i - 2 unless register.check_if_zero(string)
  else
    register.what_function(string)
  end

  register.print_registers
  $current_line += 1
end

# close_program - closes file and ends execution of the program
def close_program(a, file)
  if $current_line == a.size
    file.close
    puts 'end of file'
    exit
  end
end

puts "Welcome to the Ruby Programmable Calculator. Following are the instructions:
Make sure 'pc_input.txt' is in the folder.
r - Run all lines of file input
s - Run on line of file input
x - Exit calculator
**********************************************************************************"

loop do
  print 'Input: '
  input = gets.chomp.strip

  case input
  when 'x'
    file.close
    break
  when 'r' # read through the entire file at once
    while $current_line <= a.size do
      close_program(a, file)
      calculate(a, register)
      cutoff += 1

      if cutoff == 100 # pauses execution after 100 evaluations in a row to defend against infinite loops
        cutoff = 0
        puts 'Hit 100 evaluations. Halting loop'
        break
      end
    end
  when 's' # reading file step by step
    close_program(a, file)
    calculate(a, register)
  end
end
