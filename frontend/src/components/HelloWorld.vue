<template>
    <div class="hello">
        <h1>{{ msg }}<span v-if="name">, {{ name }}!</span></h1>
        <button v-on:click="sendMessage">Send A Message</button>
        <h2>Essential Links</h2>
        <ul>
            <li>
                <a href="https://vuejs.org" target="_blank">Core Docs</a>
            </li>
            <li>
                <a href="https://forum.vuejs.org" target="_blank">Forum</a>
            </li>
            <li>
                <a href="https://chat.vuejs.org" target="_blank">Community Chat</a>
            </li>
            <li>
                <a href="https://twitter.com/vuejs" target="_blank">Twitter</a>
            </li>
            <br>
            <li>
                <a href="http://vuejs-templates.github.io/webpack/" target="_blank">Docs for This Template</a>
            </li>
        </ul>
        <h2>Ecosystem</h2>
        <ul>
            <li>
                <a href="http://router.vuejs.org/" target="_blank">vue-router</a>
            </li>
            <li>
                <a href="http://vuex.vuejs.org/" target="_blank">vuex</a>
            </li>
            <li>
                <a href="http://vue-loader.vuejs.org/" target="_blank">vue-loader</a>
            </li>
            <li>
                <a href="https://github.com/vuejs/awesome-vue" target="_blank">awesome-vue</a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  mounted() {
    fetch(__API_URL__ + '/who_am_i', {credentials: 'include'}).then((response) => {
      response.json().then((data) => {
        this.name = data.username;
      });
    });
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
      name: null
    };
  },
  methods: {
    sendMessage() {
      fetch(__API_URL__ + '/tell_me_something/', {
        credentials: 'include',
        method: 'post',
        body: JSON.stringify({message: 'Hello from the frontend!'})
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
