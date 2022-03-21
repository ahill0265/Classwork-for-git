# parser

# abstract class holds register values and defines methods
class Register
  # the registers of the programmable calculator
  @@w = 0
  @@x = 0
  @@y = 0
  @@z = 0

  def store_constant(x, y); end

  def check_if_zero(x); end

  # print_registers - prints out the contents of the registers at time of calling
  def print_registers
    puts "w: #@@w, x: #@@x, y: #@@y, z: #@@z"
  end
end

# RegisterOperation gives methods defined in abstract class function
class RegisterOperation < Register

  # what_function - is given a line from the input file
  # determines if the instruction is to store a constant or perform an operation
  def what_function(string)
    if string.length == 3
      store_constant(string[0], string[2].to_f)
    else
      do_eval(string)
    end
  end

  # store_constant - called when an input string is an instruction to store a constant into a register
  # stores the constant into the stated register (class variable)
  def store_constant(string, constant)
    case string
    when 'w'
      @@w = constant
    when 'x'
      @@x = constant
    when 'y'
      @@y = constant
    when 'z'
      @@z = constant
    end
  end

  # do_eval - given a line of input from the input file if it's an operation
  # puts the result of that operation into a register
  def do_eval(string)
    newString = string.map do |item|
      case item
      when 'w'
        item = '@@w'
      when 'x'
        item = '@@x'
      when 'y'
        item = '@@y'
      when 'z'
        item = '@@z'
      else
        item
      end
    end

    eval(newString.join(' '))
  end

  # check_if_zero - called when the second character in an input string is '?'
  # returns a boolean of if the register being evaluated is equal to 0
  def check_if_zero(string)
    case string[0]
    when 'w'
      string[0] = '@@w'
    when 'x'
      string[0] = '@@x'
    when 'y'
      string[0] = '@@y'
    when 'z'
      string[0] = '@@z'
    end

    return eval(string[0] + ' == 0')
  end
end

