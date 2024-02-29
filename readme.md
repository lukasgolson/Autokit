# autokit version 0.1.0



A framework for effortlessly integrating external tools into your Python projects.

## Installation

```bash
pip install autokit 
```

## Basic Usage
```python
import autokit 

class MyToolManager(autokit.ExternalToolManager):
    def __init__(self, config_path="my_tools.json"):
        super().__init__(config_path)  
 

# Get a tool instance and use its methods
tool = MyToolManager().get_tool("some_tool_name")
tool.run_command("arg1", "arg2")
```

## Features
- Automatic download and configuration of external tools on first use.
- Define tools and their commands in a configuration file.
- Streamlined execution of tool commands from within your Python code.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)


Contact: olson@student.ubc.ca