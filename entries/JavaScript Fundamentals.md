# JAVASCRIPT FUNDAMENTALS

## Script tag - Including JavaScript in your Page

The `<script>` HTML element is used to embed executable code or data; this is typically used to embed or refer to JavaScript code. The `<script>` element can also be used with other languages.

Here's a very basic snippet of JavaScript using the script tag. This JavaScript is written directly into our HTML page. It will call and alert box as soon as the page loads.

```html
<script type="text/javascript">
  alert("This alert box was called with the onload event");
</script>
```
When using the script tag, we must always use the attribute name and value of type="text/javascript".

To include an **external JavaScript file**, we can use the script tag with the attribute src. You've already used the src attribute when using images. The value for the src attribute should be the path to your JavaScript file.

```html
<script type="text/javascript" src="path-to-javascript-file.js"></script>
```
This script tag should be included between the <head> tags in your HTML document.

## What is difference between var, let and const?

The var keyword is the oldest way of declaring variables in JavaScript and is supported by all browsers. The let and const keywords are newer additions to the language and are not supported by older browsers.

If you need to support older browsers, you can use var instead of let or const. If you don’t need to support older browsers, you can use let or const. If you want your variable to be immutable, use const.

Here are some examples:

```js
var x = 1;
let y = 2;
const z = 3;
 
x = 4; //OK 
y = 5; //OK 
z = 6; //Error
```
As you can see, var and let variables can be reassigned, but const variables can not.

**Another difference** between var and let/const is that var variables are function-scoped, while let and const variables are block-scoped.

This means that var variables are only available within the function they were declared in. For example:

```js
function foo() {
  var x = 1;
}
 
foo();
console.log(x); // ReferenceError: x is not defined
```
On the other hand, let and const variables are only available within the block they were declared in. For example:

```js
function foo() {
  let y = 2;
  const z = 3;
}
 
foo();
console.log(y); // ReferenceError: y is not defined 
console.log(z); // ReferenceError: z is not defined
```

So, to sum up, the main differences between var, let and const are:

- var is function-scoped while let and const are block-scoped.
- var variables can be reassigned while let and const variables can not.
- var variables are declared using the var keyword while let and const variables are declared using the let and const keywords respectively.
- const variables are immutable while let and var variables are not.

## if conditional statement

The if conditional statement instructs the computer to execute a JavaScript code block only if a specified condition is true.

Here is its syntax:

```js
if (condition) {
  // code to execute if the stated condition is true
}
```

Here is its syntax:

```js
if (new Date().getHours() < 21) {
  console.log("Today is special!");
}
```
## else conditional statement

The else conditional statement is an optional add-on to the if statement.

When used with an if statement, the else conditional statement instructs that if the if statement's condition is false, the computer should execute the else statement's code block.

Here is its syntax:

```js
if (condition) {
  // code to execute if the stated condition is true
} else {
  // code to execute if the stated condition is false
}
```
Here's an example:

```js
if (condition) {
  // code to execute if the stated condition is true
} else {
  // code to execute if the stated condition is false
}
```

Here's an example:

```js
if (new Date().getHours() < 21) {
  console.log("Today is special!");
} else {
  console.log("Last minutes embodies great opportunities!");
}
```

## else if conditional statement

The else if conditional statement instructs the computer that if the if statement's condition is false, JavaScript should execute the else if's code block based on a different condition.

```js
if (condition1) {
  // code to execute if condition1 is true
} else if (condition2) {
  // code to execute if condition1 is false and condition2 is true
} else if (condition3) {
  // code to execute if condition1 and condition2 are false but condition3 is true
} else {
  // code to execute if all the stated conditions are false
}
```

Here's an example:

```js
if (new Date().getHours() < 21) {
  console.log("Today is special!");
} else if (new Date().getHours() < 22) {
  console.log("Don't waste today's opportunities!");
}
```

Here's another example:

```js
if (new Date().getHours() < 21) {
  console.log("Today is special!");
} else if (new Date().getHours() < 22) {
  console.log("Don't waste today's opportunities!");
} else if (new Date().getHours() < 23) {
  console.log("Fear obscures the eyes of glorious opportunities!");
} else {
  console.log("Last minutes embodies great opportunities!");
}
```

