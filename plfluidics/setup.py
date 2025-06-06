import setuptools

setuptools.setup(
    name="plfluidics",
    version="0.1.0",
    author="Robert R. Puccinelli",
    author_email="robert.puccinelli@outlook.com",
    description="Microfluidic control utilities.",
    url="https://github.com/robertpuccinelli/microfluidic-software.git",
    python_requires='>=3.10',
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    package_data={'plfluidics':['server/configs/*.config', 
                                'server/scripts/*.scripts']},
    include_package_data=True,
    install_requires=[
        'flask',
        'ftd2xx',
    ],
    test_suite="tests",
)