# Python Serialization

This project demonstrates basic JSON serialization and deserialization in Python.

## Files

- `task_00_basic_serialization.py`
  - Contains functions to:
    - Serialize a Python dictionary to a JSON file
    - Deserialize JSON data back into a Python dictionary

- `main.py`
  - Test file for the serialization module

## Functions

### serialize_and_save_to_file(data, filename)

Serializes a Python dictionary and saves it to a JSON file.

### load_and_deserialize(filename)

Loads JSON data from a file and returns it as a Python dictionary.

## Example

```python
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
