export default {
    props: ["tag"],
    template: `
        <div class="tag-view">
            <div class="tag-title">
                <span class="tag-name">{{ tag.tagName }}</span>
                <span class="tag-family">{{ tag.family.name }}</span>
                <span class="tag-score">Score: {{ tag.score }}</span>
            </div>
            <div class="text-editor" contenteditable="true" :style="tag.cssStyle">
                Hello world
            </div>
        </div>
            
    `,
}