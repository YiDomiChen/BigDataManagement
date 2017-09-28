## Implementation of Disk Scheduling Algorithms

#### SSTF (Shortest Seek Time First)

SSTF orders the queue of I/O requests by track, picking requests on the nearest track to complete first.

#### SCAN (Elevator)

SCAN moves across the disk servicing requests in order across the tracks.

#### F-SCAN

F-SCAN is a variant of SCAN that addresses the potential starvation problem in the SSTF and SCAN algorithms. In SSTF and SCAN, there is a single queue containing all the requests, including those that are dynamically arriving. F-SCAN instead maintains two queues Q1 and Q2. Before serving the requests, it freezes the queue Q1 which contains all requests currently outstanding. It can moves the head to serve all requests in Q1 just like SCAN. All new requests will be placed into Q2. When it finishes all requests in Q1, it will move all requests in Q2 to Q1. It then starts the “freeze, serve, and move” cycle. F-SCAN is mentioned in the page 11 of reading chapter. Wikipedia has a bit more details too: https://en.wikipedia.org/wiki/FSCAN.