# yarn add -D node-gyp
# yarn add -D mocha chai
# mkdir test

rm -rf node_modules
yarn install
yarn node-gyp clean
yarn node-gyp configure
yarn node-gyp build

yarn test