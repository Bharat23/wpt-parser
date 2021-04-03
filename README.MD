# WPT Parser

[![PyPI version](https://badge.fury.io/py/wpt-parser.svg)](https://badge.fury.io/py/wpt-parser)

- ## [Getting Started](#getting-started)
    * [Prerequiste](#prerequiste)
    * [Installation](#installation)
    * [Examples](#example)
        * [Key Types](#key-type)
- ## [Available Methods](#available-methods)

## Getting Started

- ### Prerequisites
    - Python >= 3.6.x
    - pip

- ### Installation
    ```
    $ pip install wpt-parser
    ```

- ### Examples
    - Using the JSON Parser
    ```
    # import the class
    from WPTParser.Fetch import Fetch
    from WPTParser.JSONParser import JSONParser
    
    test_json = Fetch().json()
    keys = ['data.median.firstView.loadTime',]
    # returns a new dict with specified keys
    JSONParser(test_json).pick(keys=keys).exec()

    ```
- ### Key Types:
    - #### key_name
        - Works like simple JSON extraction. Provide the name of the key and boom!.
        - For extraction from beyond first level, append keys with a separator and provide `key_delimiter` for the program to recognize the start of next level.
        - Example: 
        ```
        """
        {
            keylevel11: {
                keylevel21: value,
                keylevel22: {
                    keylevel31: value
                }
            }
        }
        """
        # key to extract first level
        # keylevel11
        # returns {keylevel21: ...}

        # key to extract second level, first key
        # keylevel11.keylevel21
        # returns value
        ```
    - #### [list_index]
        - When you have a list as value and you want to extract a specific index value/object.
        - For extraction from beyond first level, append keys with a separator and provide `key_delimiter` for the program to recognize the start of next level.
        - Example: 
        ```
        """
        {
            keylevel11: {
                keylevel21: [
                    1, 2, 3
                ],
                keylevel22: {
                    keylevel31: value
                }
            }
        }
        """
        # key to extract second level, third index
        # keylevel11.keylevel21.[2]
        # returns 3
        ```
    - #### [{key=value}]
        - When you have a unordered list of object and you want extract a specific object from the list based on the key and value inside the object
        - For extraction from beyond first level, append keys with a separator and provide `key_delimiter` for the program to recognize the start of next level.
        - Example: 
        ```
        """
        {
            keylevel11: {
                keylevel21: [
                    1, 2, 3
                ],
                keylevel22: {
                    keylevel31: value
                },
                keylevel23: [
                    {
                        name: Awesome,
                    },
                    {
                        name: Package
                    }
                ]
            }
        }
        """
        # key to extract second level, and from that extarct the object with name = Awesome
        # keylevel11.keylevel23.[{name=Awesome}]
        # return {name: Awesome}
        ```

### Available Methods

- JSONParser

| Method | Params | type | default | Description 
| --- | --- | --- | --- | --- |
| pick | key | str | None | selects a key to be returned
| pick | keys | list | [] | selects a list key to be returned
| pick | key_delimiter | str | "." | Separator used to identify multi level JSON
| pick | key_mapping | dict | {} | Mapping of keys for picking with custom key name. 

- Fetch

| Method | Params | type | default | Description 
| --- | --- | --- | --- | --- |
| json | test_id | str | None | test_id for a wpt or a speed curve test
| json | WPT_URI | str | 'https://webpagetest.org' | URI for your WPT instance

### Note:
 - The package is under development and will be prone to more frequent updates
