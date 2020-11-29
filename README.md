# Renewa
## Here's to a greener future!
A decentralized Ethereum application for trading RECs. The front end is powered by Flask and interacts with a NFT smart contract deployed on the Ropsten test network via web3.js.

### Development Steps:
1. An ERC-721 smart contract called DigitalREC.sol (which handles all of the trading logic on Ethereum) was created, compiled, and locally deployed using the Truffle framework. The smart contract was tested using Ganache.
2. Remix was used to compile the DigitalREC and Migration contracts. After getting eth from a faucet, the smart contracts were deployed onto the Ropsten test network using Remix. I retreived the contract addresses and ABI's in order to interact with these contracts.
3. In the Flask app, web3.js is used in order to interact with the smart contracts. An instance of the deployed smart contract was created using the saved ABI and contract address. This instance was then used to request transactions to interact with the deployed smart contract, and the transactionHashes and receipts (returned after sucessful mining) provided by the Ropsten test network were stored as proof of the transactions' occurrence. 
4. The Flask app uses Metamask in order to inject a web3 instance into the browser, and the Flask app automatically configures and connected with the user's Metamask account - as transactions (which use gas) must be confirmed or rejected, and the configured Metamask account also serves as the user's identity and wallet in this application. 

### How the dApp works: 
A user, identified by their connected Metamask account, can upload RECs. The RECs are automatically verified as valid and non-retired by the smart contract and are stored as non-fungible ERC-721 tokens under the ownership of the user. Users can purchase RECs - the smart contract will automatically tranfer ownership of the REC to the user with the highest offer and will transfer funds from the buyer's account to the previous owner's account. A user can view which RECs are currently under their ownership. All of these transactions take place on the ethereum test network, meaning they are transparent, public, and can be used as immutable proof of ownership. The metamask chrome extension is needed to allow transactions to go through.


#### The following screenshots walk through the dApp in chronological order:

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/PublicKey.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/home.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/upload.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/minted_transaction.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/minted_receipt.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchase.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchase_transaction.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchaseReceipt.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/view_owned.png?raw=true "Title")








