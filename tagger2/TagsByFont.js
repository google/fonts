export default {
  props: ['tags', 'font'],
  computed: {
    filteredTags() {
      // Assumes each tag has a property 'family' with a 'name'
      return this.tags.filter(tag => tag.family && tag.family.name === this.font);
    }
  },
  template: `
    <div>
      <h3>Tags for fonter</h3>
      <select v-model="font" @change="filteredTags">
        <option v-for="tag in tags.map(tag => tag.family.name).filter((value, index, self) => self.indexOf(value) === index)" :key="tag">
          {{ tag }}
        </option>
      </select>
      <ul>
        <li v-for="tag in filteredTags" :key="tag.tagName + tag.family.name">
          {{ tag.tagName }} (Score: {{ tag.score }})
        </li>
      </ul>
    </div>
  `
};
