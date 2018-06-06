# 7tq2z

Project: Client-server system for solving Reversed Polish Notation (RPN)

Assigned: May 29th (casual thinking started, with Internet browsing)

Started: June 5th (office-time stated, with actual work)

# Introduction to README.md

I consider README.md my notebook that documents the process of solving the assignment you gave me.  This notebook is here in this prominent place in order to guide the assessors through my work.  Normally, README.md would be stripped of from some mid-process-notes and would be focused on helping the users of the end-result - I realize that.

So below you will find my notes along with what is normally considered "publishable information" about the end-product.

# System design

## Language analysis

Candidates:
* Go: fast(compilable) - worker?
* Python
* Ruby: interpreted slowly (not good for time-sensitive server probably) - user end-point?

To think: what has greater resource demands: server (work splitter) or worker (expression calculator)

Brief analysis. All possible easily: Socket communication, spawning a child process in background

## Architecture overview

As described in the assignment doc, with some additional bullet-points:
1. Client (end-point)
   * stdin/stdout
   * feeds expression data (via API) using a specific format
   * uses sockets for communication
2. Server (with api)
   * server app, socket-based, listens
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

