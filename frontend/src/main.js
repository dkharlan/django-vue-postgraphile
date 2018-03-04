// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import {ApolloClient} from 'apollo-client';
import {HttpLink} from 'apollo-link-http';
import {InMemoryCache} from 'apollo-cache-inmemory';
import VueApollo from 'vue-apollo';
import App from './App';
import router from './router/index';
import APIPlugin from './plugins/api';

const httpLink = new HttpLink({
  uri: __GRAPHQL_ENDPOINT__
});

const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
  connectToDevTools: true
});

const apolloProvider = new VueApollo({
  defaultClient: apolloClient
});

Vue.use(VueApollo);
Vue.use(APIPlugin);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  provide: apolloProvider.provide(),
  components: { App },
  template: '<App/>'
});
