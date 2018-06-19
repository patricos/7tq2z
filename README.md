# 7tq2z

Project: Client-server system for solving Reversed Polish Notation (RPN)

Assigned: May 29th (casual thinking started, with Internet browsing)

Started: June 5th (office-time stated, with actual work)

# Introduction

I consider README.md my notebook that documents the process of solving the assignment you gave me.  This notebook is here in this prominent place in order to guide the assessors through my work.  Normally, README.md would be stripped of from some mid-process-notes and would be focused on helping the users of the end-result - I realize that.

So below you will find my notes along with what is normally considered "publishable information" about the end-product.

## How to run the project

Platform is: Ubuntu 14.04 LTE.  Firstly install: `python` (version 2.7.6 was used/tested), `gccgo-go` (4.9.3), `ruby` (1.9.3p484)

You need the repository.  Go to the location you want the repo to sit and run: `git clone  https://github.com/patricos/7tq2z`.  From now on the absolute path of reference in this document is the direcotry of this repository.

One program needs compiling: `cd src/worker && go build rpnworker.go`

Look up the src directory.  The following files require some configuration definitions:

* server/logger.py - logger host and port, log path
* server/listener.py - server host and port, logger host and port, worker executable
* client/client.rb - server host and port

Start up the services.  Run each command in a separate terminal:

* `cd src/server/ && python logger.py`
* `cd src/server/ && python listener.py`

Start up the client.  You can feed the client program with a text file or use the client program manualy:  You can use `src/client/clienttest.sh` (but from its own directory!) that can be run in a shell (I used bash).  It spawns a client (`src/client/client.rb`) and fetches the content of `src/client/clienttest.txt` to stdin of the `client.rb`.  Alternatively, you can run `client.rb` manually (the first input-line contains an integer - a number of expressions - the remaining lines contain expressions).

## Caveats

This is a solution to a flash engineering challenge.  The solution to which is by a request a little bit quick'n'dirty-but-workin'.  There are therefore a few "dirty" spots that were left behind for the sake of "quckness", while still sticking to the specification.  Please note:

1. In client.rb - in its socket transmission block - performance penalty due to the organization of the connection setup.
2. In server.py - security risk - not a good practice to call a shell process with parameters made of an unsanitized input string.
3. In worker.go - not exception-resistant - errornous RPN expression will return a non-num result, and so will division by zero.
4. In logger.py - the idea of putting this online is the jewel in the crown of the "caveats"-chapter.  No input sanitation, no incomming traffic restrictions, no secret password, just feeds anything it gets into a file.  Put you safety squints on, please.

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

Okay, it has turned out that my code is my documentation - I have indeed followed one of the SCRUM's manifesto points: "working with software over extensive documentation".  So, how it is build - can be seen from the code (including comments) ;-)  However, I tried to include all non-obvious important information in this readme, so I hope it is comprehensive enough.  EOF ;-)

### Endpoint

### Server

### Worker

