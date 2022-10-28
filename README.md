# Spla3 Post Printer

## Overview
Spla3 Post Printer generates a Docker container for generating hex file using [Switch-Fightstick](https://github.com/Loloweb/Switch-Fightstick).


## Requirement
* Windows
* WSL (Ubuntu)
* Docker Engine 20.10.17
* Docker Compose 2.6.0
* Arduino UNO R3


## Usage

Clone this repository within WSL.
```
git clone https://github.com/akatohige/spla3_post_printer.git
cd ./spla3_post_printer
```

Store the image you want to post in `img/` directory under the name `post.png`.

Create and start a docker container.
```
docker compose up
```

When the process is completed, `hex/Joystick.hex` will be output.

Write the Joystick.hex file to Arduino using a writing tool such as  [dfu-programmer](https://dfu-programmer.github.io/).


## License
This repository is distributed under the [MIT License](http://opensource.org/licenses/mit-license.php).