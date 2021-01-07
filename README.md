<h1 align="center>ToDoCLI</h1>
<ul>
<h2>USAGE</h2>
<li><h3>### 1. Help </h3></li>

Executing the command without any arguments, or with a single argument `help` prints the CLI usage.

```
$ ./todo help
Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics
```

<li><h3> 2. List all pending todos </h3></li>

Use the `ls` command to see all the todos that are not yet complete. The most recently added todo should be displayed first.

```
$ ./todo ls
[2] change light bulb
[1] water the plants
```

<li><h3> 3. Add a new todo </h3></li>

Use the `add` command. The text of the todo item should be enclosed within double quotes (otherwise only the first word is considered as the todo text, and the remaining words are treated as different arguments).

```
$ ./todo add "the thing i need to do"
Added todo: "the thing i need to do"
```

<li><h3> 4. Delete a todo item </h3></li>

Use the `del` command to remove a todo item by its number.

```
$ ./todo del 3
Deleted todo #3
```

Attempting to delete a non-existent todo item should display an error message.

```
$ ./todo del 5
Error: todo #5 does not exist. Nothing deleted.
```

<li><h3> 5. Mark a todo item as completed </h3></li>

Use the `done` command to mark a todo item as completed by its number.

```
$ ./todo done 1
Marked todo #1 as done.
```

Attempting to mark a non-existed todo item as completed will display an error message.

```
$ ./todo done 5
Error: todo #5 does not exist.
```

<li><h3> 6. Generate a report </h3></li>

Use the `report` command to see the latest tally of pending and completed todos.

```
$ ./todo report
yyyy-mm-dd Pending : 1 Completed : 4

</ul>
