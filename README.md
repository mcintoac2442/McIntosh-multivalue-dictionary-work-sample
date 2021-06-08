# Anthony McIntosh Spreetail Work Sample

### Multivalue Dictionary Class and Runner

This repository was written by Anthony McIntosh for a Spreetail interview work sample. It includes a class for a multivalue dictionary object, a runner to create and interact with this object, and a test suite for said class. The multivalue dictionary functions similarly to a normal python dictionary, however each key is allowed to be associated with a set of unique members/values, rather than just a single member.

### Requirements

It is recommended to run this application using Python 3.x or later. 

Python packages can be found [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Build Instructions

To run the program, first clone the repo onto your local machine. Navigate to where you would like to keep the program and run:

    git clone https://github.com/mcintoac2442/McIntosh-multivalue-dictionary-work-sample.git

Next, navigate to the multivalue_dict directory of the cloned repo. From this directory, with python 3.x or later installed, run:

    python3 runner.py

Now you should be interacting with the multivalue dictionary!

### Files Includes

runner.py: Contains main. Allows for user interactions with the multivalue dictionary via command line
multivalue_dict.py: Contains the MultiValueDictionary class
test_multivalue_dict.py: Contains the test suite for multivalue_dict.py
