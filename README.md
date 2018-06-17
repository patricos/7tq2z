# 7tq2z

Project: Client-server system for solving Reversed Polish Notation (RPN)

Assigned: May 29th (casual thinking started, with Internet browsing)

Started: June 5th (office-time stated, with actual work)

# Introduction to README.md

I consider README.md my notebook that documents the process of solving the assignment you gave me.  This notebook is here in this prominent place in order to guide the assessors through my work.  Normally, README.md would be stripped of from some mid-process-notes and would be focused on helping the users of the end-result - I realize that.

So below you will find my notes along with what is normally considered "publishable information" about the end-product.

## Caveats

This is a solution to a flash engineering challenge, the solution which is by a request a little bit quick'n'dirty-but-workin'.  There are therefore a few "dirty" spots that were left behind for the sake of "quckness", while still sticking to the specification.  Please note:

1. In client.rb - in its socket transmission block - performance penalty due to the organization of the connection setup.
2. In server.py - security risk - not a good practice to call a shell process with parameters made of an unsanitized input string.
3. In worker.go - not exception-resistant - errornous RPN expression will return a non-num result, and so will division by zero.

# System design

## Language analysis

Candidates:
* Go: considerably faster than Python and Ruby, because it is compiled. Suitable for fast-operating worker.
* Python: build with prototypong in mind and hence it is abundant in shortcuts and wide-meaning-constructs. Suitable for complex architectures, perhaps good for server.
* Ruby: interpreted slowly (not good for time-sensitive server probably) - Unfavourable to run junction/server/splitter/processor (compared to Go at least), perhaps the best choice for end-user interface.

To think: what has greater resource demands: server (work splitter) or worker (expression calculator).  Perhaps a trade-off: many small expressions will back-up the splitter (server), and a few big expressions will place more load on worker than on splitter.

Brief analysis. All possible easily: Socket communication, spawning a child process in background.

## Architecture overview

As described in the assignment doc, with some additional bullet-points:
1. Client (end-point)
   * stdin/stdout (DONE)
   * feeds expression data (via API) using a specific format (DONE)
   * uses sockets for communication (DONE)
2. Server (with api)
   * server app: gathers requests, socket-based, listens (DONE)
   * logs events to a file with a timestamp
   * returns a calculated result + computing time
   * calls workers: one worker per an expression
3. Worker
   * accepts input parameters (string? file? pipeline?)
   * returns output value / error value

## Architectural details

### Endpoint

### Server

### Worker

Perhaps returns to the server the same way endpoits do?

