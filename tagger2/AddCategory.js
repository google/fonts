export default {
    data: function() {
        return {
            category: "", // Input for new category
        }
    },
    methods: {
        addCategory() {
            if (this.category.trim() === "") {
                alert("Category name cannot be empty.");
                return;
            }
            this.$emit('category-added', this.category.trim());
            this.category = ""; // Reset the input field after adding
        }
    },
    template: `
        <div class="frame">
            <h3>Add new category</h3>
            <input type="text" v-model="category" placeholder="Category" />
            <button @click="addCategory">Add</button>
        </div>
    `
}