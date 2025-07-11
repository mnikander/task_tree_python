|Num| YYYY-MM-DD | Superseded by | Decision                           | Rationale |
|001| 2025-07-07 |               | store data as CSV, not SQL         | Human readable, editable, and works well with git for version control.|
|002| 2025-07-07 |               | file path as command line argument | Allows storing the task list locally or in a private repository, instead of in the code repository.|
|003| 2025-07-07 |               | model tasks as a tree              | Allows splitting into subtasks and modeling dependencies, a bottom up tree structure is easy to store: only requires a parent id.|
|004| 2025-07-07 | 008           | ~~python script to visualize~~     | ~~Easy to implement using pandas.~~|
|005| 2025-07-07 |               | simplest task first                | Good strategy when overwhelmed. Make progress on a task which is quick and easy. Gets 1 task off the list and boosts motivation.|
|006| 2025-07-07 |               | shortest job next                  | Very simple. Easy to implement. Reasonable approximation of 'simplest task'. Minimizes waiting time of jobs. May starve jobs.|
|007| 2025-07-07 |               | fields for frog, urgent, important | Allows more nuanced strategies and visualizations to be implemented, such as 'eat the frog' or an Eisenhower matrix.|
|008| 2025-07-11 | 011           | ~~implement it in TypeScript~~     | ~~using TypeScript allows incremental development towards an interactive Electron app.~~|
|009| 2025-07-11 |               | print the tree in post-order       | Tasks are printed in the order in which they can be done. Sub-tasks are at the top-left and root-tasks are at the bottom-right. This emphasizes the next step.|
|010| 2025-07-11 |               | command line tool, no GUI at first | A script with console output is easy to implement.|
|011| 2025-07-11 |               | implement it in Python             | Runnable on my laptop. My laptop has Ubuntu 18, which has a very old NodeJS version (12) which can't build the TypeScript application I built.|
