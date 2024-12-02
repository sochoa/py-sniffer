from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="py-sniffer",
    version="0.1.0",
    author="sochoa",
    description="A Python package for sniffing network traffic and parsing packets.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sochoa/py-sniffer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.7",
    install_requires=[
        "scapy>=2.4.5",
    ],
    entry_points={
        "console_scripts": [
            "py-sniffer=py_sniffer.cli:main",
        ],
    },
    include_package_data=True,
)
