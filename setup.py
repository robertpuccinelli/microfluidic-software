import setuptools

setuptools.setup(
    name="plfluidics",
    version="0.0.1",
    author="Robert R. Puccinelli",
    author_email="robert.puccinelli@outlook.com",
    description="Microfluidic control utilities.",
    url="https://github.com/robertpuccinelli/microfluidic-software.git",
    python_requires='>=3.10',
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    install_requires=[
        'ftd2xx',
        'pyconfighandler@git+https://github.com/robertpuccinelli/PyConfigHandler#egg=pyconfighandler'
    ],
    test_suite="tests",
    classifiers=[
        "UCSF :: DeRisi Lab",
    ],
)