SCROLL: A Concept Note
=======


# Concept
The purpose of this tool is to reduce the hustle / tediousness of documenting and writing unit tests
for real-time data processing programs.


## How will it achive this
An ideal use would be a tool which listens to your program running, 
- registers the input and output of the functions, once for each function to save memory
- records the functions order of running
- generates documentation and tests in this running order using the 
    (recorded input/output as examples in docs, 
    recorded input/output to generate unit tests,
    automatically adds type hints to docs by checking type(input))


# Goal?
The final goal is to enable a developer/user browser through documentation that flows
in the order in which functions in the program run, hence the name SCROLL.


### Side effects
- I think this will make a developer break down their code a more to ducument as many steps (details) of the process as possible


### Questions
- What happens to methods that dont explicitly take in input and out but rather just modify class variables when called?
- Can this be adpted for pandas based projects if successful?

