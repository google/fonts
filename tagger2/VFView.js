export default {
    props: ['families'],
    data: function() {
        return {
            fontSize: 32,
            selectedFamily: null,
        }
    },
    computed: {
        cssStyle() {
            let res = `font-family: '${this.selectedFamily.name}'; font-size: ${this.fontSize}pt;`;
            if (this.selectedFamily.isVF) {
                res += ' font-variation-settings:';
            }
            this.selectedFamily.axes.forEach(axis => {
                res += ` '${axis.tag}' ${axis.value},`;
            }
            );
            return res.slice(0, -1) + ';'; // Remove trailing comma and add semicolon
        }
    },
    template: `
    <div>
        <h1>Playground</h1>
        <select v-model="selectedFamily">
            <option v-for="family in families" :key="family.name" :value="family">
                {{ family.name }}
            </option>
        </select>
        <div v-if="selectedFamily">
            Font size:
            <input type="range" v-model="fontSize" min="8" max="100" default="32" /> {{ fontSize }}pt
            <div contenteditable="true" :style="cssStyle" style="border: 1px solid #ccc; padding: 1em;">
                Hello world
            </div>
            <div v-for="axis in selectedFamily.axes" :key="axis.tag">
                <label>{{ axis.tag }}: {{ axis.value }}</label>
                <input type="range" v-model="axis.value" :min="axis.min" :max="axis.max" />
            </div>
        </div>
    </div>

    `
}