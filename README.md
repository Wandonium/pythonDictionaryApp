# A Python CLI Dictionary App

This project uses the json library to read data from a json file. The data is a python dictionary containing a large number of words along with their definitions. Hence it can be used to create a simple cli dictionary of common english words and phrases.
The project can handle words in upper, lower and mixed cases.
The project can also handle misspelled words up to a point by using the difflib library

## Running the project

1.  Make sure you have python 3 installed

    ```
    $ sudo apt-get update
    $ sudo apt-get install python3.6
    ```

2.  Make sure you have the json and difflib libraries in your python installation

        These two libraries are usually supported natively by python

3.  Clone this repo: 

        git clone https://github.com/Wandonium/pythonDictionaryApp.git

4.  Change directory to the top-level project folder. No dependencies or packages needed.

        cd pythonDictionaryApp
        
5.  Run the project from the top level directory:

        python3 dictionary.py

## Authors

* **Wando Hillary**

## License

(The MIT License)

Copyright (c) 2019 Wando Hillary &lt;me@hillarywando.com&gt;

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

