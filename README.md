<h1 align="center">URL-to-QR Converter API</h1>

<div align="center">

![STATUS](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![LICENSE](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)

</div>

---

## 📝 Table of Contents

* [About](#about)
* [Getting Started](#getting_started)
* [Usage](#usage)
* [Authors](#authors)

## 🔎 About <a name = "about"></a>

This API is a simple Flask server that generates a QR code of the provided URL. The API takes a GET request with the URL as a parameter, generates the QR code and saves it as an image.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

In order to use this project, you will need to have the following software and libraries installed:  
* Flask
* qrcode

### Installing

To get started with this project, clone the repository to your local machine and install the required dependencies.

```bash
git clone https://github.com/jgfranco17/api-server.git
cd api-server
pip install -r requirements.txt
```

## 🚀 Usage <a name = "usage"></a>

### CLI usage

To run the API server in dev mode, simply execute either of the following commands:

```bash
# Default Python execution
python app.py --port PORT

# Or, after editing the Makefile to set a port number
make run
```

## Calling the API

To get a QR code for a link, simply send a `GET` request to the server, with the URL as a parameter.

```bash
http://localhost:PORT/qrcode?url=https://www.example.com
```

## ⛏️ Built Using <a name = "built_using"></a>
![Flask](https://img.shields.io/badge/Flask-2.2.2-1C1C1C?style=for-the-badge&logo=flask&logoColor=white) 

## ✒️ Authors <a name = "authors"></a>

* [Chino Franco](https://github.com/jgfranco17) 
