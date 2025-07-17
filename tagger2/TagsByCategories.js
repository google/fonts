export default {
  props: ['tags', 'categories'],
  data() {
    return {
      selectedCategories: [...this.categories],
      sortBy: 'family' // Default sorting option
    };
  },
  watch: {
    categories(newVal) {
      this.selectedCategories = [...newVal];
    }
  },
  computed: {
    filteredTags() {
      // Use selectedCategories for filtering
      const filtered = this.tags.filter(tag => this.selectedCategories.includes(tag.tagName));
      // Sort by family name and tag name
      if (this.sortBy === 'score') {
        return filtered.sort((a, b) => b.score - a.score);
      }
      if (this.sortBy === 'family') {
        return filtered.sort((a, b) => {
          if (a.family.name < b.family.name) return -1;
          if (a.family.name > b.family.name) return 1;
          if (a.tagName < b.tagName) return -1;
          if (a.tagName > b.tagName) return 1;
          return 0;
        });
      }
    },
    sortedCategories() {
      const res = this.tags.map(tag => tag.tagName)
        .filter((value, index, self) => self.indexOf(value) === index)
        .sort();
      return res;
    }
  },
  template: `
    <div>
      <h3>Tags for categories:</h3>
      <select v-model="sortBy">
        <option value="family">Family</option>
        <option value="score">Score</option>
      </select>
      <select v-model="selectedCategories" multiple>
        <option v-for="category in sortedCategories" :key="category">
          {{ category }}
        </option>
      </select>
        <div v-for="tag in filteredTags" :key="tag.family.name + tag.tagName + tag.score">
          <tag-view :tag="tag"></tag-view>
        </div>
    </div>
  `
};
