// // Allows us to use ES6 in our migrations and tests.
// require('babel-register')
// require('babel-polyfill')

module.exports = {
  networks: {
    development: {
        host: '127.0.0.1',
        port: 7545,
        network_id: '*', // Match any network id
    }
},
compilers: {
  solc: {
      version: '0.6.2', // Fetch exact version from solc-bin (default: truffle's version)
      settings: { // See the solidity docs for advice about optimization and evmVersion
          optimizer: {
              enabled: true,
              runs: 200,
          },
          evmVersion: 'constantinople',
      },
  },
},
};