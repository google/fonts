export default {
    
//    schema: {
//        categories: ["a", "b", "c"],
//        lowTag: {
//            filters: [],
//            score: 10
//        },
//        highTag: {
//            filters: [],
//            score: 100
//        }
//    },

    props: ["categories"],
    data: function() {
        return {
            currentCategories: [],
            lowTag: {
                filters: [],
                score: 0
            },
            highTag: {
                filters: [],
                score: 0
            },
            currentLowAxis: "",
            currentLowPosition: 0,
            currentLowOp: "",
            currentLowScore: 0,
            currentHighAxis: "",
            currentHighPosition: 0,
            currentHighOp: "",
            currentHighScore: 0,
        }
    },
    methods: {
        addFilter() {
            this.lowTag.filters.push(
                {
                    axis: this.currentLowAxis,
                    op: this.currentLowOp,
                    value: this.currentLowPosition,
                    score: this.currentLowScore
                }
            );
            this.highTag.filters.push(
                {
                    axis: this.currentHighAxis,
                    op: this.currentHighOp,
                    value: this.currentHighPosition,
                    score: this.currentHighScore
                }
            );
            this.currentLowAxis = "";
            this.currentLowPosition = 0;
            this.currentLowOp = "";
            this.currentHighAxis = "";
            this.currentHighPosition = 0;
            this.currentHighOp = "";
        },
        addTags() {
            const filterSet = {
                categories: this.currentCategories,
                lowTag: this.lowTag,
                highTag: this.highTag
            };
            filterSet.lowTag.score = this.currentLowScore;
            filterSet.highTag.score = this.currentHighScore;
            this.$emit('tags-added', filterSet);
            this.currentCategories = [];
            this.lowTag = { filters: [], score: 0 };
            this.highTag = { filters: [], score: 0 };
            this.currentLowAxis = "";
            this.currentLowPosition = 0;
            this.currentLowOp = "";
            this.currentLowScore = 0;
            this.currentHighAxis = "";
            this.currentHighPosition = 0;
            this.currentHighOp = "";
            this.currentHighScore = 0;
        }
    },
    template: `
    <div class="frame">
        <h3>Add Tags</h3>
        <div>
            <h3>Categories</h3>
            <select v-model="currentCategories" multiple>
                <option v-for="category in categories" :key="category">
                    {{ category }}
                </option>
            </select>
            <h3>Low Tag:</h3>
            Score:
            <input type="number" v-model="currentLowScore" placeholder="Score" />
            <br>
            <input type="text" v-model="currentLowAxis" placeholder="Axis name" />
            <input type="number" v-model="currentLowPosition" placeholder="Position" />
            <select v-model="currentLowOp">
                <option value="<=">&lt;=</option>
                <option value=">=">&gt;=</option>
                <option value="=">=</option>
            </select>

            <h3>High Tag:</h3>
            Score:
            <input type="number" v-model="currentHighScore" placeholder="Score" />
            <br>
            <input type="text" v-model="currentHighAxis" placeholder="Axis name" />
            <input type="number" v-model="currentHighPosition" placeholder="Position" />
            <select v-model="currentHighOp">
                <option value="<=">&lt;=</option>
                <option value=">=">&gt;=</option>
                <option value="=">=</option>
            </select>
            <button @click="addFilter">Add Filter</button>
        </div>
        <div>
            <h3>Current Filters</h3>
            <h3>Low Tag</h3>
            <ul>
                <li v-for="filter in lowTag.filters" :key="filter.axis + filter.value">
                    {{ filter.axis }} {{ filter.op }} {{ filter.value }}
                    <button @click="lowTag.filters.splice(lowTag.filters.indexOf(filter), 1)">Remove</button>
                </li>
            </ul>
            <h3>High Tag</h3>
            <ul>
                <li v-for="filter in highTag.filters" :key="filter.axis + filter.value">
                    {{ filter.axis }} {{ filter.op }} {{ filter.value }}
                    <button @click="highTag.filters.splice(highTag.filters.indexOf(filter), 1)">Remove</button>
                </li>
            </ul>
        </div>
        <button @click="addTags">Add Tags</button>
    </div>
    `
}