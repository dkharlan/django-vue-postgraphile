<template>
    <ul>
        <todo-item v-for="item of items" :text="item.text"/>
    </ul>
</template>

<script>
import TodoItem from '@/components/TodoItem';

export default {
  name: "todo-list",
  components: {TodoItem}
};
</script>

<style scoped>

</style>
