<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg)" alt="logo" width="300px" style="margin-top: 20px;"/>

# TestReporter - Test Reporting System

## Description

TestReporter is a tool for monitoring the testing process of a large distributed web application. Most of the tool is implemented, but several features need finishing. While implementing the missing functionality, we will also practice:
- Inheritance (by subclassing commands)
- Abstraction (by treating different commands in a similar manner)
- Polymorphism (by overriding inherited functionality)
- Duck typing (by calling the same method on different objects)

### Models
- **TestGroup** - a model that represents a group of tests with `name` and a `collection of Tests`
- **Test** - a model that represents a test with `id`, `description` and a `collection of TestRuns`
- **TestRun** - a model that represents a single run of an automated test - has a `test_result` (pass/fail) and `runtime` (in milliseconds)

### Features
- **Add TestGroup** - creates a test group with Name and next available TestGroupId
- **Add Test** - creates a new Test with the next available TestId and description and adds it to an existing TestGroup (found by id)
- **Add TestRun** - creates a TestRun, and adds it to an existing Test (found by id)
- **Test Report** - generates a report for a Test (found by id), printing information about the case and the associated TestRuns
- **Remove Group** - removes a group of tests (identified by id)
- **View Group** - prints information about a group (identified by id)
- **View System** - prints information about all groups

## Tasks
### 1. Models
Already implemented. You are allowed to modify them in any way that you find suitable

### 2. Engine class
The `start` method has to be implemented. Its behavior is roughly the following:

    1. read input
    2. find suitable command to execute
    3. print the result of the command (or store for printing later)
    4. stop if you reached the end command

You can check the engine class of the previous workshops if you feel stuck.

**Note** - in this workshop, we **do not have to handle exceptions**. There is no invalid input.

### 3. CommandFactory class
The `create` method has to be implemented. Its responsibility is the following:

    1. receive the input
    2. determine which command is requested
    3. create and return the correct command

### 4. ApplicationData class
The class has to be finished. It should support the following functionality
- add a testgroup
- find testgroup by id
- remove testgroup by id
- find test by id

### 5. Commands
Check the sample output for the results and formatting of each command. You can use https://www.diffchecker.com/ to compare your output with the sample output. 

You need to implement the following classes. You can subclass from the provided `BaseCommand` to get access to the shared properties of all commands.

- `AddTestGroup` (params: name) - creates a new TestGroup with the given **name** and stores in the AppData. TestGroupIds must be sequential (first - 1, second - 2, etc).
- `AddTest` (params: test_group_id, description) - creates a new test with the given **description** and adds it to the test group with the given **test_group_id**. TestIds must also be sequential.
- `AddTestRun` (params: test_id, result, runtime) - adds a new test run with the given **result** and **runtime** and adds it to the test with the given **test_id**
- `RemoveGroup` (params: test_group_id) - removes a group, specified by the given **test_group_id** and also removes all its tests along with their testruns
- `TestReport` (params: test_id) - returns formatted information about a test with the given **test_id**. Formatting:
    ```
    #{test_id}. [{test_description}]: {test_runs_count} runs
    - Passing: {passing_runs_count}
    - Failing: {failing_runs_count}
    - Total runtime: {total_runtime}ms
    - Average runtime: {avg_runtime:.1f}ms
    ```
- `ViewGroup` (params: test_group_id) - returns formatted information about a group with the given **test_group_id**. Formatting:
    ```
    #{group_id}. {group_name} ({tests_count} tests)
      #{test_id}. [{test_description}]: {test_runs_count} runs
      #{test_id}. [{test_description}]: {test_runs_count} runs
    ```
- `ViewSystem` (no params) - returns formatted information about the Test Reporter System. Formatting:
    ```
    Test Reporter System ({test_groups_count} test groups)
      #{group_id}. {group_name} ({tests_count} tests)
      #{group_id}. {group_name} ({tests_count} tests)
    ```
### Hints

#### Step 1:
Start with implementing the AddTestGroup command. It is the easiest. What it does is the following:

    1. create a new TestGroup with the provided name and the next available id
    2. do not forget to increment the id, and *remember* it somewhere
    3. add the created TestGroup to the ApplicationData - you should have access to it from the inheritted BaseCommand
    4. return a message

#### Step 2:
When you have the command, you can write a portion of the CommandFactory's implementation - check if the input line starts with the command name and if yes, create and return a new AddTestGroup command instance

#### Step 3:
Now you can finish the `start` method of the engine class - use the factory to create a new command, execute it, and print or store the results for printing later

#### Step 4:
Test the program with only input that is related to adding testgroups.
Do it several times to be sure that testgroupids are sequentially generated.

#### Step 5:
Repeat (without step 3) for each of the remaining commands.  
Along the way you will likely need to add new methods to the ApplicationData class - for example for removing testgroups


### Example input

```
addtestgroup TransactionTests
addtest 1 ShouldWork_WhenToldTo
addtestrun 1 fail 10
addtestrun 1 pass 15
addtestrun 1 fail 17
addtestrun 1 fail 8
testreport 1
addtest 1 MustWork!_OnlyWhenCorrect
addtestrun 2 pass 3
addtestrun 2 pass 15
addtestrun 2 fail 74
addtestrun 2 pass 63
viewgroup 1
testreport 2
addtestgroup UITests
addtest 2 BtnClick_ActuallyClicks
addtestrun 3 pass 8
addtestrun 3 pass 3
addtestrun 3 pass 5
viewsystem
removegroup 1
viewsystem
end
```

### Example output

```
Group #1 created
Test #1 added to group #1
TestRun registered
TestRun registered
TestRun registered
TestRun registered
#1. [ShouldWork_WhenToldTo]: 4 runs
- Passing: 1
- Failing: 3
- Total runtime: 50ms
- Average runtime: 12.5ms
Test #2 added to group #1
TestRun registered
TestRun registered
TestRun registered
TestRun registered
#1. TransactionTests (2 tests)
  #1. [ShouldWork_WhenToldTo]: 4 runs
  #2. [MustWork!_OnlyWhenCorrect]: 4 runs
#2. [MustWork!_OnlyWhenCorrect]: 4 runs
- Passing: 3
- Failing: 1
- Total runtime: 155ms
- Average runtime: 38.8ms
Group #2 created
Test #3 added to group #2
TestRun registered
TestRun registered
TestRun registered
Test Reporter System (2 test groups)
  #1. TransactionTests (2 tests)
  #2. UITests (1 tests)
Group #1 removed
Test Reporter System (1 test groups)
  #2. UITests (1 tests)
```
