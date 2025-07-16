import { parse } from "./lint_grammar.js";

export function linter(rules, family, taglist) {
    const tagDict = taglist.reduce((acc, tag) => {
        acc[tag.tagName] = tag.score;
        return acc;
    }, {});
    const errors = [];
    for (const rule of rules) {
        try {
            const result = parse(rule.rule, { tags: tagDict, family  });
            if (result) {
                errors.push({
                    description: rule.description,
                    severity: rule.severity,
                });
            }
        } catch (error) {
            console.error("Error parsing rule:", rule.rule, error);
            errors.push({
                description: "Rule could not be parsed: " + rule.rule,
                severity: "ERROR",
            });
            continue;
        }
        
    }
    return errors;
}