import {FontTag} from "./models.js";

export default {
    props: ["categories"],
    data: function() {
        return {
            category: "", 
            newFamily: "",
            newScore: 0,
            isVF: false,
            axes: [],
            axisName: "",
            axisPositions: 2,
        }
    },
    methods: {
        addTag() {
            const tag = new FontTag(this.category, this.newFamily, [], this.newScore)
            this.$emit('tag-added', tag);
        },
        addVFTags() {
            // perform a cross product of the axes and their positions and create a new VF tag for each combination
            const solved = this.axesCombos(this.axes);
            for (let coordinateSet of solved) {
                const vfTag = new FontTag(this.category, this.newFamily, coordinateSet.axes, coordinateSet.score);
                this.$emit('tag-added', vfTag);
            }
        },
        addAxis() {
            console.log("Adding axis", this.axisName, this.axisPositions);
            const positions = [];
            for (let i = 0; i < this.axisPositions; i++) {
                positions.push({"coordinate": 0, "score": 0}); // Default position for each axis
            }
            this.axes.push({
                tag: this.axisName,
                positions: positions
            })
        },
        deleteAxis(axis) {
            const index = this.axes.indexOf(axis);
            if (index > -1) {
                this.axes.splice(index, 1);
            }
        },
        _axesCombos(axes, current = [], res = []) {
            if (current.length === axes.length) {
                const axisSet = {score: 0, axes: []};
                for (let i = 0; i < current.length; i++) {
                    axisSet.score += Number(current[i].score);
                    axisSet.axes.push({tag: axes[i].tag, coords: current[i].coordinate});
                }
                res.push(axisSet);
                return res;
            }
            for (let i = 0; i < axes[current.length].positions.length; i++) {
                this._axesCombos(axes, [...current, axes[current.length].positions[i]], res);
            }
            return res;
        },
        axesCombos(axes) {
            let axisSets = this._axesCombos(axes);
            axisSets.forEach((axisSet) => {
                axisSet.axes.forEach((axis) => {
                    delete axis.score;
                });
            });
            return axisSets;
        }
    },
    template: `
        <div class="frame">
            <h3>Add Tag</h3>
            <input type="checkbox" v-model="isVF" value="true" /> Variable Font
            <h3>Category</h3>
            <select v-model="category">
                <option v-for="category in categories" :key="category">
                    {{ category }}
                </option>
            </select>
            <h3>Family</h3>
            <input type="text" v-model="newFamily" placeholder="Add new family" />
            <div v-if="isVF">
                <input type="text" v-model="axisName" placeholder="Axis name" />
                <input type="number" v-model="axisPositions"/>
                <button @click="addAxis">Add Axis</button>
                <div v-for="axis in axes">
                    <h4>{{ axis.tag }}</h4>
                    <button @click="deleteAxis(axis)">Delete Axis</button>
                    <div v-for="(position, index) in axis.positions" :key="index">
                        Coordinate:
                        <input type="number" v-model="position.coordinate" placeholder="Position" />
                        Score:
                        <input type="number" v-model="position.score" placeholder="Score" />
                    </div>
                </div>
            <button @click="addVFTags">Add</button>
            </div>
            <div v-else>
                <input type="number" v-model="newScore" placeholder="Initial score" />
                <button @click="addTag">Add</button>
            </div>
        </div>
    `,
}