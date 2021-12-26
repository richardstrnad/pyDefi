from jsonrpcclient import request

import requests
import logging

logger = logging.getLogger('main.defi')
logger.addHandler(logging.NullHandler())


class Defi(object):
    def __init__(self, host, walletpassphrase):
        self.host = host
        self.walletpassphrase = walletpassphrase
        self.account = self._Account(self)
        self.blockchain = self._Blockchain(self)
        self.loan = self._Loan(self)
        self.pool = self._Pool(self)
        self.oracle = self._Oracle(self)
        self.token = self._Token(self)
        self.wallet = self._Wallet(self)

    def _request(self, method):
        resp = requests.post(
            self.host,
            json=method
        )
        if resp.status_code == 200:
            return resp.json().get('result')
        logger.error(
            f'Issue with the request, status code: {resp.status_code}'
        )
        logger.error('Dump of the json object')
        logger.error(resp.json())

    def unlock_wallet(self, duration=600):
        return self._request(
            request(
                "walletpassphrase",
                params=(
                    self.walletpassphrase,
                    duration
                )
            )
        )

    class _Wallet(object):
        def __init__(self, defi):
            self.defi = defi

        def sendToAddress(self, address, amount, comment='', comment_to='',
                          subtractfeefromamount=False):
            return self.defi._request(
                request(
                    "sendtoaddress",
                    params=(
                        address,
                        amount,
                        comment,
                        comment_to,
                        subtractfeefromamount
                    )
                )
            )

        def getBalance(self):
            return self.defi._request(
                request("getbalance")
            )

        def getBalances(self):
            return self.defi._request(
                request("getbalances")
            )

        def getWalletInfo(self):
            return self.defi._request(
                request("getwalletinfo")
            )

        def getAddressInfo(self, address):
            return self.defi._request(
                request(
                    "getaddressinfo",
                    params=(
                        address,
                    )
                )
            )

        def getTransaction(self, txid):
            return self.defi._request(
                request(
                    "gettransaction",
                    params=(
                        txid,
                    )
                )
            )

        def listUnspent(self):
            return self.defi._request(
                request("listunspent")
            )

        def getNewAddress(self, label=''):
            return self.defi._request(
                request(
                    "getnewaddress",
                    params=(
                        label,
                    )
                )
            )

    class _Loan(object):
        def __init__(self, defi):
            self.defi = defi

        def listVaults(self, ownerAddress):
            return self.defi._request(
                request(
                    "listvaults",
                    params=(
                        {'ownerAddress': ownerAddress},
                    )
                )
            )

        def getVault(self, vaultId):
            return self.defi._request(
                request(
                    "getvault",
                    params=(
                        vaultId,
                    )
                )
            )

        def listAuctions(self):
            return self.defi._request(
                request("listauctions")
            )

        def placeAuctionBid(self, vaultId, index, from_addr, amount):
            return self.defi._request(
                request(
                    "placeauctionbid",
                    params=(
                        vaultId,
                        index,
                        from_addr,
                        amount
                    )
                )
            )

    class _Pool(object):
        def __init__(self, defi):
            self.defi = defi

        def listPoolPairs(self):
            return self.defi._request(
                request("listpoolpairs")
            )

        def poolSwap(self, from_addr, tokenFrom, amountFrom, to_addr, tokenTo,
                     maxPrice=0):
            return self.defi._request(
                request(
                    "poolswap",
                    params={
                        'metadata': {
                            'from': from_addr,
                            'tokenFrom': tokenFrom,
                            'amountFrom': amountFrom,
                            'to': to_addr,
                            'tokenTo': tokenTo,
                            'maxPrice': maxPrice
                        }
                    })
            )

        def testPoolSwap(self, from_addr, tokenFrom, amountFrom, to_addr,
                         tokenTo, maxPrice=0):
            return self.defi._request(
                request(
                    "testpoolswap",
                    params={
                        'metadata': {
                            'from': from_addr,
                            'tokenFrom': tokenFrom,
                            'amountFrom': amountFrom,
                            'to': to_addr,
                            'tokenTo': tokenTo,
                            'maxPrice': maxPrice
                        }
                    })
            )

    class _Oracle(object):
        def __init__(self, defi):
            self.defi = defi

        def listOracles(self):
            return self.defi._request(
                request("listoracles")
            )

        def listPrices(self):
            return self.defi._request(
                request("listprices")
            )

    class _Token(object):
        def __init__(self, defi):
            self.defi = defi

        def listTokens(self):
            return self.defi._request(
                request("listtokens")
            )

        def mintTokens(self, amountToken, UXTO):
            return self.defi._request(
                request(
                    "minttokens",
                    params=(
                        amountToken,
                        UXTO
                    )
                )
            )

    class _Account(object):
        def __init__(self, defi):
            self.defi = defi

        def listAccountHistory(self):
            return self.defi._request(
                request("listaccounthistory")
            )

        def getTokenBalances(self):
            return self.defi._request(
                request("gettokenbalances")
            )

        def utxosToAccount(self, address, amount):
            return self.defi._request(
                request(
                    "utxostoaccount",
                    params=(
                            {address: f"{amount}@DFI"},
                    )
                )
            )

    class _Blockchain(object):
        def __init__(self, defi):
            self.defi = defi

        def getBlockchainInfo(self):
            return self.defi._request(
                request("getblockchaininfo")
            )
