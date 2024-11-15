import setuptools

setuptools.setup(
    name="plfluidics",
    version="0.0.1",
    author="Robert R. Puccinelli",
    author_email="robert.puccinelli@outlook.com",
    description="Microfluidic control utilities.",
    url="https://github.com/robertpuccinelli/microfluidic-software.git",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    install_requires=[
        'ftd2xx',
    ],
    test_suite="tests",
    classifiers=[
        "UCSF :: DeRisi Lab",
    ],
)