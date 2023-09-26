# Python + Blockchain - Your Guide to Building Full Stack DApps
Welcome to the Full Stack DApp Workshop! You'll learn how to build a decentralized application (DApp) using Python with web3.py for the blockchain interaction, Truffle for smart contract development, and Node.js for the frontend. By the end of this workshop, you'll have a solid understanding of how to create a full-stack DApp that can interact with the evm based blockchains.

# Introduction
### What is a DApp?
A DApp, short for decentralized application, is a type of software application that operates on a decentralized network, typically a blockchain. Unlike traditional applications, DApps don't rely on a centralized server, making them more transparent, secure, and resistant to censorship.

In this workshop, we will build a simple DApp that demonstrates the core principles of decentralized applications.

### Technologies Used
1. **web3.py**: A Python library that allows interaction with Ethereum and evm based blockchains, including reading data from the blockchain and sending transactions.

2. **Truffle**: A development environment, testing framework, and asset pipeline for Ethereum, aiming to make life as an Ethereum developer easier.

3. **Flask**: ```pip install Flask``` 

### Prerequisites

1. **Python**: Make sure you have Python 3.7 or later installed on your system.
You can see if you have Python already installed on your machine by going to your terminal and typing:

```$ python --version```

OR:

```$ python3 --version```

Next setup web3.py
``` $ pip install web3```

2. **Node.js and npm**: Install Node.js and npm (Node Package Manager) to manage JavaScript dependencies.

3. **Truffle**: Truffle is a popular development framework for Ethereum. Install it globally using npm:
```npm install -g truffle```
4. **RPC URL**: In order to connect to an Ethereum node with JSON RPC on the Main Net/ Test Net, we need access to a blockchain node. There are a few ways you could do this. For one, you could run your own Ethereum node with Geth or Parity. But this requires you to download a lot of data from the blockchain and keep it in sync. This is a huge headache if you've ever tried to do this before. For convenience, we will use [Infura](https://www.infura.io/) to access an Ethereum node without having to run one yourself. Infura is a service that provides a remote Ethereum node for free. All you need to do is sign up and obtain an API key and the RPC URL for the network you want to connect to.

Once you've signed up, your Infura RPC URL should look like this:

```https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY_GOES_HERE```

