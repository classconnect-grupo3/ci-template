# ci-template
# How to create a venv to test
# 1. Create a virtual environment
```bash
python3 -m venv venv
```
# 2. Activate the virtual environment
```bash
source venv/bin/activate
```
# 3. Install the required packages
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```