// eslint.config.js
module.exports = {
  languageOptions: {
    globals: {
      node: true,
    },
    parserOptions: {
      ecmaVersion: 2021, // or whatever version you're using
    },
  },
  extends: ['eslint:recommended'],
  rules: {
    'no-console': 'warn',
  },
};
