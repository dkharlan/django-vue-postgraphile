<template>
    <ul>
        <todo-item
            v-for="item of items"
            :key="item.id"
            :text="item.text" />
    </ul>
</template>

<script>
import gql from 'graphql-tag';
import TodoItem from '@/components/TodoItem';

export default {
  name: 'todo-list',
  components: {TodoItem},
  data() {
    return {
      items: []
    };
  },
  apollo: {
    items: {
      query: gql`query {
        allApiTodoitems(orderBy: PRIMARY_KEY_DESC) {
          nodes {
            id
            text
          }
        }
      }`,
      update(data) {
        return data.allApiTodoitems.nodes;
      }
    }
  }
};
</script>

<style scoped>

</style>
