const env = require('dotenv').config();

const webpack = require("webpack");

module.exports = {
  // Global page headers (https://go.nuxtjs.dev/config-head)

  env: env.parsed,

  axios: {
    baseURL: process.env.API_URL
  },

  head: {
    title: 'MiniUnsplash',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {rel: "stylesheet", href:"bootstrap.min.css"},
    ],
    script:[
      {src: 'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js'},
      {src: 'https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js'}
    ]
  },

  server: {
    port: 8080,
    host: '0.0.0.0',
  },

  modules: [
      '@nuxtjs/axios',
      '@nuxtjs/auth',
      'nuxt-lazy-load',
      'vue-sweetalert2/nuxt'
  ],

  auth: {
    localStorage: false,
    cookie: {
        options: {
            expires: 7
        }
    },

    strategies: {
        local: {
            endpoints: {
                login: { url: '/users/login', method: 'post', propertyName: 'message' },
                logout: false,
                user: { url: '/images/filter-images', method: 'get', propertyName: 'message' }
            },
            tokenRequired: true,
            tokenType: 'mini-unsplash',
            tokenName: 'Authorization'
        }
    }
  },

  plugins: [
    {src: '~/plugins/vue-placeholders.js'},
    { src: '~/plugins/jquery.js', ssr: false },
  ],

  build: {

    vendor: ["jquery"],

    plugins: [
        new webpack.ProvidePlugin({
            $: "jquery"
        })
    ],

  }

}
