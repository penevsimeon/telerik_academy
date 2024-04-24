<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# Unit Testing the Test Reporter System

[_Who tests the tests?_](https://en.wikipedia.org/wiki/Quis_custodiet_ipsos_custodes%3F)

## Description

The system is implemented and fully functional. Your task is to write unit tests for it. 
- You should try to cover as many **distinct** scenarios as possible.
    - What does **distinct** mean? Imagine that a function raises error if it receives a non-positive number, and doubles the number otherwise. Distinct scenarios would be:
        1. test the function with positive number, and expect the double of that number
        2. test the function with non-positive number, and expect an error
    - Writing several unit tests for positive values, or for negative values would be of no additional benefit.
    - One test per scenario is enough.
- Try to think about corner cases.

## Tasks

### `class TestRun`
- initializer assigns values or raises errors

### `class TestGroup`
- initializer assigns values or raises errors
- `add_test()` - read the implementation and think of distinct scenarios
- `__str__` - what cases should be tested?
- `view()` - what cases should be tested?

### `class Test`
- initializer assigns values or raises errors
- What are the possible results for each of these properties: 
    - `passing_test_runs` 
    - `failed_test_runs`
    - `total_runtime`
    - `avg_runtime`   
    - Read their implementations and think of corner cases.
- `add_test_run()` - make sure that it works with same and different TestRuns
- `generate_report()` - what cases should be tested?
- `__str__` - what cases should be tested?

### `class CommandFactory`
- check that each command is created for all possible inputs
- check that error is raised if the input has invalid command
- check that the app_data is initialized for each command
- check that the params property is correctly extracted from the input
- some commands expect models factory - check that it is correctly initialized

### `class ModelsFactory`
- Think how to test the result of each of its methods:
    - `create_group()`
    - `create_test()`
    - `create_test_run()`

### `class ApplicationData`
- Test the initializer
- Study the methods carefully and test their result:
    - `find_group()`
    - `find_test()`
    - `add_group()`
    - `remove_group()`

## Hints
- to test the `__str__` methods, you can pass the tested object to the `str` function, or format it - `f'{tested_obj}'`. Both formatting and str invoke the `__str__` magic method
- you are **NOT** expected to use *Mocks*