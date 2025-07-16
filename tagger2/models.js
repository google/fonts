async function loadText(path) {
    if (typeof window !== 'undefined' && window.fetch) {
        // Browser environment
        const response = await fetch(path);
        return await response.text();
    } else if (typeof require !== 'undefined') {
        // Node.js environment
        const fs = require('fs');
        const pathModule = require('path');
        const filePath = pathModule.join(__dirname, path);
        return fs.readFileSync(filePath, 'utf8')
    } else if (typeof process !== 'undefined' ) {
        // Node, but ESM module
        const fs = await import('fs');
        const pathModule = await import('path');
        const filePath = pathModule.join(process.cwd(), path);
        return fs.readFileSync(filePath, 'utf8');
    } else {
        throw new Error('Unknown environment');
    }
}

export class FontTag {
    constructor(tagName, family, axes, score) {
        this.tagName = tagName;
        this.family = family;
        this.axes = axes; // Array of axis objects
        this.score = score; // Score for the tag
    }
    toCSV() {
        const axesCSV = this.axes.map(axis => `${axis.tagName}:${axis.value}`).join(';');
        return `${this.tagName},${this.family.name},${axesCSV},${this.score}`;
    }
    get cssStyle() {
      if (this.axes.length === 0) {
        return `font-family: ${this.family.name}; font-size: 32pt;`;
      }
      // TODO after lunch
      let cleaned = this.family.name.replaceAll('"', '')
      let [name, axes] = cleaned.split(":");
      let [axisTag, axisCoords] = this.family.axes.split("@");
      let axisTags = axisTag.split(",");
      let axisCoordinates = axisCoords.split(",");
      let style = `font-family: "${name}", "Adobe NotDef"; font-size: 32pt; font-variation-settings:`;
      for (let i = 0; i < axisTags.length; i++) {
        style += ` '${axisTags[i]}' ${axisCoordinates[i]};`;
      }
      return style
    }

}

export class Font {
    constructor(name, axes) {
        this.name = name;
        this.axes = axes
    }
    get isVF() {
        return this.axes.length > 0;
    }
    get cssStyle() {
        if (!this.isVF) {
            return `font-family: '${this.name}'; font-size: 32pt;`;
        }
        let res = `font-family: '${this.name}'; font-size: 32pt; font-variation-settings:`;
        this.axes.forEach(axis => {
            res += ` '${axis.tag}' ${axis.min}..${axis.max},`;
        });
        return res.slice(0, -1) + ';'; // Remove trailing comma and add semicolon
    }
    get url() {
        let path = `https://fonts.googleapis.com/css2?family=${this.name.replaceAll(" ", "+")}`
        // GF api wants the axes in sorted alphabetical order. However, axes with
        // caps are last
        const sortedUpperCaseAxes = []
        const sortedLowerCaseAxes = []
        for (let a of this.axes) {
            if (a.tag.toUpperCase() === a.tag) {
            sortedUpperCaseAxes.push(a);
            } else {
            sortedLowerCaseAxes.push(a);
            }
        }
        sortedLowerCaseAxes.sort((a, b) => a.tag.localeCompare(b.tag));
        sortedUpperCaseAxes.sort((a, b) => a.tag.localeCompare(b.tag));
        const sortedAxes = [...sortedLowerCaseAxes, ...sortedUpperCaseAxes]
        if (this.axes.length > 0) {
            path += ":" + sortedAxes.map(a => {return a.tag}).join(",")
            path += "@";
            path += sortedAxes.map(axis => {return `${Number(axis.min)}..${Number(axis.max)}`}).join(",")
        }
        return path;
    }
}

export class GF {
    constructor() {
        this.familyData = {}; 
        this.families = [];
        this.lintRules = [];
    }
    async getFamilyData() {
        let data = await loadText('family_data.json');
        data = JSON.parse(data);
        let familyMeta = data["familyMetadataList"];
        let styleEmbeddingsData = await loadText('embeddings.json');
        let styleEmbeddings = JSON.parse(styleEmbeddingsData);
        familyMeta.forEach(family => {
            this.familyData[family.family] = family;
            if (family.family in styleEmbeddings) {
                this.familyData[family.family].style = styleEmbeddings[family.family];
            }
        });
    }
    async getLintRules() {
        let data = await loadText('tag_rules.csv');
        const lines = data.split('\n');
        for (let line of lines) {
            if (line.startsWith('#') || line.trim() === '') {
                continue;
            }
            let [rule, severity, description] = line.split(',');
            description = description.replace(/^"(.*)"$/, '$1');
            if (!rule || !description || !severity) {
                console.warn("Skipping line due to missing fields:", line);
                continue;
            }
            this.lintRules.push({
                rule: rule.trim(),
                description: description.trim(),
                severity: severity.trim()
            });
        }
    }
    loadFamilies() {
        for (let familyName in this.familyData) {
            const axes = []
            for (let axis of this.familyData[familyName].axes) {
                axes.push({
                    tag: axis.tag,
                    min: axis.min,
                    max: axis.max
                });
            }
            const family = new Font(familyName, axes);
            this.families.push(family);
        }
    }
    family(name) {
        return this.families.find(family => family.name === name);
    }
    similarFamilies(name, count = 10) {
        const family = this.familyData[name];
        if (!family || !family.style) {
            console.warn(`Family not found: ${name}`);
            return [];
        }
        let distances = Object.values(this.familyData).filter(
            f => f.style // New fonts may not have style embeddings
        ).map(f => {
            // Compute norm between the style embeddings
            let distance = family.style.map((value, index) => {
                return (value - (f.style[index] || 0)) ** 2;
            }).reduce((a, b) => a + b, 0);
            return [f.family, Math.sqrt(distance)];
        });
        distances.sort((a, b) => a[1] - b[1]);
        return distances.slice(0, count).map(item => item[0]).filter(familyName => familyName !== name);
    }
}

export class Tags {
    constructor(gf) {
        this.gf = gf;
        this.items = []
        this.loadTags();
        this.categories = [];
    }
    toCSV() {
        return this.items.map(tag => tag.toCSV()).join('\n');
    }
    addTag(tagName, fontName, axes, score) {
        const tag = new VFFontTag(tagName, fontName, axes, score);
        this.items.push(tag);
    }
    sort() {
        this.items.sort((a, b) => a.tagName.localeCompare(b.tagName));
    }
    sortCategories() {
        this.categories.sort((a, b) => a.localeCompare(b));
    }
    loadTags(commit) {
        if (commit === undefined) {
            commit = "refs/head/main"; // Default to main branch if no commit is specified
        }
        // TODO send this back to urls once testing is done
        loadText("families_new.csv")
        .then(csvText => {
            const lines = csvText.split('\n');
            for (let line of lines) {
                const [familyName, axes, tagName, score] = line.split(',');
                if (!familyName || !tagName) {
                    console.warn("Skipping line due to missing family name or tag name:", line);
                    continue;
                }
                const family = this.gf.family(familyName);
                if (family === undefined || family.name === undefined) {
                    console.warn("Family not found:", familyName);
                    continue;
                }
                const tag = new FontTag(tagName, family, [], score);
                this.items.push(tag);
                if (!this.categories.includes(tag.tagName)) {
                    this.categories.push(tag.tagName);
                }
            }
        })
    }
}
