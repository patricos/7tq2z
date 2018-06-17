# Client program for RPN expression calculator
# by Patryk Mazurkiewicz in Jun 2018
#

require 'socket'
require 'time'

def number_or_zero(string)
  Integer(string || '')
rescue ArgumentError
  0
end

serveripaddr = 'localhost'
serveripport = 8088

# The first stdin input is an int and it tells how long we gonna go
str = gets
n = number_or_zero  str

# All following stdin inputs are the rpn expressions
rpnlist = Array.new
for i in 1..n do
    rpnlist.push  gets
end

# Now sending the expressions to the resolver-server + outputting them
for rpn in rpnlist do
    tic = Time.now
    s = TCPSocket.new(serveripaddr, serveripport)
    s.print  rpn
    tictoc = (Time.now - tic) * 1000.0
	puts s.read + ", " + tictoc.round(3).to_s
    s.close
end


