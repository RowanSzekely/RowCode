# RowScript

RowScript is a small interpreted programming language written in Python.
This project is primarily a learning exercise focused on understanding how
programming languages work.

## Usage

- Run in interactive REPL mode:
  - `python main.py`
- Run a RowScript source file:
  - `python main.py <filename>`

## Features and Syntax

RowScript currently supports:

- **Variables and constants**
  - Declared using `declare` and `const`
  - Constants cannot be reassigned
  - Example:
    ```
    declare x = 10; x = 5;
    const y = 20;
    declare greeting = "hello";
    ```

- **Primitive values**
  - Numbers
  - Booleans
  - Strings
  - Null (`null`)

- **Binary arithmetic**
  - `+`, `-`, `*`, `/`, `%`
  - Example:
    ```
    declare result = 1 + 2 * 3;
    ```
  
- **Unary operations**
  - `-`, `!`
  - Example (In this example product is set to -20 and x to false):
    ```
    declare product = -10 * 2;
    declare x = !true;
    ```

- **Comparisons**
  - `==`, `!=`, `<`, `<=`, `>`, `>=`
  - Example:
    ```
    declare isEqual = (x == 5);
    ```

- **Block scoping**
  - `{}`
  - Each block introduces a new environment
  - Variables can be reassigned in inner blocks
  - Variables cannot be redeclared in inner scopes

- **if / elif / else statements**
  - Example:
    ```
    if (a > b) { 
        a = a + 3;
    } elif (a == b) {
        a = a + 2;
    } else {
        a = a + 1;
    }
    ```

- **While loops**
  - Loop condition is evaluated each iteration
  - Example:
    ```
    while ( x < 10 ) {
        print("looping");
        x = x + 1;
    }
    ```
  - Numbers can be used as input to have the while loop run a set number of times
  - Example (The following loop will run 10 times, even though x is being modified):
    ```
    declare x = 10;
    while(x) {
        x = x + 1;
    }
    ```

- **User-defined functions**
  - Declared using `fdeclare`
  - Functions capture the environment they are defined in
  - Functions return the last evaluated statement, unless return is used
  - Example:
    ```
    fdeclare add(a, b) {
        declare sum = a + b;
        return sum;
    }
    declare sum = add(1, 2);
    ```

- **Native functions**
  - Implemented directly in Python
  - Currently supports:
    - `print(value)`
      - Example (This will print: My name is Jon and my age is 44):
        ```
        declare name = "Jon"
        declare age = "44"
        print("My name is ", name, " and my age is ", age);
        ```
    - `length(arr)`
      - Example (This will print: 3):
        ```
        declare arr = [1,2,3];
        print(length(arr));
        ```
    - `random(min, max)`
      - Returns a random integer between min and max inclusive
      - Example:
        ```
        declare randomVal = random(1, 10);
        ```

- **Comments**
  - Single-line comments: `//`
  - Multi-line comments: `/* ... */`

- **Arrays**
  - Declared using square brackets
  - Arrays can be nested
  - Array elements can be accessed and assigned using 0-based indexing
  - Arrays can store values of any type
  - Example:
    ```
    declare inner = [1, 2];
    declare outer = [1, 2, 3, inner, "Hello"];
    print(outer[0]);
    outer[3][1] = 77;
    ```


