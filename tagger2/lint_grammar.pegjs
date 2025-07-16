Expression
    = head:Term _ "and" _ tail: Expression { return head && tail }
    / Negation / Term
 
Term =
    head:Value _ ">" _ tail:Value  { return head > tail }
/  head:Value _ ">=" _ tail:Value  { return head >= tail }
/  head:Value _ "<" _ tail:Value   { return head < tail }
/  head:Value _ "<=" _ tail:Value  { return head <= tail }
/  head:Value _ "==" _ tail:Value  { return head == tail }
/  head:Value _ "!=" _ tail:Value  { return head != tail }
/  head:Value _ "&" _ tail:Value   { return head & tail }
/  head:String _ "in" _ tail:Value { return tail.includes(head) }
/ head:Value { return head !== undefined && head }
    
Value = Tag / Integer / "family" { return options.family }
 
Negation = "not" _ head:Expression  { return !head }

Tag
  = "tag[\"" name:[A-Za-z/]+ "\"]" { return options.tags[name.join("")] }

Integer "integer"
  = _ [0-9]+ { return parseInt(text(), 10); }

_ "whitespace"
  = [ \t\n\r]*

String
  = "\"" string:[^"]+ "\"" { return string.join("") }