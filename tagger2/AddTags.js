export default {
    
    schema: {
        categories: ["a", "b", "c"],
        lowTag: {
            filters: [],
            score: 10
        },
        highTag: {
            filters: [],
            score: 100
        }
    },

    props: ["categories"],
    data: function() {
        return {
            currentCategories: [],
            currentAxis: "",
            currentPosition: 0,
            currentOp: "",
            currentScore: 0,
            filters: [],
        }
    },
    methods: {
        addFilter() {
            this.filters.push(
                {
                    axis: this.currentAxis,
                    op: this.currentOp,
                    value: this.currentPosition,
                    score: this.currentScore
                }
            )
        },
        addTags() {
            const filterSet = {
                categories: this.currentCategories,
                filters: this.filters
            };
            this.$emit('tags-added', filterSet);
            this.filters = [];
        }
    },
    template: `
    <div>
        <h3>Add Tags</h3>
        <h3>Category</h3>
            <select v-model="currentCategories" multiple>
                <option v-for="category in categories" :key="category">
                    {{ category }}
                </option>
            </select>
        <div>
            <input type="text" v-model="currentAxis" placeholder="Axis name" />
            <input type="number" v-model="currentPosition" placeholder="Position" />
            <select v-model="currentOp">
                <option value="<=">&lt;=</option>
                <option value=">=">&gt;=</option>
                <option value="=">=</option>
            </select>
            <input type="number" v-model="currentScore" placeholder="Score" />
            <button @click="addFilter">Add Filter</button>
        </div>
        <div>
            <h3>Current Filters</h3>
            <ul>
                <li v-for="filter in filters" :key="filter.axis + filter.value">
                    {{ filter.axis }} {{ filter.op }} {{ filter.value }}
                    <button @click="filters.splice(filters.indexOf(filter), 1)">Remove</button>
                </li>
            </ul>
        </div>
        <button @click="addTags">Add Tags</button>
    </div>
    `
}