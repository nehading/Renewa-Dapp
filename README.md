# Renewa
A decentralized application for trading RECs. The front end is powered by Flask and interacts with a NFT smart contract deployed on the Ropsten test network via web3.js.

How the dApp works: A user, identified by their connected Metamask account, can upload RECs. The RECs are automatically verified as valid by the smart contract and are stored as non-fungible ERC-721 tokens under the ownership of the user. Users can purchase RECs - the smart contract will automatically tranfer ownership of the REC to the user with the highest offer and will transfer funds from the buyer's account to the previous owner's account. A user can view which RECs are currently under their ownership. All of these transactions take place on the ethereum test network, meaning they are transparent, public, and can be used as immutable proof of ownership. The metamask chrome extension is needed to confirm transactions.

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/PublicKey.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/home.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/upload.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/minted_transaction.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/minted_receipt.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchase.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchase_transaction.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/purchaseReceipt.png?raw=true "Title")

![Alt text](https://github.com/neha-dhingra/Renewa/blob/main/Screenshots/view_owned.png?raw=true "Title")








