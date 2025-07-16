export default {
  props: ['panel', 'tags'],
  methods: {
    remove() {
      this.$emit('remove');
    }
  },
  template: `
    <div class="panel" style="border:1px solid #ccc; padding:1em; margin-bottom:1em;">
      <button @click="remove" style="float:right">✕</button>
      <tags-by-font v-if="panel.type === 'font'" :tags="tags" :font="panel.font"></tags-by-font>
      <tags-by-categories v-else-if="panel.type === 'categories'" :tags="tags" :categories="panel.categories"></tags-by-categories>
    </div>
  `
};
