<template>
    <ul>
        <todo-item
            v-for="item of sortedItems"
            :key="item.id"
            :text="item.text" />
    </ul>
</template>

<script>
import TodoItem from '@/components/TodoItem';

export default {
  name: 'todo-list',
  components: {TodoItem},
  data() {
    return {
      items: []
    };
  },
  computed: {
    sortedItems() {
      return this.items
        .concat()
        .sort((a, b) => b.id - a.id);
    }
  },
  mounted() {
    fetch(__API_URL__ + '/todo/all')
      .then(response => response.json())
      .then(data => {
        this.items = data;
      });
  }
};
</script>

<style scoped>

</style>
