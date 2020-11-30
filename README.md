# Renewa
## Here's to a greener future!
A decentralized Ethereum application for trading RECs. The front end is powered by Flask and interacts with a NFT smart contract deployed on the Ropsten test network via web3.js.
<br> </br>
Note: This is only a prototype and is in the development stage.

### Development Steps:
1. A Solidity ERC-721 smart contract called DigitalREC.sol (which handles all of the trading logic on Ethereum) was created, compiled, and locally deployed using the Truffle framework. The smart contract was tested using Ganache.
2. Remix was used to compile the DigitalREC and Migration contracts. After getting eth from a faucet, the smart contracts were deployed onto the Ropsten test network using Remix. I retreived the contract addresses and ABI's in order to interact with these contracts.
3. In the Flask app, web3.js is used in order to interact with the smart contracts. An instance of the deployed smart contract was created using the saved ABI and contract address. This instance was then used to request transactions to interact with the deployed smart contract, and the transactionHashes and receipts (returned after sucessful mining) provided by the Ropsten test network were stored as proof of the transactions' occurrence. 
4. The Flask app uses Metamask in order to inject a web3 instance into the browser, and the Flask app automatically configures and connected with the user's Metamask account - as transactions (which use gas) must be confirmed or rejected, and the configured Metamask account also serves as the user's identity and wallet in this application. 

### How the dApp works: 
A user, identified by their connected Metamask account, can upload RECs. The RECs are automatically verified as valid and non-retired by the smart contract and are stored as non-fungible ERC-721 tokens under the ownership of the user. Users can purchase RECs - the smart contract will automatically tranfer ownership of the REC to the user with the highest offer and will transfer funds from the buyer's account to the previous owner's account. A user can view which RECs are currently under their ownership. All of these transactions take place on the ethereum test network, meaning they are transparent, public, and can be used as immutable proof of ownership. The metamask chrome extension is needed to allow transactions to go through.


#### The following screenshots walk through the dApp in chronological order:

A user enters their Ethereum address in order to configure Metamask.
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/PublicKey.png?raw=true "Title")
<br/> <br/>


From the dashboard, a user can choose to upload RECs to sell on the Renewa marketplace, can buy RECs, or can view the RECs that they legally have ownership of.
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/home.png?raw=true "Title")
<br/> <br/>


To upload an REC onto the marketplace, the user provides information about the REC and specifies a selling price based off of their state's market price.
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/upload.png?raw=true "Title")
<br/> <br/>


The user must confirm this transaction (as it uses gas) via Metamask, so that the REC can be verified with an external API, specific to the state in which the REC was generated, and so that the REC can be successfully minted as an ERC-721 standard token on the blockchain.
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/minted_transaction.png?raw=true "Title")
<br/> <br/>


A receipt and transaction hash is displayed to the user once this transaction is successfully mined as proof of completion (the ethereum network has been immutably altered to reflect the creation of the digital REC).
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/minted_receipt.png?raw=true "Title")
<br/> <br/>


A user who would like to purchase RECs can view all RECs from the marketplace and must specify the id of the one they would like to purchase.
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchase.png?raw=true "Title")
<br/> <br/>


The user must confirm this transaction (as it uses gas) via Metamask, so that the REC's legal ownership can be transferred over to the final buyer (the buyer with the highest offer with sufficient funds in their account). This transaction also transfers money from the user's account to the REC's previous owner's account. 
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchase_transaction.png?raw=true "Title")
<br/> <br/>


A receipt and transaction hash is displayed to the user once this transaction is successfully mined (as proof that the ethereum network has been altered to reflect the new owner of the REC and to reflect that the user indeed bought the REC). A user can also view their leftover balance after purchasing the REC.
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchaseReceipt.png?raw=true "Title")
<br/> <br/>


A user can view which REC ids they have legal ownership of (this again requires querying the smart contract and making a transaction in order to reflect the state of the Ropsten test network).
![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/view_owned.png?raw=true "Title")
<br/> <br/>


### ERC-721 Standard Smart Contract and External APIs:


The deployed smart contract was also stored on IPFS and its address and ABI are stored in DigitalRECSmartContractData.json so that the smart contract is available to the public. Users can use Ethereum Scan to publicly view all transactions and smart contract logic that takes place via our dApp. Our smart contract is based off of the ERC-721 standard, a Non-Fungible token that represents a distinct object, where the values of these tokens are derived from attributes of the object (such a rarity, or in our case the specific energy generated behind the REC). Our production level dApp will use Chainlink as an oracle in order for our ethereum smart contract to query external API's such as the M-RETS API (which are needed to verify a state-issued REC as valid).  








