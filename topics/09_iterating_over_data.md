# Iteration over data
## Lists
- insert item at beginning of list?
  - array.insert(0,var)
`for my_element in my_list:`
    `print(my_element)`

## Dictionaries
IF we want to access keys and vals
`.items()`: if we don't use, not able to iterate over dictionaries. 
`for my_key, my_value in my_dict.items():`
    `print(my_key, my_value)`

IF we dont need to reference the value, don't need `.items()`:
  `for my_key in my_dict:`
    `print(my_key)`

Iterating w `.keys()` or `.values()`

# Iterating and special cases
- break: exits an entire loop
- continue: adnance one interation in a loop
- range(): creates a sequence

# Virtual Env
- Environments: sets of installed/running software/lang/packages/linbraries. 
- Virtual Envs: virutal env thats temp set up. 
- `venv`
