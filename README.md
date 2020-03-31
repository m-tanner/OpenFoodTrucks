[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Show Open Food Trucks

This is a command line application to show all the open food trucks in San Francisco at the time when the application is run.
To determine which food trucks are open, it queries Socrata, which has online documentation (https://dev.socrata.com/foundry/data.sfgov.org/jjew-r69b).

## Setup
Create a new virtual Python environment. This example uses conda, but feel free to use that with which you're familiar.
```
conda create -n open_food_trucks python=3.7
conda activate open_food_trucks
```

Install the code and it's requirements
```
# Ensure you are in the project's root directory (where the setup.py file is)
cd open_food_trucks/
# Install the project and it's dependencies into the active Python environment
pip install .
# Or if you'd like to install in editable mode and develop further
pip install -e .
```

## Run
```
# Ensure you are in the Python environment where the projects and its dependencies were installed
# If you followed the example above and used conda
conda activate open_food_trucks
# Run the script by the name assigned in the setup.py
show-open-food-trucks
```

## Test
There are no tests. However, adding them would be straightforward.
