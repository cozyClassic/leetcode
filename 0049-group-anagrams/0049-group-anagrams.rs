use std::collections::HashMap;

fn get_key(string:&String) -> Vec<char> {
    let mut chars: Vec<char> = string.chars().collect();
    chars.sort();
    chars
}

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map:HashMap<Vec<char>, Vec<String>> = HashMap::new();
        for s in strs {
            let values = map.entry(get_key(&s)).or_insert(vec![]).push(s);
        }
        map.into_values().collect()
    }
}