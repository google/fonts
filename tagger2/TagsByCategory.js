export default {
  props: ['tags', 'category'],
  computed: {
    filteredTags() {
      // Assumes each tag has a property 'tagName' for category
      return this.tags.filter(tag => tag.tagName === this.category);
    }
  },
  template: `
    <div>
      <h3>Tags for category: {{ category }}</h3>
      <ul>
        <li v-for="tag in filteredTags" :key="tag.family.name + tag.tagName">
          {{ tag.family.name }} (Score: {{ tag.score }})
        </li>
      </ul>
    </div>
  `
};
