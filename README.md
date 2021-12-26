# WIP: pyDefi
Python SDK for the DeFiChain

## This is currently a WIP
Feel free to use it, but be aware that major changes can happen at anytime :)

## Usage
You need a Wallet to which you can connect, i'm currently using **defid** which
ships with the **DeFiChain CLI**. You can download the client on the offical 
DeFiChain Download page https://defichain.com/downloads/.

### DeFiChain RPC Auth
After you downloaded the **DeFiChain CLI** go to the **rpcauth** folder in it.
e.g. `defichain-2.3.1/share/defi/rpcauth` and create a user/pw hash.
`python3 rpcauth.py user password`. The output in the format 
`rpcauth=admin:XYZ$ABC` needs to be placed in the defi config file.
There are different places and it depends on the OS you are using, on my MAC
I simply used `/Users/username/Library/Application\ Support/Defi/defi.conf`
And then just placed the string in it.
```
→ cat /Users/richy/Library/Application\ Support/Defi/defi.conf
rpcauth=user:XYZ$ABC
```

### Basic Usage
```from pyDefi import Defi

host = 'http://user:password@localhost:8554/'
defi = Defi(host, 'WALLETPASSPRASE')
defi.unlock_wallet()
print(defi.wallet.getWalletInfo())
```