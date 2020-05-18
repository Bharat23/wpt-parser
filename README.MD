# WPT Parser

- ## [Getting Started](#getting-started)
    * [Prerequiste](#prerequiste)
    * [Installation](#installation)
    * [Examples](#example)
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

### Available Methods

- JSONParser

| Method | Params | type | default | Description 
| --- | --- | --- | --- | --- |
| pick | key | str | None | selects a key to be returned
| pick | keys | list | [] | selects a list key to be returned
| pick | key_delimiter | str | "." | Separator used to identify multi level JSON

- Fetch

| Method | Params | type | default | Description 
| --- | --- | --- | --- | --- |
| json | test_id | str | None | test_id for a wpt or a speed curve test

### Note:
 - The package is under development and will be prone to more frequent updates