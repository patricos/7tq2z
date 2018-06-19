// Server program for RPN expression calculator
// by Patryk Mazurkiewicz in Jun 2018
//
// OKAY: gets a parameter strin (an expression)
// todo: explodes the expression into an array
// todo: rpn calculation algorithm
// OKAY: returns value or error - via pipelining of stgout in server
//
// note: input comes as parameters, they get parsed into os.Args array
//

package main

import (
    "os"
    "fmt"                           
    "strconv"
)

func main() {

    var numstack []float64
    var x float64
    var y float64

    for _, op := range os.Args[1:] {

        if (op == "+") || (op == "-") || (op == "*") || (op == "/") {

            y        = numstack[ len(numstack)-1]   // pop(numstack) w/out rm
            numstack = numstack[:len(numstack)-1]   // remove topmost element
            x        = numstack[ len(numstack)-1]   // pop(numstack) w/out rm
            numstack = numstack[:len(numstack)-1]   // remove topmost element

            switch op {
            case "+":  numstack = append(numstack, x+y) //
            case "-":  numstack = append(numstack, x-y) // kind of push
            case "*":  numstack = append(numstack, x*y) // to the stack
            case "/":  numstack = append(numstack, x/y) //
            }

        } else {

            z, _ := strconv.ParseFloat(op, 64)
            numstack = append(numstack, z)

        }

    }

    if len(numstack)==1 {
        fmt.Print( numstack[0] )
    } else {
        fmt.Print( "Oops..." )
    }
}

