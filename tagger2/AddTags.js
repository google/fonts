export default {
    props: ["categories"],
    data: function() {
        return {
            currentAxis: "",
            currentPosition: 0,
            currentOp: "",
            filters: [],
        }
    },
    methods: {
        addFilter() {
            filters.push(
                {axis: this.currentAxis, op: this.currentOp, value: this.currentPosition}
            )
        }
    },
    template: `
        <input type="text" v-model="currentAxis" placeholder="Axis name" />
        <input type="number" v-model="currentPosition" placeholder="Position" />
        <select v-model="currentOp">
            <option value="<=">&lt;=</option>
            <option value=">=">&gt;=</option>
            <option value="=">=</option>
        </select>
        <button @click="addFilter">Add Filter</button>
    `
}