## switch conditional statement

The switch conditional statement instructs the computer to execute a code block if the block's case value matches the given expression.

The switch statement is similar to the if...else if...else conditional statement—except that switch has a predefined expression which the computer uses to assess all other conditions.

Here is its syntax:

```js
switch (benchMarkExpression) {
  case value1:
    // code to execute if value1 matches the benchMarkExpression
    break;
  case value2:
    // code to execute if value1 does not match the benchMarkExpression but value2 does
    break;
  default:
  // code to execute if no value matches the benchMarkExpression
}
```

Here's an example:

```js
const currentHour = new Date().getHours();

switch (currentHour) {
  case 9:
    console.log("Today is special!");
    break;
  case 15:
    console.log("Don't waste today's opportunities!");
    break;
  case 21:
    console.log("Fear obscures the eyes of glorious opportunities!");
    break;
  default:
    console.log("Last minutes embodies great opportunities!");
}
```

Here's another example:
```js
switch (new Date().getDay()) {
  case 0:
    console.log("Sunday is here! The workdays begin...");
    break;
  default:
    console.log("This day is all about work...work...work.");
    break;
  case 5:
    console.log("It's Friday! Prepare for the parties!");
    break;
  case 6:
    console.log("Saturday is a good day to rest well.");
}
```

## while loop statement

A while loop instructs the computer that while a specified condition is true, it should execute the while loop's code block repeatedly.

Here is its syntax:

```js
while (condition) {
  // code to execute if the stated condition is true
}
```
Notice how similar the while loop's syntax is to the if conditional statement. The similarity is no coincidence, as they both work similarly. Their main difference is that an if statement does not loop through its code block, whereas a while statement does.

In other words, an if statement's code block executes just once. However, a while loop's code block executes repeatedly until its specified condition evaluates to false.

Here's an example:

```js
let currentDigit = 1;

while (currentDigit < 5) {
  console.log(currentDigit);
  ++currentDigit;
}
```

## Differences between arrow functions and regular functions in JavaScript

1. Syntax

Curly brackets aren’t required if only one expression is present, and it will implicitly return this result from the function. which makes the code clearer.

```js
// arrow function expression
const add = (a, b) => {
  return a + b;
}

//very simple and concise syntax
const add = (a, b) => a + b;
//eliminates (), if it has single parameter
const square = a => a * a;
```

2. No arguments (arguments are array-like objects)
3. No prototype object for the Arrow function
4. Cannot be invoked with a new keyword (Not a constructor function)

The arrow function cannot be invoked with the new keyword, because arrow functions don’t have a constructor. If you try to instantiate with a new keyword it will throw an error.

5. No own this (call, apply & bind won't work as expected)
6. It cannot be used as a Generator function
7. Duplicate-named parameters are not allowed

In non-restrict mode, regular functions allow us to use duplicate named parameters. But in strict mode, it is not allowed.

## Array Methods

In JavaScript, there are various array methods available that makes it easier to perform useful calculations.

Some of the commonly used JavaScript array methods are:

![Alt text](array-methods.png)

## Fetch API

It was used a free fake API for testing and prototyping - For **GET, POST and DELETE** methods from the exemple attached (see /fetching-data directory) 

https://jsonplaceholder.typicode.com/

We simulate displaying a list of users by getting them with **fetch()** method - a global method that provides an easy, logical way to fetch resources asynchronously across the network.

```js
fetch('https://jsonplaceholder.typicode.com/users')
```

The example contains the functionalities to delete an existing user and to add a new user. After each operation we need to update the UI user list, by adding or removing the affected item.

<i>Note:</i> 
The delete method is used only for learning purpose. In real life we do not want to delete a user (we just disable it).

```js
//ADD A NEW USER
fetch("https://jsonplaceholder.typicode.com/users", {
    method: "POST",
    body: JSON.stringify({
        id: mockedUsers.length + 1,
        name: userName.value,
        email: email.value,
        phone: phone.value,
        company: {
            name: company.value
        }
    }),
  headers: {
    "Content-type": "application/json; charset=UTF-8"
  }
})

// DELETE AN EXISTING USER
fetch('https://jsonplaceholder.typicode.com/users/' + userId,
{
  method: 'DELETE'
})
```


Sndsd