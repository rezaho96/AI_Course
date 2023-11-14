from setuptools import setup

with open(r"PythonAdvanced\package\requirements.txt") as file1:
    required=file1.read().splitlines()
print(required)  
setup(
    name="packageReza",
    version='0.1.0',
    description="Hello ",
    author="Reza Hoseini",
    author_email="reza097@gmail.com",
    long_description=open(r"PythonAdvanced\package\README.txt").read(),
    packages=["myPackage"],
    install_requires=required,
    python_requires=">=3.8"
)