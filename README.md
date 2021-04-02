# gdz

Gdz is a programme for pasing data from a web-site - https://12baliv.com.ua.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
$pip3 install bs4
$pip3 install re
$pip3 install requests
$pip3 install lxml
```

## Usage

```bash
{path-to-dir}$python3 Main.py
```
At same directory will be made [gdz.db]. There will be all parsed data.

## Work process

		|-------------------------|             |------------|
         	|     	Main.py        	  |------------>|   DB.py    |
		|-------------------------|             |------------|
                         /                                      ^
                        /                                       |
                       /           |--------------|             |
                      /      /-----|    data.py   |------\      |
                     /      /      |--------------|       \     |
                    /      /                               \    |  
                   ∨      ∨                                 ∨   |
            |----------------|                          |------------|
            |   control.py   |------------------------->| parser.py  |
            |----------------|                          |------------|
   
