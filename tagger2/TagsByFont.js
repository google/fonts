export default {
  props: ['tags', 'font'],
  computed: {
    filteredTags() {
      // Assumes each tag has a property 'family' with a 'name'
      return this.tags.filter(tag => tag.family && tag.family.name === this.font);
    },
    lintErrors() {
      return this.$root.gf.linter(this.$root.gf.lintRules, this.font, this.filteredTags);
    }
  },
  methods: {
    removeTag(tag) {
      this.$root.$emit('remove-tag', tag);
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
          {{ tag.tagName }}
           <input type="number" v-model="tag.score" @change="$emit('update:tags', tags)" />
           <button @click="removeTag(tag)">Remove</button>
        </li>
      </ul>

      <ul>
        <li v-for="error in lintErrors" :key="error.description" :class="{ 'tag-error': error.severity === 'ERROR', 'tag-warn': error.severity === 'WARN', 'tag-fail': error.severity === 'FAIL', 'tag-info': error.severity === 'INFO' }">
          {{ error.description }}
        </li>
      </ul>
    </div>
  `
};
