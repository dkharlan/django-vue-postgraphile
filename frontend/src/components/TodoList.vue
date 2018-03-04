<template>
    <ul>
        <todo-item v-for="item of items" :key="item.id" :text="item.text"/>
    </ul>
</template>

<script>
import TodoItem from '@/components/TodoItem';

export default {
  name: 'todo-list',
  props: ['items'],
  components: {TodoItem}
};
</script>

<style scoped>

</style>
