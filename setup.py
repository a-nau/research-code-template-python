from setuptools import setup, find_packages

# we don't distinguish between the project and environment requirements, for details
# see https://packaging.python.org/discussions/install-requires-vs-requirements/
with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="research_code_template_python",
    version="0.0.1",
    author="Naumann",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <4",
    install_requires=required_packages,
)
