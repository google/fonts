export default {
  props: ['tags', 'font'],
  computed: {
    filteredTags() {
      // Assumes each tag has a property 'family' with a 'name'
      return this.tags.filter(tag => tag.family && tag.family.name === this.font);
    },
    similarFamilies() {
      return this.$root.gf.similarFamilies(this.font, 10);
    }
  },
  methods: {
    removeTag(tag) {
      this.$root.$emit('remove-tag', tag);
    },
    addFontPanel(font) {
      this.$root.panels.push({ type: 'font', font });
    }
  },
  template: `
    <div>
      <h3>Tags for:</h3>
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
      <p>Similar families</p>
      <ul>
        <li v-for="family in similarFamilies" :key="family" :style="{ fontFamily: family }">
          {{ family }} <button @click="addFontPanel(family)">Add</button>
        </li>
      </ul>
    </div>
  `
};
