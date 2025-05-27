from setuptools import setup, find_packages

setup(
    name="your_package_name",
    version="0.1.0",
    package_dir={"": "src"},      # Tells setuptools to look in 'src'
    packages=find_packages(where="src"),
    install_requires=[
        # Add any dependencies here, e.g. "numpy", "requests"
    ],
    python_requires=">=3.7",
    author="Yashaswy Govada",
    description="Pytest",
)
