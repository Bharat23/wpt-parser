import setuptools

setuptools.setup(
    name="wpt-parser",
    package=['wpt-parser'],
    version="0.0.1",
    author="Bharat Sinha",
    author_email="bsinha@ancestry.com",
    description="A plug-n-play package to start using new relic APIs for data gathering",
    url="https://github.com/Bharat23/newrelic-api-parser",
    packages=setuptools.find_packages(),
    license='MIT',
    keywords = ['WPT parser', 'wpt', 'json'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
    ],
    install_requires=[
          'requests',
      ],
    python_requires='>=3.6',
)
