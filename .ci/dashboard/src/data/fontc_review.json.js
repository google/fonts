const sheet = await fetch(
  "https://docs.google.com/spreadsheets/d/1ao3k56FwQy6W0Ll5QbU_wpuKEvNPYcn8YyEU9_L8O4Q/gviz/tq?tqx=out:json&tq"
);
const text = await sheet.text();
const json = JSON.parse(text.substr(47).slice(0, -2));
var families = {};
for (const row of json.table.rows) {
  const family = row.c[0]?.v.split("/")?.pop();
  const reviewed = row.c[3]?.v;
  if (family && reviewed) {
    families[family] = reviewed;
  }
}
console.log(JSON.stringify(families));
