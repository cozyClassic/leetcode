use std::collections::HashMap;

fn get_key(string:&String) -> Vec<char> {
    let mut chars: Vec<char> = string.chars().collect();
    chars.sort_by(|a, b| b.cmp(a));
    chars
}

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map:HashMap<Vec<char>, Vec<String>> = HashMap::new();
        for s in strs {
            let key:Vec<char> = get_key(&s);
            let values = map.entry(key).or_insert(vec![]);
            values.push(s);
        }
        map.into_values().collect()
    }
}