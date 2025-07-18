export default {
  props: ['tags', 'font'],
  computed: {
    filteredTags() {
      // Assumes each tag has a property 'family' with a 'name'
      return this.tags.filter(tag => tag.family && tag.family.name === this.font);
    },
    similarFamilies() {
      return this.$root.gf.similarFamilies(this.font, 10);
    },
    lintErrors() {
      return this.$root.gf.linter(this.$root.gf.lintRules, this.font, this.filteredTags);
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
      <select v-model="font">
        <option v-for="tag in tags.map(tag => tag.family.name).filter((value, index, self) => self.indexOf(value) === index)" :key="tag">
          {{ tag }}
        </option>
      </select>
      <p :style="{ fontFamily: font }" contenteditable="true" class="sample">
        Grumpy wizards make toxic brew for the evil Queen and Jack.
      </p>

      <ul>
        <li v-for="tag in filteredTags" :key="tag.tagName + tag.family.name + tag.score">
          <span class="tag-name">{{ tag.tagName }}</span>
           <input type="number" v-model="tag.score" @change="$emit('update:tags', tags)" />
           <button @click="removeTag(tag)">Remove</button>
        </li>
      </ul>
      <h3 v-if="similarFamilies.length">Similar families</h3>
      <ul>
        <li v-for="family in similarFamilies" :key="family" :style="{ fontFamily: family }">
          {{ family }} <button @click="addFontPanel(family)">Add</button>
        </li>
      </ul>
      <h3 v-if="lintErrors.length">Warnings</h3>
      <ul>
        <li v-for="error in lintErrors" :key="error.description" :class="{ 'tag-error': error.severity === 'ERROR', 'tag-warn': error.severity === 'WARN', 'tag-fail': error.severity === 'FAIL', 'tag-info': error.severity === 'INFO' }">
        {{ error.description }}
        </li>
      </ul>
    </div>
  `
};
